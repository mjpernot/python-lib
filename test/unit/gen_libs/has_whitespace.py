#!/usr/bin/python
# Classification (U)

"""Program:  has_whitespace.py

    Description:  Unit testing of has_whitespace in gen_libs.py.

    Usage:
        test/unit/gen_libs/has_whitespace.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
        test_empty_string -> Test with empty data string.
        test_multiple_space -> Test with multiple spaces in string.
        test_carriage_space -> Test with carriage return character.
        test_tab_space -> Test with tab character.
        test_newline_space -> Test with newline character.
        test_middle_space -> Test with white space in middle of string.
        test_begin_space -> Test with white space at beginning of string.
        test_end_space -> Test with white space at end of string.
        test_no_spaces -> Test with no white spaces.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = "DataString"
        self.data2 = "DataString "
        self.data3 = " DataString"
        self.data4 = "Data String"
        self.data5 = "Data String\n"
        self.data6 = "Data String\t"
        self.data7 = "Data String\r"
        self.data8 = "This is a data string"
        self.data9 = ""

    def test_empty_string(self):

        """Function:  test_empty_string

        Description:  Test with empty data string.

        Arguments:

        """

        self.assertFalse(gen_libs.has_whitespace(self.data9))

    def test_multiple_space(self):

        """Function:  test_multiple_space

        Description:  Test with multiple spaces in string.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data8))

    def test_carriage_space(self):

        """Function:  test_carriage_space

        Description:  Test with carriage return character.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data7))

    def test_tab_space(self):

        """Function:  test_tab_space

        Description:  Test with tab character.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data6))

    def test_newline_space(self):

        """Function:  test_newline_space

        Description:  Test with newline character.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data5))

    def test_middle_space(self):

        """Function:  test_middle_space

        Description:  Test with white space in middle of string.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data4))

    def test_begin_space(self):

        """Function:  test_begin_space

        Description:  Test with white space at beginning of string.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data3))

    def test_end_space(self):

        """Function:  test_end_space

        Description:  Test with white space at end of string.

        Arguments:

        """

        self.assertTrue(gen_libs.has_whitespace(self.data2))

    def test_no_spaces(self):

        """Function:  test_no_spaces

        Description:  Test with no white spaces.

        Arguments:

        """

        self.assertFalse(gen_libs.has_whitespace(self.data))


if __name__ == "__main__":
    unittest.main()
