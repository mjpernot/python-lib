#!/usr/bin/python
# Classification (U)

"""Program:  validate_date.py

    Description:  Unit testing of validate_date in gen_libs.py.

    Usage:
        test/unit/gen_libs/validate_date.py

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
        test_with_char -> Test with character passed.
        test_invalid_format -> Test with invalid datetime group format.
        test_valid_format -> Test with valid datetime group format.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg1 = "2019-05-23 17:15:00"
        self.dtg2 = "2019/05/23 17:15:00"
        self.fmt = "%Y/%m/%d %H:%M:%S"

    def test_new_format(self):

        """Function:  test_new_format

        Description:  Test with new format passed.

        Arguments:

        """

        self.assertTrue(gen_libs.validate_date(self.dtg2, dtg_format=self.fmt))

    def test_invalid_format(self):

        """Function:  test_invalid_format

        Description:  Test with invalid datetime group format.

        Arguments:

        """

        self.assertFalse(gen_libs.validate_date(self.dtg2))

    def test_valid_format(self):

        """Function:  test_valid_format

        Description:  Test with valid datetime group format.

        Arguments:

        """

        self.assertTrue(gen_libs.validate_date(self.dtg1))


if __name__ == "__main__":
    unittest.main()
