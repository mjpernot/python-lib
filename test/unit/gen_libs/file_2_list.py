# Classification (U)

"""Program:  file_2_list.py

    Description:  Unit testing of file_2_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/file_2_list.py

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
        test_empty_file
        test_one_line_file
        test_multi_line_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.one_line = ["this is line one"]
        self.multi_line = ["this is line one", "this is line two"]

        self.empty_file = "test/unit/gen_libs/testfiles/file_2_list.txt"
        self.one_file = "test/unit/gen_libs/testfiles/file_2_list2.txt"
        self.multi_file = "test/unit/gen_libs/testfiles/file_2_list3.txt"

    def test_empty_file(self):

        """Function:  test_empty_file

        Description:  Test with empty file.

        Arguments:

        """

        self.assertEqual(gen_libs.file_2_list(self.empty_file), [])

    def test_one_line_file(self):

        """Function:  test_one_line_file

        Description:  Test one line in file.

        Arguments:

        """

        self.assertEqual(gen_libs.file_2_list(self.one_file), self.one_line)

    def test_multi_line_file(self):

        """Function:  test_multi_line_file

        Description:  Test multiple line file.

        Arguments:

        """

        self.assertEqual(gen_libs.file_2_list(self.multi_file),
                         self.multi_line)


if __name__ == "__main__":
    unittest.main()
