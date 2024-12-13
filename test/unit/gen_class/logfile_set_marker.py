# Classification (U)

"""Program:  logfile_set_marker.py

    Description:  Unit testing of LogFile.set_marker in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_set_marker.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_empty
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.loglist = ["This", "is", "a", "test"]
        self.results = "test"

    def test_empty(self):

        """Function:  test_empty

        Description:  Test with empty loglist.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = []
        log.set_marker()

        self.assertIsNone(log.lastline)

    def test_default(self):

        """Function:  test_default

        Description:  Test set_marker method with default settings.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.set_marker()

        self.assertEqual(log.lastline, self.results)


if __name__ == "__main__":
    unittest.main()
