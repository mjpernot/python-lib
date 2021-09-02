#!/usr/bin/python
# Classification (U)

"""Program:  chk_int.py

    Description:  Unit testing of chk_int in gen_libs.py.

    Usage:
        test/unit/gen_libs/chk_int.py

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
        test_with_symbol
        test_with_char
        test_with_negative
        test_with_one
        test_with_zero

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    def test_with_symbol(self):

        """Function:  test_with_symbol

        Description:  Test with symbol.

        Arguments:

        """

        self.assertFalse(gen_libs.chk_int("a"))

    def test_with_char(self):

        """Function:  test_with_char

        Description:  Test with character.

        Arguments:

        """

        self.assertFalse(gen_libs.chk_int("a"))

    def test_with_negative(self):

        """Function:  test_with_negative

        Description:  Test with -1.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_int("-1"))

    def test_with_one(self):

        """Function:  test_with_one

        Description:  Test with 1.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_int("1"))

    def test_with_zero(self):

        """Function:  test_with_zero

        Description:  Test with 0.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_int("0"))


if __name__ == "__main__":
    unittest.main()
