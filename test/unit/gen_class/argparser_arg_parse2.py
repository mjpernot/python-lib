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
        test_all_together
        test_multi_defdict_set
        test_multilist_two_val
        test_multilist_one_val
        test_multilist_def_arg
        test_multilist_two_args
        test_multilist_one_arg
        test_optvalset_arg_int

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

#        self.path_file = "./merge_repo.py"
#        self.argv = [self.path_file, "-c", "merge", "-d", "-M", "-f",
#                     "file1", "file2"]
#        self.opt_val_list = ["-c", "-d", "-f", "-g"]
#        self.opt_def_dict = {"-g": "def_val"}
#        self.multi_list = ["-f", "-g"]
#        self.opt_val = ["-d"]

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-M"]
        self.argv3 = ["program.py", "-M", "-a"]
        self.argv4 = ["program.py", "-M", "merge"]
        self.argv5 = ["program.py", "-c", "cfg", "-d", "/path"]
        self.argv6 = ["program.py", "-c", "cfg", "-d"]
        self.argv7 = [
            "program.py", "-c", "cfg", "-d", "/path", "-M", "-f",
            "file1", "file2"]

        self.opt_val = ["-c", "-d", "-f", "-g"]
        self.opt_val2 = ["-M", "-a"]
        self.opt_def = {"-g": "def_val"}
        self.multi_val = ["-f", "-g"]
        self.opt_val_bin = ["-d"]

        self.results = {"-M": True}
        self.results2 = {"-M": True, "-a": True}
        self.results3 = {"-M": "merge"}
        self.results4 = {"-c": "cfg", "-d": "/path"}
        self.results5 = {"-c": "cfg"}
        self.results6 = {"-c": "cfg", "-d": None}

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_all_together(self, mock_int):

        """Function:  test_all_together

        Description:  Test with all options together.

        Arguments:

        """

        mock_int.return_value = False

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list,
                                               opt_val=self.opt_val),
                         {"-c": "merge", "-d": None, "-M": True,
                          "-f": ["file1", "file2"]})

    @mock.patch("arg_parser.arg_default")
    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multi_defdict_set(self, mock_int, mock_def):

        """Function:  test_multi_defdict_set

        Description:  Test with multi_list and opt_def_dict set.

        Arguments:

        """

        mock_int.return_value = False
        mock_def.return_value = {"-g": "def_val"}

        self.argv = [self.path_file, "-g"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               self.opt_def_dict,
                                               multi_val=self.multi_list),
                         {"-g": "def_val"})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_two_val(self, mock_int):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to two values.

        Arguments:

        """

        mock_int.return_value = False

        self.argv = [self.path_file, "-f", "file1", "file2"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"]})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_one_val(self, mock_int):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        mock_int.return_value = False

        self.argv = [self.path_file, "-f", "file1"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1"]})

    @mock.patch("arg_parser.arg_default")
    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_def_arg(self, mock_int, mock_def):

        """Function:  test_multilist_def_arg

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        mock_int.return_value = False
        mock_def.return_value = "SystemExit: Error: Arg -f missing value"

        self.argv = [self.path_file, "-f"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         "SystemExit: Error: Arg -f missing value")

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_two_args(self, mock_int):

        """Function:  test_multilist_two_args

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:

        """

        mock_int.return_value = False

        self.argv = [self.path_file, "-f", "file1", "file2", "-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"], "-M": True})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_one_arg(self, mock_int):

        """Function:  test_multilist_one_arg

        Description:  Test with multi_list set to one argument.

        Arguments:

        """

        mock_int.return_value = False

        self.argv = [self.path_file, "-f", "file1", "file2"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"]})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_optvalset_arg_int(self, mock_int):

        """Function:  test_optvalset_arg_int

        Description:  Test with opt_val_set set to integer value.

        Arguments:

        """

        mock_int.return_value = True

        self.argv = [self.path_file, "-c", "-1"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "-1"})

### STOPPED HERE - Failing for some reason.  See run for error codes.
    @mock.patch("arg_parser.gen_libs.chk_int")
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

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_opt_def_no_val2(self, mock_int):

        """Function:  test_opt_def_no_val2

        Description:  Test with opt_def but no value.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv6, opt_val=self.opt_val)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_parse2())

    @mock.patch("arg_parser.gen_libs.chk_int")
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
