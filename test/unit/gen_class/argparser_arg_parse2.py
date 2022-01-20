#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_parse2.py

    Description:  Unit testing of arg_parse2 in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_parse2.py

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
        test_opt_val_bin_override2
        test_opt_val_bin_override
        test_multi_val_override2
        test_multi_val_override
        test_opt_def_override2
        test_opt_def_override
        test_opt_val_override2
        test_opt_val_override
        test_all_together
        test_multiple_opt_def
        test_multilist_multiple_val
        test_multi_val_one_val
        test_multi_val_no_val
        test_multi_val_def_arg
        test_multi_val_two_args
        test_multi_val_one_arg
        test_opt_val_arg_int
        test_opt_val_bin
        test_opt_def_no_val2
        test_opt_def_no_val
        test_opt_val_two_arg
        test_opt_val_one_arg
        test_arg_value_not_set
        test_prog_with_arg
        test_with_two_args
        test_with_one_arg
        test_argv_no_args
        test_empty_argv_list2
        test_empty_argv_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-M"]
        self.argv3 = ["program.py", "-M", "-a"]
        self.argv4 = ["program.py", "-M", "merge"]
        self.argv5 = ["program.py", "-c", "cfg", "-d", "/path"]
        self.argv6 = ["program.py", "-c", "cfg", "-d"]
        self.argv7 = ["program.py", "-c", "-1"]
        self.argv8 = ["program.py", "-f", "file1", "file2"]
        self.argv9 = [
            "program.py", "-f", "file1", "file2", "-g", "file3", "file4"]
        self.argv10 = ["program.py", "-f"]
        self.argv11 = ["program.py", "-f", "file5"]
        self.argv12 = ["program.py", "-f", "file1", "file2", "file3"]
        self.argv13 = ["program.py", "-f", "-g"]
        self.argv14 = [
            "program.py", "-c", "cfg", "-d", "/path", "-M", "-f",
            "file1", "file2"]

        self.opt_val = ["-c", "-d", "-f", "-g"]
        self.opt_val2 = ["-M", "-a"]
        self.opt_def = {"-g": ["def_val"], "-f": ["file1", "file2"]}
        self.opt_def2 = {"-f": ["file1"]}
        self.multi_val = ["-f", "-g"]
        self.multi_val2 = ["-g"]
        self.opt_val_bin = ["-d"]
        self.opt_val_bin2 = ["-M", "-a"]

        self.results = {"-M": True}
        self.results2 = {"-M": True, "-a": True}
        self.results3 = {"-M": "merge"}
        self.results4 = {"-c": "cfg", "-d": "/path"}
        self.results5 = {"-c": "cfg"}
        self.results6 = {"-c": "cfg", "-d": None}
        self.results7 = {"-c": "-1"}
        self.results8 = {"-f": ["file1", "file2"]}
        self.results9 = {"-f": ["file1", "file2"], "-g": ["file3", "file4"]}
        self.results10 = {"-f": ["file1"]}
        self.results11 = {"-f": ["file5"]}
        self.results12 = {"-f": ["file1", "file2", "file3"]}
        self.results13 = {"-g": ["def_val"], "-f": ["file1", "file2"]}
        self.results14 = {"-c": "cfg", "-d": "/path", "-M": True,
                          "-f": ["file1", "file2"]}
        self.results15 = {"-f": "file5"}
        self.results16 = {"-M": None, "-a": None}

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_val_bin_override2(self, mock_int):

        """Function:  test_opt_val_bin_override2

        Description:  Test with opt_val_bin passed in to override.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv3, opt_val_bin=self.opt_val_bin)

        self.assertTrue(args_array.arg_parse2(opt_val_bin=self.opt_val_bin2))

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_val_bin_override(self, mock_int):

        """Function:  test_opt_val_bin_override

        Description:  Test with opt_val_bin passed in to override.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv3, opt_val_bin=self.opt_val_bin)
        args_array.arg_parse2(opt_val_bin=self.opt_val_bin2)

        self.assertEqual(args_array.args_array, self.results16)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_override2(self, mock_int):

        """Function:  test_multi_val_override2

        Description:  Test with multi_val passed in to override.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv11, opt_val=self.opt_val, multi_val=self.multi_val)

        self.assertTrue(args_array.arg_parse2(multi_val=self.multi_val2))

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_override(self, mock_int):

        """Function:  test_multi_val_override

        Description:  Test with multi_val passed in to override.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv11, opt_val=self.opt_val, multi_val=self.multi_val)
        args_array.arg_parse2(multi_val=self.multi_val2)

        self.assertEqual(args_array.args_array, self.results15)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_def_override2(self, mock_int):

        """Function:  test_opt_def_override2

        Description:  Test with opt_def passed in to override.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv10, opt_val=self.opt_val, multi_val=self.multi_val,
            opt_def=self.opt_def2)

        self.assertTrue(args_array.arg_parse2(opt_def=self.opt_def))

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_def_override(self, mock_int):

        """Function:  test_opt_def_override

        Description:  Test with opt_def passed in to override.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv10, opt_val=self.opt_val, multi_val=self.multi_val,
            opt_def=self.opt_def2)
        args_array.arg_parse2(opt_def=self.opt_def)

        self.assertEqual(args_array.args_array, self.results8)

    def test_opt_val_override2(self):

        """Function:  test_opt_val_override2

        Description:  Test with opt_val passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, opt_val=self.opt_val2)

        self.assertTrue(args_array.arg_parse2(opt_val=self.opt_val))

    def test_opt_val_override(self):

        """Function:  test_opt_val_override

        Description:  Test with opt_val passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, opt_val=self.opt_val2)
        args_array.arg_parse2(opt_val=self.opt_val)

        self.assertEqual(args_array.args_array, self.results)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_all_together(self, mock_int):

        """Function:  test_all_together

        Description:  Test with all options together.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv14, opt_val=self.opt_val, multi_val=self.multi_val,
            opt_def=self.opt_def, do_parse=True)

        self.assertEqual(args_array.args_array, self.results14)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multiple_opt_def(self, mock_int):

        """Function:  test_multiple_opt_def

        Description:  Test with multiple default values with multi_val.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv13, opt_val=self.opt_val, multi_val=self.multi_val,
            opt_def=self.opt_def, do_parse=True)

        self.assertEqual(args_array.args_array, self.results13)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multilist_multiple_val(self, mock_int):

        """Function:  test_multilist_multiple_val

        Description:  Test with multi_list set to multiple values.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv12, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        self.assertEqual(args_array.args_array, self.results12)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_one_val(self, mock_int):

        """Function:  test_multi_val_one_val

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv11, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        self.assertEqual(args_array.args_array, self.results11)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_no_val(self, mock_int):

        """Function:  test_multi_val_no_val

        Description:  Test with multi_list and setting one of them using
            default values.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv10, opt_val=self.opt_val, multi_val=self.multi_val)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_parse2())

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_def_arg(self, mock_int):

        """Function:  test_multi_val_def_arg

        Description:  Test with multi_list and setting one of them using
            default values.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv10, opt_val=self.opt_val, multi_val=self.multi_val,
            opt_def=self.opt_def2, do_parse=True)

        self.assertEqual(args_array.args_array, self.results10)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_two_args(self, mock_int):

        """Function:  test_multi_val_two_args

        Description:  Test with multi_val set to two arguments with multiple
            values.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv9, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        self.assertEqual(args_array.args_array, self.results9)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_multi_val_one_arg(self, mock_int):

        """Function:  test_multi_val_one_arg

        Description:  Test with multi_val set to one argument.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv8, opt_val=self.opt_val, multi_val=self.multi_val,
            do_parse=True)

        self.assertEqual(args_array.args_array, self.results8)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_val_arg_int(self, mock_int):

        """Function:  test_opt_val_arg_int

        Description:  Test with opt_val_set set to integer value.

        Arguments:

        """

        mock_int.return_value = True

        args_array = gen_class.ArgParser(
            self.argv7, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.args_array, self.results7)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_val_bin(self, mock_int):

        """Function:  test_opt_val_bin

        Description:  Test with opt_val_bin set with no value passed in for the
            argument.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_val_bin=self.opt_val_bin,
            do_parse=True)

        self.assertEqual(args_array.args_array, self.results6)

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_def_no_val2(self, mock_int):

        """Function:  test_opt_def_no_val2

        Description:  Test with opt_def but no value.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv6, opt_val=self.opt_val)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_parse2())

    @mock.patch("gen_class.gen_libs.chk_int")
    def test_opt_def_no_val(self, mock_int):

        """Function:  test_opt_def_no_val

        Description:  Test with opt_def but no value.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv6, opt_val=self.opt_val)

        with gen_libs.no_std_out():
            args_array.arg_parse2()

        self.assertEqual(args_array.args_array, self.results5)

    def test_opt_val_two_arg(self):

        """Function:  test_opt_val_two_arg

        Description:  Test with opt_val set to two arguments.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.args_array, self.results4)

    def test_opt_val_one_arg(self):

        """Function:  test_opt_val_one_arg

        Description:  Test with opt_val set to one argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val2, do_parse=True)

        self.assertEqual(args_array.args_array, self.results3)

    def test_arg_value_not_set(self):

        """Function:  test_arg_value_not_set

        Description:  Test with argument with value, but not set in opt_val.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv4, do_parse=True)

        self.assertEqual(args_array.args_array, self.results)

    def test_prog_with_arg(self):

        """Function:  test_prog_with_arg

        Description:  Test with program name with argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, do_parse=True)

        self.assertEqual(args_array.args_array, self.results)

    def test_with_two_args(self):

        """Function:  test_with_two_args

        Description:  Test with two arguments, no values.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, do_parse=True)

        self.assertEqual(args_array.args_array, self.results2)

    def test_with_one_arg(self):

        """Function:  test_with_one_arg

        Description:  Test with one argument, no values.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, do_parse=True)

        self.assertEqual(args_array.args_array, self.results)

    def test_argv_no_args(self):

        """Function:  test_argv_no_args

        Description:  Test with argv with no arguments.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv, do_parse=True)

        self.assertEqual(args_array.args_array, {})

    def test_empty_argv_list2(self):

        """Function:  test_empty_argv_list2

        Description:  Test with argv as empty list.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv)
        args_array.argv = []

        self.assertTrue(args_array.arg_parse2())

    def test_empty_argv_list(self):

        """Function:  test_empty_argv_list

        Description:  Test with argv as empty list.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv)
        args_array.argv = []
        args_array.arg_parse2()

        self.assertEqual(args_array.args_array, {})


if __name__ == "__main__":
    unittest.main()
