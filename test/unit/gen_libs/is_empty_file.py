# Classification (U)

"""Program:  is_empty_file.py

    Description:  Unit testing of is_empty_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/is_empty_file.py

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
        test_no_file
        test_data_file
        test_empty_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.no_file = "test/unit/gen_libs/testfiles/is_empty_file0.txt"
        self.empty_file = "test/unit/gen_libs/testfiles/is_empty_file.txt"
        self.data_file = "test/unit/gen_libs/testfiles/is_empty_file2.txt"

    def test_no_file(self):

        """Function:  test_no_file

        Description:  Test with no file.

        Arguments:

        """

        self.assertIsNone(gen_libs.is_empty_file(self.no_file))

    def test_data_file(self):

        """Function:  test_data_file

        Description:  Test with data in file.

        Arguments:

        """

        self.assertFalse(gen_libs.is_empty_file(self.data_file))

    def test_empty_file(self):

        """Function:  test_empty_file

        Description:  Test with empty file.

        Arguments:

        """

        self.assertTrue(gen_libs.is_empty_file(self.empty_file))


if __name__ == "__main__":
    unittest.main()
