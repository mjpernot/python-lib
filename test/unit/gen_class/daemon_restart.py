# Classification (U)

"""Program:  daemon_restart.py

    Description:  Unit testing of Daemon.restart in gen_class.py.

    Usage:
        test/unit/gen_class/daemon_restart.py

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
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default_settings

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pidfile = "test/unit/gen_class/testfiles/daemon_pidfile"
        self.daemon = gen_class.Daemon(self.pidfile)

    @mock.patch("gen_class.Daemon.stop", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon.start", mock.Mock(return_value=True))
    def test_default_settings(self):

        """Function:  test_default_settings

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(self.daemon.restart())


if __name__ == "__main__":
    unittest.main()
