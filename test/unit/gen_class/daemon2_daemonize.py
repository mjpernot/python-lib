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

        self.stderr = "test/unit/gen_class/tmp/daemonize2_stderr.txt"
        self.stdout = "test/unit/gen_class/tmp/daemonize2_stdout.txt"
        self.pid_file = "test/unit/gen_class/tmp/daemonize2_pid_file.txt"
        self.daemon = gen_class.Daemon2(
            self.pid_file, stdout=self.stdout, stderr=self.stderr)

    @mock.patch("os.umask", mock.Mock(return_value=True))
    @mock.patch("os.setsid", mock.Mock(return_value=True))
    @mock.patch("os.chdir", mock.Mock(return_value=True))
    @mock.patch("atexit.register", mock.Mock(return_value=True))
    @mock.patch("os.dup2", mock.Mock(return_value=None))
    @mock.patch("os.fork")
    def test_daemonize(self, mock_fork):

        """Function:  test_daemonize

        Description:  Test with successful daemon fork.

        Arguments:

        """

        mock_fork.side_effect = [False, False]

        self.assertFalse(self.daemon.daemonize())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.stderr):
            os.remove(self.stderr)

        if os.path.isfile(self.stdout):
            os.remove(self.stdout)

        if os.path.isfile(self.pid_file):
            os.remove(self.pid_file)


if __name__ == "__main__":
    unittest.main()
