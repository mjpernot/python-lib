#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_dir_chk.py

    Description:  Unit testing of arg_dir_chk in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_dir_chk.py

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
import gen_class
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_dir_perms_chk_override
        test_multiple_dirs_no_access3
        test_multiple_dirs_no_access2
        test_multiple_dirs_no_access
        test_multiple_dirs_access
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

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-d", "/path/dir1"]
        self.argv3 = [
            "program.py", "-d", "/path/dir1", "-g", "/path/dir2"]
        self.opt_val = ["-d", "-g"]
        self.dir_perms_chk = {}
        self.dir_perms_chk2 = {"-d": 1}
        self.dir_perms_chk3 = {"-d": 4}
        self.dir_perms_chk4 = {"-d": 2}
        self.dir_perms_chk5 = {"-g": 1}
        self.dir_perms_chk6 = {"-d": 4, "-g": 4}

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_perms_chk_override(self, mock_os, mock_octal):

        """Function:  test_dir_perms_chk_override

        Description:  Test with passing in dir_perms_chk to override.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, True]
        mock_octal.side_effect = ["rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk)

        self.assertTrue(
            args_array.arg_dir_chk(dir_perms_chk=self.dir_perms_chk4))

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_multiple_dirs_no_access3(self, mock_os, mock_octal):

        """Function:  test_multiple_dirs_no_access3

        Description:  Test with multiple directories with both no access.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False, True, True, False, True]
        mock_octal.side_effect = ["rwx", "rwx", "rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_multiple_dirs_no_access2(self, mock_os, mock_octal):

        """Function:  test_multiple_dirs_no_access2

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, True, True, False, True]
        mock_octal.side_effect = ["rwx", "rwx", "rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_multiple_dirs_no_access(self, mock_os, mock_octal):

        """Function:  test_multiple_dirs_no_access

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False, True, True, True, True]
        mock_octal.side_effect = ["rwx", "rwx", "rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_multiple_dirs_access(self, mock_os, mock_octal):

        """Function:  test_multiple_dirs_access

        Description:  Test with multiple directories with access.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, True, True, True, True]
        mock_octal.side_effect = ["rwx", "rwx", "rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6)

        self.assertTrue(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_rw4(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw4

        Description:  Test with directory and with no read or write acess.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False, False]
        mock_octal.side_effect = ["rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_rw3(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw3

        Description:  Test with directory and with no write acess.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, False]
        mock_octal.side_effect = ["rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_rw2(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw2

        Description:  Test with directory and with no read acess.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False, True]
        mock_octal.side_effect = ["rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_rw(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_rw

        Description:  Test with directory and with read and write.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True, True]
        mock_octal.side_effect = ["rwx", "rwx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4)

        self.assertTrue(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_w2(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_w2

        Description:  Test with directory and with no write access.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, False]
        mock_octal.side_effect = ["-wx", "-wx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk3)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_w(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_w

        Description:  Test with directory and with write.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.side_effect = [True, True]
        mock_octal.side_effect = ["-wx", "-wx"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4)

        self.assertTrue(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_with_x(self, mock_os, mock_octal):

        """Function:  test_dir_exist_with_x

        Description:  Test with directory and only with execute.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = True
        mock_octal.side_effect = ["--x", "--x"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2)

        self.assertTrue(args_array.arg_dir_chk())

    @mock.patch("gen_class.gen_libs.octal_to_str")
    @mock.patch("gen_class.os")
    def test_dir_exist_no_x(self, mock_os, mock_octal):

        """Function:  test_dir_exist_no_x

        Description:  Test with no execute on directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = False
        mock_octal.side_effect = ["---", "---"]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os")
    def test_dir_not_exist(self, mock_os):

        """Function:  test_dir_not_exist

        Description:  Test with no directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.access.return_value = True

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk5)

        self.assertTrue(args_array.arg_dir_chk())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_perms_chk=self.dir_perms_chk2)

        self.assertTrue(args_array.arg_dir_chk())

    def test_empty_dir_perms_chk(self):

        """Function:  test_empty_dir_perms_chk

        Description:  Test with dir_perms_chk is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_perms_chk=self.dir_perms_chk)

        self.assertTrue(args_array.arg_dir_chk())


if __name__ == "__main__":
    unittest.main()
