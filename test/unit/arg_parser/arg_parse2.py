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

        self.argv = ["./merge_repo.py", "-c", "merge", "-d", "config", "-M"]
        self.opt_val_list = ["-c", "-d"]
        self.opt_def_dict = None
        self.multi_list = []
        self.opt_val = []

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
