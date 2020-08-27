#!/usr/bin/python
# Classification (U)

"""Program:  arg_dir_chk_crt.py

    Description:  Unit testing of arg_dir_chk_crt in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_dir_chk_crt.py

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


def raise_oserror(dirname):

    """Function:  raise_oserror

    Description:  Stub holder to return a raised OSError exception.

    Arguments:

    """

    if dirname == "/test_path/dir1" or dirname == "/test_path/dir2":
        raise OSError(21, "Other Error")

    elif dirname == "/dir/path/dirname13":
        raise OSError(13, "Permission denied")

    elif dirname == "/dir/path/dirname17":
        raise OSError(17, "File exist")


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_create_dir_perm -> Test with permission denied to create dir.
        test_create_dir_exist -> Test with file exist to create directory.
        test_not_subset -> Test with dir_crt_list not subset of dir_chk_list.
        test_chk_good_crt_fail -> Test check dir good, but create dir failed.
        test_match_create_dir_fail -> Test with failing to create directory.
        test_match_create_dir -> Test with creating directory.
        test_match_no_dir -> Test with directory does not exist.
        test_match_no_access -> Test match between sets, but no access to dir.
        test_one_match_between_sets -> Test one match between sets and is dir.
        test_no_match_between_sets -> Test no match between arguments passed.
        test_empty_argsarray -> Test with args_array is empty.
        test_empty_dirchklist -> Test with dir_chk_list is empty.

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

        self.dir_crt_list = []
        self.dir_crt_list2 = ["-d"]
        self.dir_crt_list3 = ["-g"]

    @mock.patch("arg_parser.os")
    def test_create_dir_perm(self, mock_os):

        """Function:  test_create_dir_perm

        Description:  Test with permission denied to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(
                self.args_array5, self.dir_chk_list2, self.dir_crt_list2))

    @mock.patch("arg_parser.os")
    def test_create_dir_exist(self, mock_os):

        """Function:  test_create_dir_exist

        Description:  Test with file exist to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(
                self.args_array4, self.dir_chk_list2, self.dir_crt_list2))

    def test_not_subset(self):

        """Function:  test_not_subset

        Description:  Test with dir_crt_list not subset of dir_chk_list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(
                self.args_array3, self.dir_chk_list4, self.dir_crt_list3))

    @mock.patch("arg_parser.os")
    def test_chk_good_crt_fail(self, mock_os):

        """Function:  test_chk_good_crt_fail

        Description:  Test with checking dir good, but creating dir failed.

        Arguments:

        """

        mock_os.path.isdir.side_effect = [True, True, False]
        mock_os.makedirs = raise_oserror
        mock_os.access.return_value = True

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(
                self.args_array3, self.dir_chk_list3, self.dir_crt_list3))

    @mock.patch("arg_parser.os")
    def test_match_create_dir_fail(self, mock_os):

        """Function:  test_match_create_dir_fail

        Description:  Test with failing to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(
                self.args_array2, self.dir_chk_list2, self.dir_crt_list2))

    @mock.patch("arg_parser.os")
    def test_match_create_dir(self, mock_os):

        """Function:  test_match_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.makedirs.return_value = True

        self.assertFalse(arg_parser.arg_dir_chk_crt(
            self.args_array2, self.dir_chk_list2, self.dir_crt_list2))

    @mock.patch("arg_parser.os")
    def test_match_no_dir(self, mock_os):

        """Function:  test_match_no_dir

        Description:  Test with directory does not exist.

        Arguments:

        """

        mock_os.path.isdir.return_value = False

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                       self.dir_chk_list2))

    @mock.patch("arg_parser.os")
    def test_match_no_access(self, mock_os):

        """Function:  test_match_no_access

        Description:  Test with match between sets, but no access to directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = False

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                       self.dir_chk_list2))

    @mock.patch("arg_parser.os")
    def test_one_match_between_sets(self, mock_os):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets and is directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = True

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                    self.dir_chk_list2))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                    self.dir_chk_list5))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with args_array is empty.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.dir_chk_list2))

    def test_empty_dirchklist(self):

        """Function:  test_empty_dirchklist

        Description:  Test with dir_chk_list is empty.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                    self.dir_chk_list))


if __name__ == "__main__":
    unittest.main()
