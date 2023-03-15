# Classification (U)

"""Program:  daemon2_del_pid.py

    Description:  Unit testing of Daemon2.del_pid in gen_class.py.

    Usage:
        test/unit/gen_class/daemon2_del_pid.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default_setting

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_file = "Pid_File"
        self.daemon = gen_class.Daemon2(self.pid_file)

    @mock.patch("os.remove", mock.Mock(return_value=True))
    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(self.daemon.del_pid())


if __name__ == "__main__":
    unittest.main()
