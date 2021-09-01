#!/usr/bin/python
# Classification (U)

"""Program:  is_pos_int.py

    Description:  Unit testing of is_pos_int in mysql_perf.py.

    Usage:
        test/unit/gen_libs/is_pos_int.py

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
        test_non_int
        test_zero
        test_negative
        test_positive

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    def test_non_int(self):

        """Function:  test_non_int

        Description:  Test with non-integer.

        Arguments:

        """

        self.assertFalse(gen_libs.is_pos_int("1"))

    def test_zero(self):

        """Function:  test_zero

        Description:  Test with zero.

        Arguments:

        """

        self.assertFalse(gen_libs.is_pos_int(0))

    def test_negative(self):

        """Function:  test_negative

        Description:  Test with negative number.

        Arguments:

        """

        self.assertFalse(gen_libs.is_pos_int(-1))

    def test_positive(self):

        """Function:  test_positive

        Description:  Test with positive number.

        Arguments:

        """

        self.assertTrue(gen_libs.is_pos_int(1))


if __name__ == "__main__":
    unittest.main()
