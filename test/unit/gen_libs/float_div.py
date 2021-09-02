#!/usr/bin/python
# Classification (U)

"""Program:  float_div.py

    Description:  Unit testing of float_div in gen_libs.py.

    Usage:
        test/unit/gen_libs/float_div.py

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
        setUp
        test_exception
        test_float_div

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.num = 0
        self.num1 = 10
        self.num2 = 2
        self.out = 0
        self.out2 = 5

    def test_exception(self):

        """Function:  test_exception

        Description:  Test with division by 0.

        Arguments:

        """

        self.assertEqual(gen_libs.float_div(self.num2, self.num), self.out)

    def test_float_div(self):

        """Function:  test_float_div

        Description:  Test float_div function.

        Arguments:

        """

        self.assertEqual(gen_libs.float_div(self.num1, self.num2), self.out2)


if __name__ == "__main__":
    unittest.main()
