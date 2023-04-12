# Classification (U)

"""Program:  daemon2_restart.py

    Description:  Unit testing of Daemon2.restart in gen_class.py.

    Usage:
        test/unit/gen_class/daemon2_restart.py

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
        test_default_settings

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_file = "test/unit/gen_class/testfiles/daemon2_pid_file"
        self.daemon = gen_class.Daemon2(self.pid_file)

    @mock.patch("gen_class.Daemon2.stop", mock.Mock(return_value=True))
    @mock.patch("gen_class.Daemon2.start", mock.Mock(return_value=True))
    def test_default_settings(self):

        """Function:  test_default_settings

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(self.daemon.restart())


if __name__ == "__main__":
    unittest.main()
