#!/usr/bin/python
# Classification (U)

"""Program:  arg_parse2.py

    Description:  Unit testing of arg_parse2 in arg_parser.py.

    Usage:
        test/integration/arg_parser/arg_parse2.py

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

# Local
sys.path.append(os.getcwd())
import arg_parser
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
        test_optval_set
        test_optvalset_no_val
        test_optvalset_two_arg
        test_optvalset_one_arg
        test_arg_value_not_set
        test_prog_with_arg
        test_with_two_args
        test_with_one_arg
        test_argv_no_args
        test_empty_argv_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.path_file = "./merge_repo.py"
        self.argv = [self.path_file, "-c", "merge", "-d", "-M", "-f",
                     "file1", "file2"]
        self.opt_val_list = ["-c", "-d", "-f", "-g"]
        self.opt_def_dict = {"-g": "def_val"}
        self.multi_list = ["-f", "-g"]
        self.opt_val = ["-d"]

    def test_all_together(self):

        """Function:  test_all_together

        Description:  Test with all options together.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list,
                                               opt_val=self.opt_val),
                         {"-c": "merge", "-d": None, "-M": True,
                          "-f": ["file1", "file2"]})

    def test_multi_defdict_set(self):

        """Function:  test_multi_defdict_set

        Description:  Test with multi_list and opt_def_dict set.

        Arguments:

        """

        self.argv = [self.path_file, "-g"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               self.opt_def_dict,
                                               multi_val=self.multi_list),
                         {"-g": "def_val"})

    def test_multilist_two_val(self):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to two values.

        Arguments:

        """

        self.argv = [self.path_file, "-f", "file1", "file2"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"]})

    def test_multilist_one_val(self):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        self.argv = [self.path_file, "-f", "file1"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1"]})

    @unittest.skip("Error:  Need to fix arg_default and remove sys.exit call.")
    def test_multilist_def_arg(self):

        """Function:  test_multilist_def_arg

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        self.argv = [self.path_file, "-f"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         "SystemExit: Error: Arg -f missing value")

    def test_multilist_two_args(self):

        """Function:  test_multilist_two_args

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:

        """

        self.argv = [self.path_file, "-f", "file1", "file2", "-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"], "-M": True})

    def test_multilist_one_arg(self):

        """Function:  test_multilist_one_arg

        Description:  Test with multi_list set to one argument.

        Arguments:

        """

        self.argv = [self.path_file, "-f", "file1", "file2"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"]})

    def test_optvalset_arg_int(self):

        """Function:  test_optvalset_arg_int

        Description:  Test with opt_val_set set to integer value.

        Arguments:

        """

        self.argv = [self.path_file, "-c", "-1"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "-1"})

    def test_optval_set(self):

        """Function:  test_optval_set

        Description:  Test with opt_val set with no value in arg.

        Arguments:

        """

        self.argv = [self.path_file, "-c", "merge", "-d"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               opt_val=self.opt_val),
                         {"-c": "merge", "-d": None})

    @unittest.skip("Error:  Need to fix arg_default and remove sys.exit call.")
    def test_optvalset_no_val(self):

        """Function:  test_optvalset_no_val

        Description:  Test with opt_val_set set with no value in arg.

        Arguments:

        """

        self.argv = [self.path_file, "-c", "merge", "-d"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         "SystemExit: Error: Arg -d missing value")

    def test_optvalset_two_arg(self):

        """Function:  test_optvalset_two_arg

        Description:  Test with opt_val_set set to two arguments.

        Arguments:

        """

        self.argv = [self.path_file, "-c", "merge", "-d", "config"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "merge", "-d": "config"})

    def test_optvalset_one_arg(self):

        """Function:  test_optvalset_one_arg

        Description:  Test with opt_val_set set to one argument.

        Arguments:

        """

        self.argv = [self.path_file, "-c", "merge"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "merge"})

    def test_arg_value_not_set(self):

        """Function:  test_arg_value_not_set

        Description:  Test with argument with value, but not set in opt_val.

        Arguments:

        """

        self.argv = [self.path_file, "-c", "merge"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-c": True})

    def test_prog_with_arg(self):

        """Function:  test_prog_with_arg

        Description:  Test with program name with argument.

        Arguments:

        """

        self.argv = [self.path_file, "-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-M": True})

    def test_with_two_args(self):

        """Function:  test_with_two_args

        Description:  Test with two arguments, no values.

        Arguments:

        """

        self.argv = ["-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-M": True})

    def test_with_one_arg(self):

        """Function:  test_with_one_arg

        Description:  Test with one argument, no values.

        Arguments:

        """

        self.argv = ["-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-M": True})

    def test_argv_no_args(self):

        """Function:  test_argv_no_args

        Description:  Test with argv with no arguments.

        Arguments:

        """

        self.argv = [self.path_file]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {})

    def test_empty_argv_list(self):

        """Function:  test_empty_argv_list

        Description:  Test with argv as empty list.

        Arguments:

        """

        self.argv = []

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {})


if __name__ == "__main__":
    unittest.main()
