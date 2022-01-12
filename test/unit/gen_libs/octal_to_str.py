#!/usr/bin/python
# Classification (U)

"""Program:  octal_to_str.py

    Description:  Unit testing of octal_to_str in gen_libs.py.

    Usage:
        test/unit/gen_libs/octal_to_str.py

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
        setUp
        test_four_perms_str
        test_four_perms
        test_three_perms_str
        test_three_perms
        test_two_perms_str
        test_two_perms
        test_eight_str
        test_eight
        test_seven_str
        test_seven
        test_six_str
        test_six
        test_five_str
        test_five
        test_four_str
        test_four
        test_three_str
        test_three
        test_two_str
        test_two
        test_one_str
        test_one
        test_zero_str
        test_zero
        test_empty_string

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    def test_four_perms_str(self):

        """Function:  test_four_perms_str

        Description:  Test with four permissions as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("7545"), "rwxr-xr--r-x")

    def test_four_perms(self):

        """Function:  test_four_perms

        Description:  Test with four permissions.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(7545), "rwxr-xr--r-x")

    def test_three_perms_str(self):

        """Function:  test_three_perms_str

        Description:  Test with three permissions as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("754"), "rwxr-xr--")

    def test_three_perms(self):

        """Function:  test_three_perms

        Description:  Test with three permissions.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(754), "rwxr-xr--")

    def test_two_perms_str(self):

        """Function:  test_two_perms_str

        Description:  Test with two permissions as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("75"), "rwxr-x")

    def test_two_perms(self):

        """Function:  test_two_perms

        Description:  Test with two permissions.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(75), "rwxr-x")

    def test_eight_str(self):

        """Function:  test_eight_str

        Description:  Test with seven as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("8"), "rwx")

    def test_eight(self):

        """Function:  test_eight

        Description:  Test with seven.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(8), "rwx")

    def test_seven_str(self):

        """Function:  test_seven_str

        Description:  Test with seven as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("7"), "rwx")

    def test_seven(self):

        """Function:  test_seven

        Description:  Test with seven.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(7), "rwx")

    def test_six_str(self):

        """Function:  test_six_str

        Description:  Test with six as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("6"), "rw-")

    def test_six(self):

        """Function:  test_six

        Description:  Test with six.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(6), "rw-")

    def test_five_str(self):

        """Function:  test_five_str

        Description:  Test with five as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("5"), "r-x")

    def test_five(self):

        """Function:  test_five

        Description:  Test with five.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(5), "r-x")

    def test_four_str(self):

        """Function:  test_four_str

        Description:  Test with four as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("4"), "r--")

    def test_four(self):

        """Function:  test_four

        Description:  Test with four.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(4), "r--")

    def test_three_str(self):

        """Function:  test_three_str

        Description:  Test with three as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("3"), "-wx")

    def test_three(self):

        """Function:  test_three

        Description:  Test with three.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(3), "-wx")

    def test_two_str(self):

        """Function:  test_two_str

        Description:  Test with two as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("2"), "-w-")

    def test_two(self):

        """Function:  test_two

        Description:  Test with two.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(2), "-w-")

    def test_one_str(self):

        """Function:  test_one_str

        Description:  Test with one as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("1"), "--x")

    def test_one(self):

        """Function:  test_one

        Description:  Test with one.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(1), "--x")

    def test_zero_str(self):

        """Function:  test_zero_str

        Description:  Test with zero as a string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str("0"), "---")

    def test_zero(self):

        """Function:  test_zero

        Description:  Test with zero.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(0), "---")

    def test_empty_string(self):

        """Function:  test_empty_string

        Description:  Test with empty string.

        Arguments:

        """

        self.assertEqual(gen_libs.octal_to_str(""), "")


if __name__ == "__main__":
    unittest.main()
