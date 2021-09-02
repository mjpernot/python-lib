#!/usr/bin/python
# Classification (U)

"""Program:  dir_file_match.py

    Description:  Unit testing of dir_file_match in gen_libs.py.

    Usage:
        test/integration/gen_libs/dir_file_match.py

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
        test_file_search_path
        test_no_file_match
        test_file_match

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir_path = "test/integration/gen_libs/basefiles/"
        self.list_files = ["file1.txt", "file2.txt", "test.txt"]
        self.results = []
        self.results2 = ["file1.txt", "file2.txt"]
        self.results3 = ["test/integration/gen_libs/basefiles/file1.txt",
                         "test/integration/gen_libs/basefiles/file2.txt"]
        self.file_str = "file"
        self.file_str2 = "none"

    def test_file_search_path(self):

        """Function:  test_file_search_path

        Description:  Test with files matching with path included.

        Arguments:

        """

        self.assertEqual(gen_libs.dir_file_match(
            self.dir_path, self.file_str, True), self.results3)

    def test_no_file_match(self):

        """Function:  test_no_file_match

        Description:  Test with no files matching.

        Arguments:

        """

        self.assertEqual(gen_libs.dir_file_match(
            self.dir_path, self.file_str2), self.results)

    def test_file_match(self):

        """Function:  test_file_match

        Description:  Test with files matching.

        Arguments:

        """

        self.assertEqual(gen_libs.dir_file_match(self.dir_path, self.file_str),
                         self.results2)


if __name__ == "__main__":
    unittest.main()
