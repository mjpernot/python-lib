#!/usr/bin/python
# Classification (U)

"""Program:  validate_int.py

    Description:  Unit testing of validate_int in gen_libs.py.

    Usage:
        test/unit/gen_libs/validate_int.py

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
        test_with_char -> Test with character passed
        test_with_integer

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.int = 1
        self.char = "a"

    def test_with_char(self):

        """Function:  test_with_char

        Description:  Test with character passed.

        Arguments:

        """

        self.assertFalse(gen_libs.validate_int(self.char))

    def test_with_integer(self):

        """Function:  test_with_integer

        Description:  Test with integer passed.

        Arguments:

        """

        self.assertTrue(gen_libs.validate_int(self.int))


if __name__ == "__main__":
    unittest.main()
