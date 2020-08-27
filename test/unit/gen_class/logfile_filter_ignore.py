#!/usr/bin/python
# Classification (U)

"""Program:  logfile_filter_ignore.py

    Description:  Unit testing of LogFile.filter_ignore in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_filter_ignore.py

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
        test_case_insensitive -> Test with case insensitive ignore.
        test_no_find_use_marker -> Test no ignore found and use_marker is True.
        test_no_find -> Test with no ignore entries found.
        test_use_marker_arg -> Test with use_marker argument set to True.
        test_empty_ignore -> Test with empty ignore.
        test_empty_log -> Test with empty loglist.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.loglist = ["This", "is", "a", "test"]
        self.loglist2 = ["This is a test",
                         "This is another test",
                         "And yet another line",
                         "And this is a lowercase test",
                         "and the last line"]
        self.ignore = ["is", "a"]
        self.ignore2 = ["nothing"]
        self.ignore3 = ["AND"]
        self.result = ["test"]
        self.result2 = ["test"]
        self.result3 = ["a", "test"]
        self.result4 = ["This is a test",
                        "This is another test"]

    def test_case_insensitive(self):

        """Function:  test_case_insensitive

        Description:  Test with case insensitive ignore.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist2

        log.load_ignore(self.ignore3)
        log.filter_ignore()
        self.assertEqual(log.loglist, self.result4)

    def test_no_find_use_marker(self):

        """Function:  test_no_find_use_marker

        Description:  Test no ignore entries found and use_marker is True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.ignore = self.ignore2
        log.linemarker = 2

        log.filter_ignore(use_marker=True)
        self.assertEqual(log.loglist, self.result3)

    def test_no_find(self):

        """Function:  test_no_find

        Description:  Test with no ignore entries found.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.ignore = self.ignore2

        log.filter_ignore()
        self.assertEqual(log.loglist, self.loglist)

    def test_use_marker_arg(self):

        """Function:  test_use_marker_arg

        Description:  Test with use_marker argument set to True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.ignore = self.ignore
        log.linemarker = 2

        log.filter_ignore(use_marker=True)
        self.assertEqual(log.loglist, self.result2)

    def test_empty_ignore(self):

        """Function:  test_empty_ignore

        Description:  Test with empty ignore.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.ignore = []

        log.filter_ignore()
        self.assertEqual(log.loglist, self.loglist)

    def test_empty_log(self):

        """Function:  test_empty_log

        Description:  Test with empty loglist.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = []
        log.ignore = self.ignore

        log.filter_ignore()
        self.assertEqual(log.loglist, [])

    def test_default(self):

        """Function:  test_default

        Description:  Test get_marker method with default settings.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.ignore = self.ignore

        log.filter_ignore()
        self.assertEqual(log.loglist, self.result)


if __name__ == "__main__":
    unittest.main()
