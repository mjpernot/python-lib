#!/usr/bin/python
# Classification (U)

"""Program:  arg_dir_chk.py

    Description:  Unit testing of arg_dir_chk in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_dir_chk.py

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
import mock

# Local
sys.path.append(os.getcwd())
import arg_parser
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        
        test_match_no_dir
        test_match_no_access
        test_one_match_between_sets
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_chk_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        dir1 = "/test_path/dir1"
        self.args_array = {}
        self.args_array2 = {"-d": dir1}
        self.args_array3 = {"-d": dir1, "-g": "/test_path/dir2"}
        self.args_array4 = {"-d": "/dir/path/dirname13"}
        self.args_array5 = {"-d": "/dir/path/dirname17"}
        self.dir_chk_list = []
        self.dir_chk_list2 = ["-d"]
        self.dir_chk_list3 = ["-d", "-g"]
        self.dir_chk_list4 = ["-d", "-i"]
        self.dir_chk_list5 = ["-g"]

    @mock.patch("arg_parser.os")
    def test_match_no_dir(self, mock_os):

        """Function:  test_match_no_dir

        Description:  Test with directory does not exist.

        Arguments:

        """

        mock_os.path.isdir.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_chk_list2))

    @mock.patch("arg_parser.os")
    def test_match_no_access(self, mock_os):

        """Function:  test_match_no_access

        Description:  Test with match between sets, but no read access to
            directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_chk_list2))

    @mock.patch("arg_parser.os")
    def test_one_match_between_sets(self, mock_os):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets and is directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = True

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_chk_list2))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_chk_list5))

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array, self.dir_chk_list2))

    def test_empty_dir_chk_list(self):

        """Function:  test_empty_dir_chk_list

        Description:  Test with dir_chk_list is empty.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_chk_list))


if __name__ == "__main__":
    unittest.main()
