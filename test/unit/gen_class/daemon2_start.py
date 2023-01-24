# Classification (U)

"""Program:  daemon2_start.py

    Description:  Unit testing of Daemon2.start in gen_class.py.

    Usage:
        test/unit/gen_class/daemon2_start.py

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
        test_pid_not_exists
        test_pid_exists

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_file = "test/unit/gen_class/testfiles/daemon1_pid_file"
        self.pid_file2 = "test/unit/gen_class/testfiles/daemon1_pid_file2"
        self.daemon2 = gen_class.Daemon2(self.pid_file2)
        self.daemon = gen_class.Daemon2(self.pid_file)

    @mock.patch("sys.exit", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon2.daemonize", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon2.run", mock.Mock(return_value=True))
    @mock.patch("sys.stderr")
    def test_pid_not_exists(self, mock_write):

        """Function:  test_pid_not_exists

        Description:  Test with pid does not exists.

        Arguments:

        """

        mock_write.write.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(self.daemon2.start())

    @mock.patch("sys.exit", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon2.daemonize", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon2.run", mock.Mock(return_value=True))
    @mock.patch("sys.stderr")
    def test_pid_exists(self, mock_write):

        """Function:  test_pid_exists

        Description:  Test with pid exists.

        Arguments:

        """

        mock_write.write.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(self.daemon2.start())


if __name__ == "__main__":
    unittest.main()
