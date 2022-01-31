#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_dir_crt.py

    Description:  Unit testing of arg_dir_crt in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_dir_crt.py

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
        test_multi_chk_perm_fail3
        test_multi_chk_perm_fail2
        test_multi_chk_perm_fail
        test_multi_chk_perm_success
        test_dir_perms_crt_override
        test_chk_perm_fail
        test_chk_perm_success
        test_dir_not_exist2
        test_dir_not_exist
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_perms_crt

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
        self.dir_perms_crt = {}
        self.dir_perms_crt2 = {"-d": 1}
        self.dir_perms_crt4 = {"-d": 2}
        self.dir_perms_crt5 = {"-g": 1}
        self.dir_perms_crt6 = {"-d": 4, "-g": 4}
        self.dir_perms_crt7 = {"-d": 7}

    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    @mock.patch("gen_libs.chk_perm")
    def test_multi_chk_perm_fail3(self, mock_chk):

        """Function:  test_multi_chk_perm_fail3

        Description:  Test with multiple check permission on directories with
            failure.

        Arguments:

        """

        mock_chk.side_effect = [False, False]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertFalse(args_array.arg_dir_crt())

    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    @mock.patch("gen_libs.chk_perm")
    def test_multi_chk_perm_fail2(self, mock_chk):

        """Function:  test_multi_chk_perm_fail2

        Description:  Test with multiple check permission on directories with
            failure.

        Arguments:

        """

        mock_chk.side_effect = [False, True]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertFalse(args_array.arg_dir_crt())

    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    @mock.patch("gen_libs.chk_perm")
    def test_multi_chk_perm_fail(self, mock_chk):

        """Function:  test_multi_chk_perm_fail

        Description:  Test with multiple check permission on directories with
            failure.

        Arguments:

        """

        mock_chk.side_effect = [True, False]

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertFalse(args_array.arg_dir_crt())

    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=True))
    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    def test_multi_chk_perm_success(self):

        """Function:  test_multi_chk_perm_success

        Description:  Test with multiple successful check permission on
            directories.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=True))
    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    def test_dir_perms_crt_override(self):

        """Function:  test_dir_perms_crt_override

        Description:  Test with passing in dir_perms_crt to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt, do_parse=True)

        self.assertTrue(
            args_array.arg_dir_crt(dir_perms_crt=self.dir_perms_crt4))

    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=False))
    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    def test_chk_perm_fail(self):

        """Function:  test_chk_perm_fail

        Description:  Test with failed check permission on directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt7, do_parse=True)

        self.assertFalse(args_array.arg_dir_crt())

    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=True))
    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=True))
    def test_chk_perm_success(self):

        """Function:  test_chk_perm_success

        Description:  Test with successful check permission on directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt7, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    @mock.patch("gen_libs.make_dir", mock.Mock(return_value=False))
    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=False))
    def test_dir_not_exist2(self):

        """Function:  test_dir_not_exist2

        Description:  Test with no directory exists, but fails to create
            directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt7, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    @mock.patch("gen_libs.chk_perm", mock.Mock(return_value=True))
    @mock.patch("gen_libs.make_dir", mock.Mock(return_value=True))
    @mock.patch("gen_class.os.path.isdir", mock.Mock(return_value=False))
    def test_dir_not_exist(self):

        """Function:  test_dir_not_exist

        Description:  Test with no directory exists and create directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt7, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt5, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_perms_crt=self.dir_perms_crt2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_empty_dir_perms_crt(self):

        """Function:  test_empty_dir_perms_crt

        Description:  Test with dir_perms_crt is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_perms_crt=self.dir_perms_crt,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())


if __name__ == "__main__":
    unittest.main()
