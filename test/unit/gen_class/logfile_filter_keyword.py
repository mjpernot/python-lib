#!/usr/bin/python
# Classification (U)

"""Program:  logfile_filter_keyword.py

    Description:  Unit testing of LogFile.filter_keyword in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_filter_keyword.py

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
        setUp
        test_case_insensitive
        test_all_predicate2
        test_all_predicate
        test_no_find_use_marker
        test_no_find
        test_use_marker_arg
        test_empty_keyword
        test_empty_log
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.loglist = ["This", "is", "a", "test"]
        self.loglist2 = ["This a", "is", "is a", "test is"]
        self.loglist3 = ["This is a test",
                         "This is another test",
                         "And yet another line",
                         "And this is a lowercase test",
                         "and the last line"]
        self.keyword = ["is", "a"]
        self.keyword2 = ["nothing"]
        self.keyword3 = ["AND"]
        self.result = ["This", "is", "a"]
        self.result2 = ["a"]
        self.result3 = ["This a", "is a"]
        self.result4 = ["And yet another line",
                        "And this is a lowercase test",
                        "and the last line"]

    def test_case_insensitive(self):

        """Function:  test_case_insensitive

        Description:  Test with case-insensitive searches.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist3

        log.load_keyword(self.keyword3)
        log.filter_keyword()
        self.assertEqual(log.loglist, self.result4)

    def test_all_predicate2(self):

        """Function:  test_all_predicate2

        Description:  Test with all predicate set with finds.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist2
        log.keyword = self.keyword
        log.predicate = all

        log.filter_keyword()
        self.assertEqual(log.loglist, self.result3)

    def test_all_predicate(self):

        """Function:  test_all_predicate

        Description:  Test with all predicate set.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.keyword = self.keyword
        log.predicate = all

        log.filter_keyword()
        self.assertEqual(log.loglist, [])

    def test_no_find_use_marker(self):

        """Function:  test_no_find

        Description:  Test no keyword entries found and use_marker is True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.keyword = self.keyword2
        log.linemarker = 2

        log.filter_keyword(use_marker=True)
        self.assertEqual(log.loglist, [])

    def test_no_find(self):

        """Function:  test_no_find

        Description:  Test with no keyword entries found.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.keyword = self.keyword2

        log.filter_keyword()
        self.assertEqual(log.loglist, [])

    def test_use_marker_arg(self):

        """Function:  test_use_marker_arg

        Description:  Test with use_marker argument set to True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.keyword = self.keyword
        log.linemarker = 2

        log.filter_keyword(use_marker=True)
        self.assertEqual(log.loglist, self.result2)

    def test_empty_keyword(self):

        """Function:  test_empty_keyword

        Description:  Test with empty keyword.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.keyword = []

        log.filter_keyword()
        self.assertEqual(log.loglist, self.loglist)

    def test_empty_log(self):

        """Function:  test_empty_log

        Description:  Test with empty loglist.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = []
        log.keyword = self.keyword

        log.filter_keyword()
        self.assertEqual(log.loglist, [])

    def test_default(self):

        """Function:  test_default

        Description:  Test get_marker method with default settings.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.keyword = self.keyword

        log.filter_keyword()
        self.assertEqual(log.loglist, self.result)


if __name__ == "__main__":
    unittest.main()
