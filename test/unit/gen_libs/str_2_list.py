# Classification (U)

"""Program:  str_2_list.py

    Description:  Unit testing of str_2_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/str_2_list.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_with_space
        test_with_colon
        test_with_comma

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.str1 = "1,2,3,4"
        self.list = ["1", "2", "3", "4"]
        self.del1 = ","
        self.str2 = "1:2:3:4"
        self.del2 = ":"
        self.str3 = "1 2 3 4"
        self.del3 = " "

    def test_with_space(self):

        """Function:  test_with_space

        Description:  Test with space delimited string.

        Arguments:

        """

        self.assertEqual(gen_libs.str_2_list(self.str3, self.del3), self.list)

    def test_with_colon(self):

        """Function:  test_with_colon

        Description:  Test with colon delimited string.

        Arguments:

        """

        self.assertEqual(gen_libs.str_2_list(self.str2, self.del2), self.list)

    def test_with_comma(self):

        """Function:  test_with_comma

        Description:  Test with comma delimited string.

        Arguments:

        """

        self.assertEqual(gen_libs.str_2_list(self.str1, self.del1), self.list)


if __name__ == "__main__":
    unittest.main()
