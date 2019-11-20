#!/usr/bin/python
# Classification (U)

"""Program:  LogFile_filter_regex.py

    Description:  Unit testing of LogFile.filter_regex in gen_class.py.

    Usage:
        test/unit/gen_class/LogFile_filter_regex.py

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
        test_regex_multiple -> Test with multiple regex expressions.
        test_no_find_marker_chk -> Test no regex found and marker_chk is True.
        test_no_find -> Test with no regex entries found.
        test_marker_chk_arg -> Test with marker_chk argument set to True.
        test_empty_regex -> Test with empty regex.
        test_empty_log -> Test with empty loglist.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.loglist = ["2019-11 This", "20191-11 is", "2018-10 a",
                        "20-11 test"]
        self.regex = "^\d{4}-\d{2}"
        self.regex2 = "\d{4}:\d{2}"
        self.regex3 = "^\d{4}-\d{2}|^\d{2}-\d{2}"
        self.result = ["2019-11 This", "2018-10 a"]
        self.result2 = ["2018-10 a"]
        self.result3 = ["2019-11 This", "2018-10 a", "20-11 test"]

    def test_regex_multiple(self):

        """Function:  test_regex_multiple

        Description:  Test with multiple regex expressions.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.regex = self.regex3

        log.filter_regex()
        self.assertEqual(log.loglist, self.result3)

    def test_no_find_marker_chk(self):

        """Function:  test_no_find

        Description:  Test no regex entries found and marker_chk is True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.regex = self.regex2
        log.linemarker = 2

        log.filter_regex(marker_chk=True)
        self.assertEqual(log.loglist, [])

    def test_no_find(self):

        """Function:  test_no_find

        Description:  Test with no regex entries found.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.regex = self.regex2

        log.filter_regex()
        self.assertEqual(log.loglist, [])

    def test_marker_chk_arg(self):

        """Function:  test_marker_chk_arg

        Description:  Test with marker_chk argument set to True.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.regex = self.regex
        log.linemarker = 2

        log.filter_regex(marker_chk=True)
        self.assertEqual(log.loglist, self.result2)

    def test_empty_regex(self):

        """Function:  test_empty_regex

        Description:  Test with empty ignore.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.regex = ""

        log.filter_regex()
        self.assertEqual(log.loglist, self.loglist)

    def test_empty_log(self):

        """Function:  test_empty_log

        Description:  Test with empty loglist.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = []
        log.regex = self.regex

        log.filter_regex()
        self.assertEqual(log.loglist, [])

    def test_default(self):

        """Function:  test_default

        Description:  Test get_marker method with default settings.

        Arguments:

        """

        log = gen_class.LogFile()
        log.loglist = self.loglist
        log.regex = self.regex

        log.filter_regex()
        self.assertEqual(log.loglist, self.result)


if __name__ == "__main__":
    unittest.main()
