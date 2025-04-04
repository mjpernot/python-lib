# Classification (U)

"""Program:  bytes_2_readable.py

    Description:  Unit testing of bytes_2_readable in gen_libs.py.

    Usage:
        test/unit/gen_libs/bytes_2_readable.py

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
        test_with_negative
        test_with_1mb
        test_with_1025
        test_with_1024
        test_with_one
        test_with_zero

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    def test_with_negative(self):

        """Function:  test_with_negative

        Description:  Test with -1 bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.bytes_2_readable(1048577), "1.00MB")

    def test_with_1mb(self):

        """Function:  test_with_1mb

        Description:  Test with 1048577 bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.bytes_2_readable(1048577), "1.00MB")

    def test_with_1025(self):

        """Function:  test_with_1025

        Description:  Test with 1025 bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.bytes_2_readable(1025), "1.00KB")

    def test_with_1024(self):

        """Function:  test_with_1024

        Description:  Test with 1024 bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.bytes_2_readable(1024), "1024.00B")

    def test_with_one(self):

        """Function:  test_with_one

        Description:  Test with one bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.bytes_2_readable(1), "1.00B")

    def test_with_zero(self):

        """Function:  test_with_zero

        Description:  Test with zero bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.bytes_2_readable(0), "0.00B")


if __name__ == "__main__":
    unittest.main()
