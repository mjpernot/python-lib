#!/usr/bin/python
# Classification (U)

"""Program:  daemon_init.py

    Description:  Unit testing of Daemon.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/daemon_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_stderr_arg
        test_stdout_arg
        test_stdin_arg
        test_argv_list
        test_default_setting

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pidfile = "PidFile"
        self.argv_list = ["program", "arg1", "arg2"]
        self.stdin = "/path/file1"
        self.stdout = "/path/file2"
        self.stderr = "/path/file3"

    def test_stderr_arg(self):

        """Function:  test_stderr_arg

        Description:  Test with stderr arg passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon(self.pidfile, stderr=self.stderr)

        self.assertEqual((daemon_inst.stderr, daemon_inst.pidfile),
                         (self.stderr, self.pidfile))

    def test_stdout_arg(self):

        """Function:  test_stdout_arg

        Description:  Test with stdout arg passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon(self.pidfile, stdout=self.stdout)

        self.assertEqual((daemon_inst.stdout, daemon_inst.pidfile),
                         (self.stdout, self.pidfile))

    def test_stdin_arg(self):

        """Function:  test_stdin_arg

        Description:  Test with stdin arg passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon(self.pidfile, stdin=self.stdin)

        self.assertEqual((daemon_inst.stdin, daemon_inst.pidfile),
                         (self.stdin, self.pidfile))

    def test_argv_list(self):

        """Function:  test_argv_list

        Description:  Test with argv list passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon(self.pidfile, argv_list=self.argv_list)

        self.assertEqual((daemon_inst.argv_list, daemon_inst.pidfile),
                         (self.argv_list, self.pidfile))

    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        daemon_inst = gen_class.Daemon(self.pidfile)

        self.assertEqual((daemon_inst.argv_list, daemon_inst.pidfile),
                         ([], self.pidfile))


if __name__ == "__main__":
    unittest.main()
