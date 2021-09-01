#!/usr/bin/python
# Classification (U)

"""Program:  str_2_type.py

    Description:  Unit testing of str_2_type in gen_libs.py.

    Usage:
        test/unit/gen_libs/str_2_type.py

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
        test_with_tuple
        test_with_int

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.str1 = "100"
        self.int = 100
        self.str2 = "(1,2,3)"
        self.tuple = (1, 2, 3)
        self.str3 = "[1,2,3]"
        self.list = [1, 2, 3]

    def test_with_list(self):

        """Function:  test_with_list

        Description:  Test with converting string to list.

        Arguments:

        """

        self.assertEqual(gen_libs.str_2_type(self.str3), self.list)

    def test_with_tuple(self):

        """Function:  test_with_tuple

        Description:  Test with converting string to tuple.

        Arguments:

        """

        self.assertEqual(gen_libs.str_2_type(self.str2), self.tuple)

    def test_with_int(self):

        """Function:  test_with_int

        Description:  Test with converting string to integer.

        Arguments:

        """

        self.assertEqual(gen_libs.str_2_type(self.str1), self.int)


if __name__ == "__main__":
    unittest.main()
