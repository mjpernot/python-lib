#!/usr/bin/python
# Classification (U)

"""Program:  daemon_start.py

    Description:  Unit testing of Daemon.start in gen_class.py.

    Usage:
        test/unit/gen_class/daemon_start.py

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
        setUp -> Initialize testing environment.
        test_pid_not_exists -> Test with pid does not exists.
        test_pid_exists -> Test with pid exists.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pidfile = "test/unit/gen_class/testfiles/daemon_pidfile"
        self.pidfile2 = "test/unit/gen_class/testfiles/daemon_pidfile2"
        self.daemon2 = gen_class.Daemon(self.pidfile2)
        self.daemon = gen_class.Daemon(self.pidfile)

    @mock.patch("sys.exit", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon.daemonize", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon.run", mock.Mock(return_value=True))
    @mock.patch("sys.stderr")
    def test_pid_not_exists(self, mock_write):

        """Function:  test_pid_not_exists

        Description:  Test with pid does not exists.

        Arguments:

        """

        mock_write.write.return_value = True

        self.assertFalse(self.daemon2.start())

    @mock.patch("sys.exit", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon.daemonize", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon.run", mock.Mock(return_value=True))
    @mock.patch("sys.stderr")
    def test_pid_exists(self, mock_write):

        """Function:  test_pid_exists

        Description:  Test with pid exists.

        Arguments:

        """

        mock_write.write.return_value = True

        self.assertFalse(self.daemon.start())


if __name__ == "__main__":
    unittest.main()
