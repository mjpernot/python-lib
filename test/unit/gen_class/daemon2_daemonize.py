# Classification (U)

"""Program:  daemon2_daemonize.py

    Description:  Unit testing of Daemon2.daemonize in gen_class.py.

    Usage:
        test/unit/gen_class/daemon2_daemonize.py

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
        test_daemonize
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_file = "Pid_File"
        self.daemon = gen_class.Daemon2(self.pid_file)

    @mock.patch("os.umask", mock.Mock(return_value=True))
    @mock.patch("os.setsid", mock.Mock(return_value=True))
    @mock.patch("os.chdir", mock.Mock(return_value=True))
    @mock.patch("os.fork")
    def test_daemonize(self, mock_fork):

        """Function:  test_daemonize

        Description:  Test with successful daemon fork.

        Arguments:

        """

        mock_fork.side_effect = [False, False]

        self.assertFalse(self.daemon.daemonize())


if __name__ == "__main__":
    unittest.main()
