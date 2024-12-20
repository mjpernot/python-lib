# Classification (U)

"""Program:  filename_search.py

    Description:  Unit testing of filename_search in gen_libs.py.

    Usage:
        test/integration/gen_libs/filename_search.py

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
        test_file_search_path
        test_no_file_search
        test_file_search2
        test_file_search

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.file1 = "file1.txt"
        self.dir_path = "test/integration/gen_libs/basefiles/"
        self.list_files = [self.file1, "file2.txt", "test.txt"]
        self.results = []
        self.results2 = ["md5_file.txt", self.file1, "file2.txt"]
        self.results3 = [self.file1]
        self.results4 = ["test/integration/gen_libs/basefiles/md5_file.txt",
                         "test/integration/gen_libs/basefiles/file1.txt",
                         "test/integration/gen_libs/basefiles/file2.txt"]
        self.file_str = "file"
        self.file_str2 = "none"
        self.file_str3 = "le1"

    def test_file_search_path(self):

        """Function:  test_file_search_path

        Description:  Test with files matching with path included.

        Arguments:

        """

        self.assertEqual(gen_libs.filename_search(
            self.dir_path, self.file_str, True).sort(), self.results4.sort())

    def test_no_file_search(self):

        """Function:  test_no_file_search

        Description:  Test with no files matching.

        Arguments:

        """

        self.assertEqual(gen_libs.filename_search(
            self.dir_path, self.file_str2), self.results)

    def test_file_search2(self):

        """Function:  test_file_search2

        Description:  Test with files matching.

        Arguments:

        """

        self.assertEqual(gen_libs.filename_search(
            self.dir_path, self.file_str3), self.results3)

    def test_file_search(self):

        """Function:  test_file_search

        Description:  Test with files matching.

        Arguments:

        """

        self.assertEqual(gen_libs.filename_search(
            self.dir_path, self.file_str).sort(), self.results2.sort())


if __name__ == "__main__":
    unittest.main()
