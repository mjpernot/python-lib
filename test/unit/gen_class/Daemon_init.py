#!/usr/bin/python
# Classification (U)

"""Program:  Daemon_init.py

    Description:  Unit testing of Daemon.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/Daemon_init.py

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

    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        daemon_inst = gen_class.Daemon(self.pidfile)

        self.assertEqual((daemon_inst.argv_list, daemon_inst.pidfile),
                         ([], self.pidfile))


if __name__ == "__main__":
    unittest.main()
