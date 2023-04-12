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
import unittest
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
        test_multiple_dirs_fail6
        test_multiple_dirs_fail5
        test_multiple_dirs_fail4
        test_multiple_dirs_fail3
        test_multiple_dirs_fail2
        test_multiple_dirs_fail
        test_multiple_dirs_access
        test_dir_perm_pass
        test_dir_perm_fail
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

        p_name = "program.py"

        self.argv = [p_name]
        self.argv2 = [p_name, "-d", "/path/dir1"]
        self.argv3 = [p_name, "-d", "/path/dir1", "-g", "/path/dir2"]
        self.opt_val = ["-d", "-g"]
        self.dir_perms_chk = {}
        self.dir_perms_chk2 = {"-d": 1}
        self.dir_perms_chk4 = {"-d": 2}
        self.dir_perms_chk5 = {"-g": 1}
        self.dir_perms_chk6 = {"-d": 4, "-g": 4}

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_dir_perms_chk_override(self, mock_chk, mock_os):

        """Function:  test_dir_perms_chk_override

        Description:  Test with passing in dir_perms_chk to override.

        Arguments:

        """

        mock_chk.side_effect = [True, True]
        mock_os.side_effect = [True, True]

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk, do_parse=True)

        self.assertTrue(
            args_array.arg_dir_chk(dir_perms_chk=self.dir_perms_chk4))

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_fail6(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_fail6

        Description:  Test with multiple directories with two failures.

        Arguments:

        """

        mock_chk.side_effect = [True, True]
        mock_os.side_effect = [False, False]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_fail5(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_fail5

        Description:  Test with multiple directories with one failure.

        Arguments:

        """

        mock_chk.side_effect = [True, True]
        mock_os.side_effect = [True, False]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_fail4(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_fail4

        Description:  Test with multiple directories with one failure.

        Arguments:

        """

        mock_chk.side_effect = [True, True]
        mock_os.side_effect = [False, True]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_fail3(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_fail3

        Description:  Test with multiple directories with two failures.

        Arguments:

        """

        mock_chk.side_effect = [False, False]
        mock_os.side_effect = [True, True]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_fail2(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_fail2

        Description:  Test with multiple directories with one failure.

        Arguments:

        """

        mock_chk.side_effect = [False, True]
        mock_os.side_effect = [True, True]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_fail(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_fail

        Description:  Test with multiple directories with one failure.

        Arguments:

        """

        mock_chk.side_effect = [True, False]
        mock_os.side_effect = [True, True]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir")
    @mock.patch("gen_libs.chk_perm")
    def test_multiple_dirs_access(self, mock_chk, mock_os):

        """Function:  test_multiple_dirs_access

        Description:  Test with multiple directories with correct permissions.

        Arguments:

        """

        mock_chk.side_effect = [True, True]
        mock_os.side_effect = [True, True]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=True))
    def test_dir_perm_pass(self):

        """Function:  test_dir_perm_pass

        Description:  Test with check permissions on directory pass.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=False))
    def test_dir_perm_fail(self):

        """Function:  test_dir_perm_fail

        Description:  Test with check permissions on directory failed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk())

    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=False))
    def test_dir_not_exist(self):

        """Function:  test_dir_not_exist

        Description:  Test with no directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk5, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_perms_chk=self.dir_perms_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_empty_dir_perms_chk(self):

        """Function:  test_empty_dir_perms_chk

        Description:  Test with dir_perms_chk is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_perms_chk=self.dir_perms_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())


if __name__ == "__main__":
    unittest.main()
