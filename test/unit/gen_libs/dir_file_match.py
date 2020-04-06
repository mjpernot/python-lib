#!/usr/bin/python
# Classification (U)

"""Program:  dir_file_match.py

    Description:  Unit testing of dir_file_match in gen_libs.py.

    Usage:
        test/unit/gen_libs/dir_file_match.py

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
import mock

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
        test_file_search_path -> Test with files matching with path included.
        test_no_file_match -> Test with no files matching.
        test_file_match -> Test with files matching.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir_path = "test/unit/gen_libs/tmp/"
        self.list_files = ["file1.txt", "file2.txt", "test.txt"]
        self.results = []
        self.results2 = ["file1.txt", "file2.txt"]
        self.results3 = ["test/unit/gen_libs/tmp/file1.txt",
                         "test/unit/gen_libs/tmp/file2.txt"]
        self.file_str = "file"
        self.file_str2 = "none"

    @mock.patch("gen_libs.list_files")
    def test_file_search_path(self, mock_list):

        """Function:  test_file_search_path

        Description:  Test with files matching with path included.

        Arguments:

        """

        mock_list.return_value = self.list_files

        self.assertEqual(gen_libs.dir_file_match(
            self.dir_path, self.file_str, True), self.results3)

    @mock.patch("gen_libs.list_files")
    def test_no_file_match(self, mock_list):

        """Function:  test_no_file_match

        Description:  Test with no files matching.

        Arguments:

        """

        mock_list.return_value = self.list_files

        self.assertEqual(gen_libs.dir_file_match(self.dir_path,
                                                 self.file_str2),
                         self.results)

    @mock.patch("gen_libs.list_files")
    def test_file_match(self, mock_list):

        """Function:  test_file_match

        Description:  Test with files matching.

        Arguments:

        """

        mock_list.return_value = self.list_files

        self.assertEqual(gen_libs.dir_file_match(self.dir_path, self.file_str),
                         self.results2)


if __name__ == "__main__":
    unittest.main()
