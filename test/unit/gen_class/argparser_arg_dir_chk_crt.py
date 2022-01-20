#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_dir_chk_crt.py

    Description:  Unit testing of arg_dir_chk_crt in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_dir_chk_crt.py

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
        test_create_dir_perm
        test_create_dir_exist
        test_not_subset
        test_chk_good_crt_fail
        test_match_create_dir_fail
        test_match_create_dir
        test_match_no_dir
        test_match_no_access
        test_one_match_between_sets
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_chk

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
        self.argv4 = ["program.py", "-d", "/path/dir13"]
        self.argv5 = ["program.py", "-d", "/path/dir17"]
        self.opt_val = ["-d", "-g"]

        self.dir_chk = []
        self.dir_chk2 = ["-d"]
        self.dir_chk3 = ["-d", "-g"]
        self.dir_chk4 = ["-d", "-i"]
        self.dir_chk5 = ["-g"]

        self.dir_crt = []
        self.dir_crt2 = ["-d"]
        self.dir_crt3 = ["-g"]

    @mock.patch("gen_libs.make_dir")
    @mock.patch("gen_class.os")
    def test_create_dir_perm(self, mock_os, mock_dir):

        """Function:  test_create_dir_perm

        Description:  Test with permission denied to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_dir.return_value = False

        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            dir_crt=self.dir_crt2, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk_crt())

    @mock.patch("gen_libs.make_dir")
    @mock.patch("gen_class.os")
    def test_create_dir_exist(self, mock_os, mock_dir):

        """Function:  test_create_dir_exist

        Description:  Test with file exist to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_dir.return_value = False

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            dir_crt=self.dir_crt2, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk_crt())

    def test_not_subset(self):

        """Function:  test_not_subset

        Description:  Test with dir_crt_list not subset of dir_chk_list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, dir_chk=self.dir_chk4,
            dir_crt=self.dir_crt3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk_crt())

    @mock.patch("gen_libs.make_dir")
    @mock.patch("gen_class.os")
    def test_chk_good_crt_fail(self, mock_os, mock_dir):

        """Function:  test_chk_good_crt_fail

        Description:  Test with checking dir good, but creating dir failed.

        Arguments:

        """

        mock_os.path.isdir.side_effect = [True, True, False]
        mock_os.access.return_value = True
        mock_dir.return_value = False

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, dir_chk=self.dir_chk3,
            dir_crt=self.dir_crt3, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk_crt())

    @mock.patch("gen_libs.make_dir")
    @mock.patch("gen_class.os")
    def test_match_create_dir_fail(self, mock_os, mock_dir):

        """Function:  test_match_create_dir_fail

        Description:  Test with failing to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_dir.return_value = False

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            dir_crt=self.dir_crt2, do_parse=True)

        self.assertFalse(args_array.arg_dir_chk_crt())

    @mock.patch("gen_libs.make_dir")
    @mock.patch("gen_class.os")
    def test_match_create_dir(self, mock_os, mock_dir):

        """Function:  test_match_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_dir.return_value = True

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            dir_crt=self.dir_crt2, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    @mock.patch("gen_class.os")
    def test_match_no_dir(self, mock_os):

        """Function:  test_match_no_dir

        Description:  Test with directory does not exist.

        Arguments:

        """

        mock_os.path.isdir.return_value = False

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk_crt())

    @mock.patch("gen_class.os")
    def test_match_no_access(self, mock_os):

        """Function:  test_match_no_access

        Description:  Test with match between sets, but no access to directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = False

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk_crt())

    @mock.patch("gen_class.os")
    def test_one_match_between_sets(self, mock_os):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets and is directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = True

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk5,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_empty_dir_chk(self):

        """Function:  test_empty_dir_chk

        Description:  Test with dir_chk is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())


if __name__ == "__main__":
    unittest.main()
