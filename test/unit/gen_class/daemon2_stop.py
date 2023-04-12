# Classification (U)

"""Program:  daemon2_stop.py

    Description:  Unit testing of Daemon2.stop in gen_class.py.

    Usage:
        test/unit/gen_class/daemon2_stop.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import gen_class
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_pid_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_file = "Pid_File"
        self.daemon = gen_class.Daemon2(self.pid_file)

    @mock.patch("gen_class.Daemon2.get_pid_by_file",
                mock.Mock(return_value=None))
    def test_no_pid_file(self):

        """Function:  test_no_pid_file

        Description:  Test with no pid file found.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(self.daemon.stop())


if __name__ == "__main__":
    unittest.main()
