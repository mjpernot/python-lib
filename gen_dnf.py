# Classification (U)

"""Program:  gen_dnf.py

    Description:  Class that has class definitions for dnf use.

    Function:

    Classes:
        Dnf

"""

# Libraries and Global Variables

# Standard
import socket
import distro
import dnf

# Local
try:
    from . import version

except (ValueError, ImportError) as err:
    import version

__version__ = version.__version__

# Global


class Dnf():
    """Class:  Dnf

    Description: Class which is a representation for python3-dnf class.  A
        dnf object is used as a proxy for using the dnf command.

    Methods:
        __init__
        capture_pkgs
        capture_repos
        fetch_install_pkgs
        fetch_repos
        fetch_update_pkgs
        get_all_repos
        get_distro
        get_enabled_repos
        get_hostname
        get_install_pkgs
        get_installed
        get_os
        get_release
        get_update_pkgs
        get_updates

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the Dnf class.

        Arguments:

        """

        self.base = dnf.Base()
        self.packages = None
        self.host_name = socket.gethostname()
        self.os_name = distro.name()
        self.release = distro.version()
        self.distro = (distro.name(), distro.version(), distro.codename())

    def capture_pkgs(self):

        """Method:  capture_pkgs

        Description:  Query for all installed packages on the system.

        Arguments:

        """

        self.base.fill_sack()
        self.packages = self.base.sack.query()

    def capture_repos(self):

        """Method:  capture_repos

        Description:  Query for all of the repos on the system.

        Arguments:

        """

        self.base.read_all_repos()
        self.base.fill_sack()

    def fetch_install_pkgs(self):

        """Method:  fetch_install_pkgs

        Description:  Return a dictionary of installed packages in a list.

        Note:  This is a backwards comptable function for programs that use
            the gen_class.Yum class.

        Arguments:
            (output) List of installed of packages in JSON format

        """

        pkgs = self.get_install_pkgs()

        return [{"package": pkg.name, "ver": pkg.version, "arch": pkg.arch}
                for pkg in pkgs]

    def fetch_repos(self):

        """Method:  fetch_repos

        Description:  Return a list of repos.

        Note:  This is a backwards comptable function for programs that use
            the gen_class.Yum class.

        Arguments:
            (output) List of repositories

        """

        return self.get_all_repos()

    def fetch_update_pkgs(self):

        """Method:  fetch_update_pkgs

        Description:  Return a list of dictionaries of packages that have
            updates.

        Note:  This is a backwards comptable function for programs that use
            the gen_class.Yum class.

        Arguments:
            (output) List of packages for installation in JSON format

        """

        query = self.get_update_pkgs()

        return [
            {"package": pkg.name, "ver": pkg.version, "arch": pkg.arch,
             "repo": pkg.reponame} for pkg in query.upgrades().latest(1)]

    def get_all_repos(self, url=False):

        """Method:  get_all_repos

        Description:  Return a list of all the repos on the system.

        Note: If including the url, then each item in the list will be a
            set.
            Postition:
                0: Repository Name
                1: Reposirory Base URL

        Arguments:
            (input) url -> True|False - Include the repos base URL
            (output) data -> List of repositories on the system

        """

        self.capture_repos()

        if url:
            data = [(rep.name, str(rep.baseurl))
                    for rep in self.base.repos.all()]

        else:
            data = [rep.name for rep in self.base.repos.all()]

        return data

    def get_distro(self):

        """Method:  get_distro

        Description:  Reuturn linux_distribution settings.

        Arguments:
            (output) self.distro -> Linux distribution as a tuple value

        """

        return self.distro

    def get_enabled_repos(self, url=False):

        """Method:  get_enabled_repos

        Description:  Return a list of enabled repos on the system.

        Note: If including the url, then each item in the list will be a
            set.
            Postition:
                0: Repository Name
                1: Reposirory Base URL

        Arguments:
            (input) url -> True|False - Include the repos base URL
            (output) data -> List of enabled repositories on the system

        """

        self.capture_repos()

        if url:
            data = [(rep.name, str(rep.baseurl))
                    for rep in self.base.repos.iter_enabled()]

        else:
            data = [rep.name for rep in self.base.repos.iter_enabled()]

        return data

    def get_hostname(self):

        """Method:  get_hostname

        Description:  Return the server's hostname.

        Arguments:
            (output) self.host_name -> Server host name

        """

        return self.host_name

    def get_install_pkgs(self):

        """Method:  get_install_pkgs

        Description:  Return installed packages.

        Arguments:
            (output) Class of installed packages

        """

        self.capture_pkgs()

        return self.packages.installed()

    def get_installed(self):

        """Method:  get_installed

        Description:  Return list of installed packages.

        Arguments:

        """

        ins_pkg = self.get_install_pkgs()

        return [str(pkg) for pkg in ins_pkg]

    def get_os(self):

        """Method:  get_os

        Description:  Return the operating system platform.

        Arguments:
            (output) self.os_name -> Server's Operating system name

        """

        return self.os_name

    def get_release(self):

        """Method:  get_release

        Description:  Return the OS kernel release version.

        Arguments:
            (output) self.release -> Kernel release version

        """

        return self.release

    def get_update_pkgs(self):

        """Method:  get_update_pkgs

        Description:  Return update packages.

        Arguments:
            (output) Class of update packages

        """

        self.capture_repos()

        return self.base.sack.query()

    def get_updates(self):

        """Method:  get_updates

        Description:  Return list of packages that have updates available.

        Arguments:

        """

        query = self.get_update_pkgs()

        return [str(pkg) for pkg in query.upgrades().latest(1)]
