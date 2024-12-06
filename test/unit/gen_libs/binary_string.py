# Classification (U)

"""Program:  binary_string.py

    Description:  Unit testing of binary_string in gen_libs.py.

    Usage:
        test/unit/gen_libs/binary_string.py

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
        test_binary_file
        test_text_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        base_path = "test/unit/gen_libs/testfiles"
        self.file = os.path.join(os.getcwd(), base_path, "binary_text")
        self.file2 = os.path.join(os.getcwd(), base_path, "binary_text2")

    def test_binary_file(self):

        """Function:  test_binary_file

        Description:  Test with binary in file.

        Arguments:

        """

        self.assertFalse(gen_libs.is_file_text(self.file2))

    def test_text_file(self):

        """Function:  test_text_file

        Description:  Test with text in file.

        Arguments:

        """

        self.assertTrue(gen_libs.is_file_text(self.file))


if __name__ == "__main__":
    unittest.main()
