#!/usr/bin/python
# Classification (U)

"""Program:  logfile_find_marker.py

    Description:  Unit testing of LogFile.find_marker in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_find_marker.py

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
        test_no_find_update -> Test with no marker found with update arg.
        test_no_find -> Test with no marker found.
        test_update_arg -> Test with update argument set to True.
        test_empty_marker -> Test with empty marker.
        test_empty_log -> Test with empty loglist.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.loglist = ["This", "is", "a", "test"]
        self.marker = "is"
        self.marker2 = "nofind"
        self.result = ["a", "test"]
        self.item = 2

    def test_no_find_update(self):

        """Function:  test_no_find_update

        Description:  Test with no marker found with update arg.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.marker = self.marker2

        log.find_marker(update=True)
        self.assertEqual((log.loglist, log.linemarker), (self.loglist, None))

    def test_no_find(self):

        """Function:  test_no_find

        Description:  Test with no marker found.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.marker = self.marker2

        log.find_marker()
        self.assertEqual((log.loglist, log.linemarker), (self.loglist, None))

    def test_update_arg(self):

        """Function:  test_update_arg

        Description:  Test with update argument set to True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.marker = self.marker

        log.find_marker(update=True)
        self.assertEqual((log.loglist, log.linemarker), (self.result, 0))

    def test_empty_marker(self):

        """Function:  test_empty_marker

        Description:  Test with empty marker.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist

        log.find_marker()
        self.assertEqual((log.loglist, log.linemarker), (self.loglist, None))

    def test_empty_log(self):

        """Function:  test_empty_log

        Description:  Test with empty loglist.

        Arguments:

        """

        log = gen_class.LogFile()
        log.marker = self.marker

        log.find_marker()
        self.assertEqual((log.loglist, log.linemarker), ([], None))

    def test_default(self):

        """Function:  test_default

        Description:  Test get_marker method with default settings.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.marker = self.marker

        log.find_marker()
        self.assertEqual((log.loglist, log.linemarker),
                         (self.loglist, self.item))


if __name__ == "__main__":
    unittest.main()
