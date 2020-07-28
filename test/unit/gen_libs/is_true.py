#!/usr/bin/python
# Classification (U)

"""Program:  is_true.py

    Description:  Unit testing of is_true in gen_libs.py.

    Usage:
        test/unit/gen_libs/is_true.py

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
        test_is_true_off -> Test with False value.
        test_is_true_on -> Test with True value.
        test_is_true_no -> Test with No value.
        test_is_true_yes -> Test with Yes value.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.is1 = "Yes"
        self.is2 = "No"
        self.is3 = "ON"
        self.is4 = "OFF"

    def test_is_true_off(self):

        """Function:  test_is_true_off

        Description:  Test with OFF value.

        Arguments:

        """

        self.assertEqual(gen_libs.is_true(self.is4), False)

    def test_is_true_on(self):

        """Function:  test_is_true_on

        Description:  Test with ON value.

        Arguments:

        """

        self.assertEqual(gen_libs.is_true(self.is3), True)

    def test_is_true_no(self):

        """Function:  test_is_true_no

        Description:  Test with No value.

        Arguments:

        """

        self.assertEqual(gen_libs.is_true(self.is2), False)

    def test_is_true_yes(self):

        """Function:  test_is_true_yes

        Description:  Test with Yes value.

        Arguments:

        """

        self.assertEqual(gen_libs.is_true(self.is1), True)


if __name__ == "__main__":
    unittest.main()
