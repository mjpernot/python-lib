# Classification (U)

###############################################################################
#
# Filename:     gen_class.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               None
#
###############################################################################

"""Program:  gen_class.py

    Description:  Class that has class definitions for general use.

    Classes:
        Daemon
        ProgressBar
        SingleInstanceException
        ProgramLock
        System
            Mail
        Logger
        Yum

"""

###############################################################################
# Libraries and Global Variables

# Standard
import os
import fcntl
import sys
import tempfile
import logging
import socket
import smtplib
import time
import atexit
import signal
import platform

# Third-party
import yum

# Local
import version

# Version Information
__version__ = version.__version__


class Daemon:

    """Class:  Daemon

    Description:

    Super-Class:
        None

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.
        daemonize -> Background the process and create a pidfile for tracking.
        delpid -> Remove pidfile from the file system.
        start -> Start the daemon process
        stop -> Kill the daemon process
        restart -> Restart the daemon process
        run -> Stub method holder, instance will contain the code to execute.

    """

    def __init__(self, pidfile, stdin="/dev/null", stdout="/dev/null",
                 stderr="/dev/null", argv_list=[]):

        """Method:  __init__

        Description:  Initialization of an instance of the Daemon class.

        Arguments:
            (input) pidfile -> Path and name of pidfile for program.
            (input) stdin -> Standard in setting.
            (input) stdout -> Standard out setting.
            (input) stderr -> Standard error setting.
            (input) argv_list -> List of command line options and values.

        """

        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self.argv_list = argv_list

    def daemonize(self):

        """Method:  daemonize

        Description:  Fork the program into a background process and create
            a pidfile to track the process.

        Note:  Will do the UNIX double-fork magic (see Stevens, "Advanced
            Programming in the UNIX Environment" for details.

        Arguments:
            None

        """

        # Do first fork
        try:
            pid = os.fork()

            if pid > 0:
                # Exit first parent
                sys.exit(0)

        except OSError, e:
            sys.stderr.write("Fork #1 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # Decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # Do second fork
        try:
            pid = os.fork()

            if pid > 0:
                # Exit from second parent
                sys.exit(0)

        except OSError, e:
            sys.stderr.write("Fork #2 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # Redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, "r")
        so = file(self.stdout, "a+")
        se = file(self.stderr, "a+", 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # Write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile, "w+").write("%s\n" % pid)

    def delpid(self):

        """Method:  delpid

        Description:  Remove pidfile from the file system.

        Arguments:
            None

        """

        os.remove(self.pidfile)

    def start(self):

        """Method:  start

        Description:  Start the daemon process.

        Arguments:
            None

        """

        # Check for a pidfile to see if the daemon already runs.
        try:
            pf = file(self.pidfile, "r")
            pid = int(pf.read().strip())
            pf.close()

        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exists.  Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):

        """Method:  stop

        Description:  Kill the daemon process.

        Arguments:
            None

        """

        # Get the pid from the pidfile
        try:
            pf = file(self.pidfile, "r")
            pid = int(pf.read().strip())
            pf.close()

        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist.  Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)

            # Not an error in a restart
            return

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)

        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)

            else:
                print(str(err))
                sys.exit(1)

    def restart(self):

        """Method:  restart

        Description:  Stop and restart the daemon process.

        Arguments:
            None

        """

        self.stop()
        self.start()

    def run(self):

        """Method:  run

        Description:  Stub method holder, will contain the code to execute.
            Override this method when subclassing Daemon.  It will be called
            after the process has been daemonized by start() or restart().

        Arguments:
            None

        """


class ProgressBar(object):

    """Class:  ProgressBar

    Description:  Class that displays and updates a progress bar for an ongoing
        operation.

    Super-Class:  object

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.
        update -> Calculates how the total number of blocks completed.
        calc_and_update -> Calculate the percentage completed.

    """

    def __init__(self, msg, width=20, progress_sym="#", empty_sym=" "):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgressBar class.

        Arguments:
            (input) msg -> General message describing the operation.
            (input) width -> Width of the progress bar.
            (input) progress_sym -> Character displaying completed.
            (input) empty_sym -> Character displaying uncompleted.

        """

        self.width = width

        if self.width <= 0:
            self.width = 20

        self.msg = msg
        self.progress_sym = progress_sym
        self.empty_sym = empty_sym

    def update(self, progress):

        """Method:  update

        Description:  Calculates the total number of blocks completed in the
            progress bar and displays the progress bar.

        Arguments:
            (input) progress -> Precentage completed in whole numbers.

        """

        total_blocks = self.width
        filled_blocks = int(round(progress / (100 / float(total_blocks))))
        empty_blocks = total_blocks - filled_blocks

        # Compile the progress bar of completed and uncompleted blocks.
        progress_bar = self.progress_sym * filled_blocks + self.empty_sym \
            * empty_blocks

        if not self.msg:
            self.msg = ""

        progress_msg = "\r{0} {1} {2}%".format(self.msg, progress_bar,
                                               progress)

        # Overwrite the existing progress bar with the updated progress bar.
        sys.stdout.write(progress_msg)
        sys.stdout.flush()

    def calc_and_update(self, done, total):

        """Method:  calc_and_update

        Description:  Calculate the percentage completed.

        Arguments:
            (input) done -> Number of items completed.
            (input) total -> Total number of items to complete.

        """

        progress = int(round((done / float(total)) * 100))
        self.update(progress)


class SingleInstanceException(BaseException):

    """Class:  SingleInstanceException

    Description:  Class exception for the ProgramLock class when an instance
        lock has been detected.

    Super-Class:  BaseException

    Sub-Classes:
        None

    Methods:
        None

    """

    pass


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class that creates a file lock instance and in which other
        programs using the same parameters will detect the lock as already
        present and prevent a second program instance from starting.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Class instance initilization.
        __del__ -> Deletion of the ProgramLock instance.

    """

    def __init__(self, argv, flavor_id=""):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgramLock class.

        Arguments:
            (input) argv -> Arguments from the command line.
            (input) flavor_id -> Unique identifier for an instance.

        """

        self.lock_created = False

        # Creates filename based on the full path to the program file.
        basename = os.path.splitext(os.path.abspath(argv[0]))[0].replace(
            "/", "-").replace(":", "-").replace("\\", "-") + "-%s" \
            % flavor_id + ".lock"

        self.lock_file = os.path.normpath(tempfile.gettempdir()) + "/" \
            + basename

        self.f_ptr = open(self.lock_file, "w")
        self.f_ptr.flush()

        # Creates a lock on the file, will fail if one is already present.
        try:
            fcntl.lockf(self.f_ptr, fcntl.LOCK_EX | fcntl.LOCK_NB)

        except IOError:
            raise SingleInstanceException()

        self.lock_created = True

    def __del__(self):

        """Method:  __del__

        Description:  Deletion of the ProgramLock instance.

        Arguments:
            None

        """

        if not self.lock_created:
            return

        fcntl.lockf(self.f_ptr, fcntl.LOCK_UN)

        if os.path.isfile(self.lock_file):
            os.unlink(self.lock_file)


class System(object):

    """Class:  System

    Description:  Class which is a representation of a Linux server.  A server
        object is used as a proxy for operating with the system.  The basic
        methods and attributes to contain information about the physical
        server.

    Super-Class:  object

    Sub-Classes:
        Mail

    Methods:
        __init__ -> Class instance initilization.
        set_host_name -> Set the hostname attribute.

    """

    def __init__(self, host=None, host_name=None):

        """Method:  __init__

        Description:  Initialization of an instance of the System class.

        Arguments:
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        self.host = host
        self.host_name = host_name

    def set_host_name(self, host_name=None):

        """Method:  set_host_name

        Description:  Set the hostname attribute either from argument or pull
            from the server.

        Arguments:
            (input) host_name -> Host name of server.

        """

        if host_name:
            self.host_name = host_name

        else:
            self.host_name = socket.gethostname()


class Mail(System):

    """Class:  Mail

    Description:  Class which is a representation of an email.  An email object
        is used as a proxy for creating an email.  The basic methods and
        attributes include reading in the message, creating the message body,
        and sending the email.

    Super-Class:  System

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.
        add_2_msg -> Add text to text string if data is present.
        read_stdin -> Add standard in to mail message.
        create_body -> Combines subject line & message into a single entity.
        send_mail -> Emails message out via smtp connection.
        print_email -> Print email to standard out.

    """

    def __init__(self, to, subj=None, frm=None, msg_type=None, host_name=None,
                 host=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail class.

        Arguments:
            (input) to -> To email address.
            (input) subj -> Subject line of mail.
            (input) msg_type -> Type of email being sent.
            (input) frm -> From email address.
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        super(Mail, self).__init__(host, host_name)

        self.subj = subj
        self.to = to
        self.frm = frm
        self.msg_type = msg_type
        self.msg = ""

    def add_2_msg(self, txt_ln=None):

        """Method:  add_2_msg

        Description:  Add text to text string if data is present.

        Arguments:
            (input) txt_ln -> Line of text to add to message.

        """

        if txt_ln:
            self.msg = self.msg + txt_ln

    def read_stdin(self):

        """Method:  read_stdin

        Description:  Loops through standard in and sends anything to be added
            to the message.

        Arguments:
            None

        """

        for ln in sys.stdin:
            self.add_2_msg(ln)

    def create_body(self):

        """Method:  create_body

        Description:  Combines subject line and message into a single entity.

        Arguments:
            None

        """

        # Pull first 30 characters from message.
        if not self.subj:
            self.subj = self.msg[:30]

        return "Subject: %s\n\n%s" % (self.subj, self.msg)

    def send_mail(self):

        """Method:  send_mail

        Description:  Opens connection to smtp and mails out the message body
            to the email address.  Call to create_body() puts "Subj:" into the
            message which is required for sendmail.

        Arguments:
            None

        """

        server = smtplib.SMTP("localhost")
        server.sendmail(self.frm, self.to, self.create_body())
        server.quit()

    def print_email(self):

        """Method:  print_email

        Description:  Prints email message to standard out.

        Arguments:
            None

        """

        return "To: %s\nFrom: %s\n%s" % (self.to, self.frm, self.create_body())


class Logger(object):

    """Class:  Logger

    Description:  Class which is a representation of a log file instance.  A
        Logger object is used as a proxy to implement the creation, formatting,
        writing to, and closing of a log file.

    Super-Class:  object

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.
        log_debug -> Write a debug message to log file.
        log_info -> Write a information message to log file.
        log_warn -> Write a warning message to log file.
        log_err -> Write a error message to log file.
        log_crit -> Write a critical message to log file.
        log_close -> Close the log file and drop the file handler.

    """

    def __init__(self, name, log_file, level="INFO", msg_fmt=None,
                 date_fmt=None, mode="a", **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Logger class.

        Arguments:
            (input) name -> Name of log handler.
            (input) log_file -> Name of log file to write to.
            (input) level -> Level of message to accept to the log file.
            (input) msg_fmt -> Format of a log file entry.
            (input) date_fmt -> Format of date and time for a log file entry.
            (input) mode -> a|w - Write mode to log file (append, write)
                NOTE:  Mode is not yet implemented.
            (input)  **kwargs:
                None

        """

        self.handler = logging.FileHandler(log_file)

        if not msg_fmt:
            msg_fmt = "%(asctime)s %(levelname)s %(message)s"

        self.formatter = logging.Formatter(msg_fmt, date_fmt)

        self.handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(name)

        if level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)

        elif level == "INFO":
            self.logger.setLevel(logging.INFO)

        elif level == "WARNING":
            self.logger.setLevel(logging.WARNING)

        elif level == "ERROR":
            self.logger.setLevel(logging.ERROR)

        elif level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)

        else:
            self.logger.setLevel(logging.INFO)

        self.logger.addHandler(self.handler)

    def log_debug(self, msg, **kwargs):

        """Method:  log_debug

        Description:  Writes message to log file at DEBUG level.

        Arguments:
            (input) msg -> Message to be written to log.
            (input)  **kwargs:
                None

        """

        self.logger.debug(msg)

    def log_info(self, msg, **kwargs):

        """Method:  log_info

        Description:  Writes message to log file at INFO level.

        Arguments:
            (input) msg -> Message to be written to log.
            (input)  **kwargs:
                None

        """

        self.logger.info(msg)

    def log_warn(self, msg, **kwargs):

        """Method:  log_warn

        Description:  Writes message to log file at WARNING level.

        Arguments:
            (input) msg -> Message to be written to log.
            (input)  **kwargs:
                None

        """

        self.logger.warning(msg)

    def log_err(self, msg, **kwargs):

        """Method:  log_err

        Description:  Writes message to log file at ERROR level.

        Arguments:
            (input) msg -> Message to be written to log.
            (input)  **kwargs:
                None

        """

        self.logger.error(msg)

    def log_crit(self, msg, **kwargs):

        """Method:  log_crit

        Description:  Writes message to log file at CRITICAL level.

        Arguments:
            (input) msg -> Message to be written to log.
            (input)  **kwargs:
                None

        """

        self.logger.critical(msg)

    def log_close(self, **kwargs):

        """Method:  log_close

        Description:  Closes the log file and removes the log handler.

        Arguments:
            (input) msg -> Message to be written to log.
            (input)  **kwargs:
                None

        """

        for handle in self.logger.handlers:
            handle.close()
            self.logger.removeHandler(handle)


class Yum(yum.YumBase):

    """Class:  Yum

    Description:  Class which is a representation for YumBase system class.  A
        yum object is used as a proxy for using the yum command.

    Super-Class:  yum.YumBase

    Sub-Classes:

    Methods:
        __init__ -> Class instance initilization.
        get_hostname -> Return the class' hostname
        get_os -> Return the class' OS platform.
        get_release -> Return the class' OS release version.
        get_distro -> Reuturn class' linux_distribution.
        fetch_repos -> Return a list of repos
        fetch_install_pkgs -> Return a dict of installed packages in a list.
        fetch_update_pkgs -> Return a dict of packages to be updated in a list.

    """

    def __init__(self, host_name=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Yum class.

        Arguments:
            (input) host_name -> Host name of server.

        """

        yum.YumBase.__init__(self)

        if host_name:
            self.host_name = host_name

        else:
            self.host_name = socket.gethostname()

        self.os = platform.system()
        self.release = platform.release()
        self.distro = platform.linux_distribution()

    def get_distro(self):

        """Method:  get_distro

        Description:  Reuturn class' linux_distribution.

        Arguments:
            (output) self.distro -> Linux distribution tuple value.

        """

        return self.distro

    def get_hostname(self):

        """Method:  get_hostname

        Description:  Return the class' hostname.

        Arguments:
            (output) self.host_name -> Server's host name.

        """

        return self.host_name

    def get_os(self, **kwargs):

        """Method:  get_os

        Description:  Return the class' OS platform.

        Arguments:
            (output) self.os -> Server's Operating system name.

        """

        return self.os

    def get_release(self, **kwargs):

        """Method:  get_release

        Description:  Return the class' OS release version.

        Arguments:
            (output) self.release -> Kernel release version.

        """

        return self.release

    def fetch_repos(self):

        """Method:  fetch_repos

        Description:  Return a list of repos.

        Arguments:
            (output) List of repositories.

        """

        self.doRepoSetup()

        return [repo.name for repo in self.repos.listEnabled()]

    def fetch_install_pkgs(self):

        """Method:  fetch_install_pkgs

        Description:  Return a dictionary of installed packages in a list.

        Arguments:
            (output) List of installed of packages in JSON format.

        """

        return [{"Package": pkg.name, "Ver": pkg.version, "Arch": pkg.arch}
                for pkg in self.rpmdb]

    def fetch_update_pkgs(self):

        """Method:  fetch_update_pkgs

        Description:  Return a dictionary of packages to be updated in a list.

        Arguments:
            (output) List of packages to be installed/updated in JSON format.

        """

        return [{"Package": pkg.name, "Ver": pkg.version, "Arch": pkg.arch,
                 "Repo": str(getattr(pkg, "repo"))}
                for pkg in self.doPackageLists(pkgnarrow="updates",
                                               patterns="",
                                               ignore_case=True)]