#!/usr/bin/python
# Classification (U)

"""Program:  arg_parse2.py

    Description:  Unit testing of arg_parse2 in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_parse2.py

    Arguments:
        None

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
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_all_together -> Test with all options together.
        test_multi_defdict_set -> Test with multi_list and opt_def_dict set.
        test_multilist_two_val -> Test with multi_list set to two values.
        test_multilist_one_val -> Test with multi_list set to one value.
        test_multilist_def_arg -> Test with multi_list set to 1 arg using def.
        test_multilist_two_args -> Test multi_list set to 1 arg & 1 other arg.
        test_multilist_one_arg -> Test with multi_list set to one argument.
        test_optvalset_arg_int -> Test opt_val_set set to integer value.
        test_optval_set -> Test with opt_val set with no value in arg.
        test_optvalset_no_val -> Test opt_val_set set with no value in arg.
        test_optvalset_two_arg -> Test with opt_val_set set to two arguments.
        test_optvalset_one_arg -> Test with opt_val_set set to one argument.
        test_arg_value_not_set -> Test argument value, but not set in opt_val.
        test_prog_with_arg -> Test with program name with argument.
        test_with_two_args -> Test with two arguments, no values.
        test_with_one_arg -> Test with one argument, no values.
        test_argv_no_args -> Test with argv with no arguments.
        test_empty_argv_list -> Test with argv as empty list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py", "-c", "merge", "-d", "-M", "-f",
                     "file1", "file2"]
        self.opt_val_list = ["-c", "-d", "-f", "-g"]
        self.opt_def_dict = {"-g": "def_val"}
        self.multi_list = ["-f", "-g"]
        self.opt_val = ["-d"]

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_all_together(self, mock_int):

        """Function:  test_all_together

        Description:  Test with all options together.

        Arguments:
            None

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
            None

        """

        mock_int.return_value = False
        mock_def.return_value = {"-g": "def_val"}

        self.argv = ["./merge_repo.py", "-g"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               self.opt_def_dict,
                                               multi_val=self.multi_list),
                         {"-g": "def_val"})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_two_val(self, mock_int):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to two values.

        Arguments:
            None

        """

        mock_int.return_value = False

        self.argv = ["./merge_repo.py", "-f", "file1", "file2"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"]})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_one_val(self, mock_int):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to one value.

        Arguments:
            None

        """

        mock_int.return_value = False

        self.argv = ["./merge_repo.py", "-f", "file1"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1"]})

    @mock.patch("arg_parser.arg_default")
    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_def_arg(self, mock_int, mock_def):

        """Function:  test_multilist_def_arg

        Description:  Test with multi_list set to one arg using default.

        Arguments:
            None

        """

        mock_int.return_value = False
        mock_def.return_value = "SystemExit: Error: Arg -f missing value"

        self.argv = ["./merge_repo.py", "-f"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         "SystemExit: Error: Arg -f missing value")

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_two_args(self, mock_int):

        """Function:  test_multilist_two_args

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:
            None

        """

        mock_int.return_value = False

        self.argv = ["./merge_repo.py", "-f", "file1", "file2", "-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"], "-M": True})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_one_arg(self, mock_int):

        """Function:  test_multilist_one_arg

        Description:  Test with multi_list set to one argument.

        Arguments:
            None

        """

        mock_int.return_value = False

        self.argv = ["./merge_repo.py", "-f", "file1", "file2"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               multi_val=self.multi_list),
                         {"-f": ["file1", "file2"]})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_optvalset_arg_int(self, mock_int):

        """Function:  test_optvalset_arg_int

        Description:  Test with opt_val_set set to integer value.

        Arguments:
            None

        """

        mock_int.return_value = True

        self.argv = ["./merge_repo.py", "-c", "-1"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "-1"})

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_optval_set(self, mock_int):

        """Function:  test_optval_set

        Description:  Test with opt_val set with no value in arg.

        Arguments:
            None

        """

        mock_int.return_value = False

        self.argv = ["./merge_repo.py", "-c", "merge", "-d"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list,
                                               opt_val=self.opt_val),
                         {"-c": "merge", "-d": None})

    @mock.patch("arg_parser.gen_libs.chk_int")
    @mock.patch("arg_parser.arg_default")
    def test_optvalset_no_val(self, mock_def, mock_int):

        """Function:  test_optvalset_no_val

        Description:  Test with opt_val_set set with no value in arg.

        Arguments:
            None

        """

        mock_def.return_value = "SystemExit: Error: Arg -d missing value"
        mock_int.return_value = False

        self.argv = ["./merge_repo.py", "-c", "merge", "-d"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         "SystemExit: Error: Arg -d missing value")

    def test_optvalset_two_arg(self):

        """Function:  test_optvalset_two_arg

        Description:  Test with opt_val_set set to two arguments.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py", "-c", "merge", "-d", "config"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "merge", "-d": "config"})

    def test_optvalset_one_arg(self):

        """Function:  test_optvalset_one_arg

        Description:  Test with opt_val_set set to one argument.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py", "-c", "merge"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-c": "merge"})

    def test_arg_value_not_set(self):

        """Function:  test_arg_value_not_set

        Description:  Test with argument with value, but not set in opt_val.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py", "-c", "merge"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-c": True})

    def test_prog_with_arg(self):

        """Function:  test_prog_with_arg

        Description:  Test with program name with argument.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py", "-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-M": True})

    def test_with_two_args(self):

        """Function:  test_with_two_args

        Description:  Test with two arguments, no values.

        Arguments:
            None

        """

        self.argv = ["-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-M": True})

    def test_with_one_arg(self):

        """Function:  test_with_one_arg

        Description:  Test with one argument, no values.

        Arguments:
            None

        """

        self.argv = ["-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {"-M": True})

    def test_argv_no_args(self):

        """Function:  test_argv_no_args

        Description:  Test with argv with no arguments.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {})

    def test_empty_argv_list(self):

        """Function:  test_empty_argv_list

        Description:  Test with argv as empty list.

        Arguments:
            None

        """

        self.argv = []

        self.assertEqual(arg_parser.arg_parse2(self.argv, []), {})


if __name__ == "__main__":
    unittest.main()
