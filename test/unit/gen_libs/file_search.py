#!/usr/bin/python
# Classification (U)

"""Program:  file_search.py

    Description:  Unit testing of file_search in gen_libs.py.

    Usage:
        test/unit/gen_libs/file_search.py

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
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_no_str_found -> Test with no string found.
        test_str_found_first_line -> Test string found in first line.
        test_str_found_last_line -> Test string found in last line.
        test_str_found_first_instance -> Test found with multiple matches.
        test_str_found_middle_line -> Test string found in middle line.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.first_str = "line one"
        self.last_str = "line four"
        self.no_str = "line zero"
        self.multi_str = "line two"
        self.middle_str = "line three"

        self.match_first = "this is line one\n"
        self.match_last = "this is line four\n"
        self.match_multi = "this is line two\n"
        self.match_middle = "this is line three\n"

        self.f_name = "test/unit/gen_libs/testfiles/file_search.txt"

    def test_no_str_found(self):

        """Function:  test_no_str_found

        Description:  Test with no string found.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search(self.f_name, self.no_str), None)

    def test_str_found_first_line(self):

        """Function:  test_str_found_first_line

        Description:  Test string found in first line.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search(self.f_name, self.first_str),
                         self.match_first)

    def test_str_found_last_line(self):

        """Function:  test_str_found_last_line

        Description:  Test string found in last line.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search(self.f_name, self.last_str),
                         self.match_last)

    def test_str_found_first_instance(self):

        """Function:  test_str_found_first_instance

        Description:  Test found with multiple matches.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search(self.f_name, self.multi_str),
                         self.match_multi)

    def test_str_found_middle_line(self):

        """Function:  test_str_found_middle_line

        Description:  Test string found in middle line.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search(self.f_name, self.middle_str),
                         self.match_middle)


if __name__ == "__main__":
    unittest.main()
