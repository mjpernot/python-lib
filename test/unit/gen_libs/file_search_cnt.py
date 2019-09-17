#!/usr/bin/python
# Classification (U)

"""Program:  file_search_cnt.py

    Description:  Unit testing of file_search_cnt in gen_libs.py.

    Usage:
        test/unit/gen_libs/file_search_cnt.py

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
        test_file_search_cnt -> Test with 0 pattern found.
        test_file_search_cnt2 -> Test with 1 pattern found.
        test_file_search_cnt3 -> Test with 2 pattern found.
        test_file_search_cnt4 -> Test with an empty file.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = "test/unit/gen_libs/tmp/file_search_cnt_test.txt"
        self.f_name2 = "test/unit/gen_libs/tmp/file_search_cnt_test2.txt"
        self.pattern = "quack"
        f_hdlr = open(self.f_name, "w")
        print("This is a test file", file=f_hdlr)
        print("This is a quick brown fox file", file=f_hdlr)
        f_hdlr.close()
        f_hdlr2 = open(self.f_name2, "w")
        f_hdlr2.close()

    def test_file_search_cnt(self):

        """Function:  test_file_search_cnt

        Description:  Test file_search_cnt function with 0 pattern found.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search_cnt(self.f_name, self.pattern),
                         0)

    def test_file_search_cnt2(self):

        """Function:  test_file_search_cnt2

        Description:  Test file_search_cnt function with 1 pattern found.

        Arguments:

        """

        self.pattern = "test"
        self.assertEqual(gen_libs.file_search_cnt(self.f_name, self.pattern),
                         1)

    def test_file_search_cnt3(self):

        """Function:  test_file_search_cnt3

        Description:  Test file_search_cnt function with 2 pattern found.

        Arguments:

        """

        self.pattern = "file"
        self.assertEqual(gen_libs.file_search_cnt(self.f_name, self.pattern),
                         2)

    def test_file_search_cnt4(self):

        """Function:  test_file_search_cnt4

        Description:  Test file_search_cnt function with an empty file.

        Arguments:

        """

        self.assertEqual(gen_libs.file_search_cnt(self.f_name2,
                                                  self.pattern), 0)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)
        os.remove(self.f_name2)


if __name__ == "__main__":
    unittest.main()
