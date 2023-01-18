# Classification (U)

"""Program:  daemon2_init.py

    Description:  Unit testing of Daemon2.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/daemon2_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_argv_list
        test_default_setting

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_file = "Pid_File"
        self.argv_list = ["program", "arg1", "arg2"]
        self.argv_list2 = list()
        self.stdout = "/path/file2"
        self.stderr = "/path/file3"

    def test_stderr_arg(self):

        """Function:  test_stderr_arg

        Description:  Test with stderr arg passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon2(self.pid_file, stderr=self.stderr)

        self.assertEqual((daemon_inst.stderr, daemon_inst.pid_file),
                         (self.stderr, self.pid_file))

    def test_stdout_arg(self):

        """Function:  test_stdout_arg

        Description:  Test with stdout arg passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon2(self.pid_file, stdout=self.stdout)

        self.assertEqual((daemon_inst.stdout, daemon_inst.pid_file),
                         (self.stdout, self.pid_file))

    def test_argv_list(self):

        """Function:  test_argv_list

        Description:  Test with argv list passed.

        Arguments:

        """

        daemon_inst = gen_class.Daemon2(
            self.pid_file, argv_list=self.argv_list)

        self.assertEqual((daemon_inst.argv_list, daemon_inst.pid_file),
                         (self.argv_list, self.pid_file))

    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        daemon_inst = gen_class.Daemon2(self.pid_file)

        self.assertEqual((daemon_inst.argv_list, daemon_inst.pid_file),
                         (self.argv_list2, self.pid_file))


if __name__ == "__main__":
    unittest.main()
