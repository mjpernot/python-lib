#!/usr/bin/python
# Classification (U)

"""Program:  list_filter_files.py

    Description:  Unit testing of list_filter_files in gen_libs.py.

    Usage:
        test/unit/gen_libs/list_filter_files.py

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
        setUp -> Unit testing initilization.
        test_multi_files -> Test with multiple files selected in directory.
        test_one_file_select -> Test with one file selected in directory.
        test_no_files_select -> Test with no files selected in directory.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir_path = "test/unit/gen_libs/tmp"
        self.file_filter3 = "*.txt"
        self.file_filter1 = "*.md"
        self.file_filter2 = "*.py"
        self.fname1 = os.path.join(self.dir_path, "file1.py")
        self.fname2 = os.path.join(self.dir_path, "file2.txt")
        self.fname3 = os.path.join(self.dir_path, "file3.txt")
        self.fname4 = os.path.join(self.dir_path, "file4.cfg")

        with open(self.fname1, "a"):
            os.utime(self.fname1, None)

        with open(self.fname2, "a"):
            os.utime(self.fname2, None)

        with open(self.fname3, "a"):
            os.utime(self.fname3, None)

        with open(self.fname4, "a"):
            os.utime(self.fname4, None)

        self.results1 = []
        self.results2 = ["test/unit/gen_libs/tmp/file1.py"]
        self.results3 = ["test/unit/gen_libs/tmp/file3.txt",
                         "test/unit/gen_libs/tmp/file2.txt"]
        self.results4 = ["test/unit/gen_libs/tmp/file2.txt",
                         "test/unit/gen_libs/tmp/file3.txt"]

    def test_multi_files(self):

        """Function:  test_multi_files

        Description:  Test with multiple files selected in directory.

        Arguments:

        """

        file_list = gen_libs.list_filter_files(self.dir_path,
                                               self.file_filter3)

        self.assertTrue(
            file_list == self.results3 or file_list == self.results4)

    def test_one_file_select(self):

        """Function:  test_one_file_select

        Description:  Test with one file selected in directory.

        Arguments:

        """

        self.assertEqual(gen_libs.list_filter_files(self.dir_path,
                                                    self.file_filter2),
                         self.results2)

    def test_no_files_select(self):

        """Function:  test_no_files_select

        Description:  Test with no files selected in directory.

        Arguments:

        """

        self.assertEqual(gen_libs.list_filter_files(self.dir_path,
                                                    self.file_filter1),
                         self.results1)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.fname1)
        os.remove(self.fname2)
        os.remove(self.fname3)
        os.remove(self.fname4)


if __name__ == "__main__":
    unittest.main()
