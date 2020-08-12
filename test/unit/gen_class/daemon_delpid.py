#!/usr/bin/python
# Classification (U)

"""Program:  daemon_delpid.py

    Description:  Unit testing of Daemon.delpid in gen_class.py.

    Usage:
        test/unit/gen_class/daemon_delpid.py

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
        test_default_setting -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pidfile = "PidFile"
        self.daemon = gen_class.Daemon(self.pidfile)

    @mock.patch("os.remove", mock.Mock(return_value=True))
    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(self.daemon.delpid())


if __name__ == "__main__":
    unittest.main()
