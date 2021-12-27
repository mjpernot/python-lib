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
        test_dir_exist_with_rw4
        test_dir_exist_with_rw3
        test_dir_exist_with_rw2
        test_dir_exist_with_rw
        test_dir_exist_with_w2
        test_dir_exist_with_w
        test_dir_exist_with_r2
        test_dir_exist_with_r
        test_dir_exist_with_x
        test_dir_exist_no_x
        test_dir_not_exist
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_perms_chk

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        dir1 = "/test_path/dir1"
        self.args_array = {}
        self.args_array2 = {"-d": dir1}
#        self.args_array3 = {"-d": dir1, "-g": "/test_path/dir2"}
#        self.args_array4 = {"-d": "/dir/path/dirname13"}
#        self.args_array5 = {"-d": "/dir/path/dirname17"}
        self.dir_perms_chk = {}
        self.dir_perms_chk2 = {"-d": 1}
        self.dir_perms_chk3 = {"-d": 4}
        self.dir_perms_chk4 = {"-d": 2}
        self.dir_perms_chk5 = {"-g": 1}
#        self.dir_perms_chk3 = {"-d": 1, "-g": 1}
#        self.dir_perms_chk4 = {"-d": 1, "-i": 1}

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_rw4(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw4

        Description:  Test with directory and with no read or write acess.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False, False]
        mock_octal.side_effect = ["rwx", "rwx"]

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_rw3(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw3

        Description:  Test with directory and with no write acess.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, False]
        mock_octal.side_effect = ["rwx", "rwx"]

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_rw2(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw2

        Description:  Test with directory and with no read acess.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False, True]
        mock_octal.side_effect = ["rwx", "rwx"]

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_rw(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw

        Description:  Test with directory and with read and write.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, True]
        mock_octal.side_effect = ["rwx", "rwx"]

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_w2(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_w2

        Description:  Test with directory and with no write access.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False]
        mock_octal.side_effect = ["-wx", "-wx"]

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_w(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_w

        Description:  Test with directory and with write.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True]
        mock_octal.side_effect = ["-wx", "-wx"]

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_with_x(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_x

        Description:  Test with directory and only with execute.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = True
        mock_octal.side_effect = ["--x", "--x"]

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk2))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_exist_no_x(self, mock_os, mock_octal):

        """Function:  test_dir_exist_no_x

        Description:  Test with directory and only with execute.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = False
        mock_octal.side_effect = ["---", "---"]

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk2))

    @mock.patch("arg_parser.gen_libs.octal_to_str")
    @mock.patch("arg_parser.os")
    def test_dir_not_exist(self, mock_os, mock_octal):

        """Function:  test_dir_not_exist

        Description:  Test with directory and only with execute.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.access.return_value = True
        mock_octal.side_effect = ["--x", "--x"]

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk2))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk5))

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array, self.dir_perms_chk2))

    def test_empty_dir_perms_chk(self):

        """Function:  test_empty_dir_perms_chk

        Description:  Test with dir_perms_chk is empty.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk))


if __name__ == "__main__":
    unittest.main()
