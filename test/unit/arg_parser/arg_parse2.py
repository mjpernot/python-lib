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
        self.opt_val_list = []
        self.opt_def_dict = None
        self.multi_list = []
        self.opt_val = []

    def test_with_one_arg(self):

        """Function:  test_with_one_arg

        Description:  Test with one argument, no values.

        Arguments:
            None

        """

        self.argv = ["-M"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {"-M": True})

    def test_argv_no_args(self):

        """Function:  test_argv_no_args

        Description:  Test with argv with no arguments.

        Arguments:
            None

        """

        self.argv = ["./merge_repo.py"]

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {})

    def test_empty_argv_list(self):

        """Function:  test_empty_argv_list

        Description:  Test with argv as empty list.

        Arguments:
            None

        """

        self.argv = []

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list),
                         {})



if __name__ == "__main__":
    unittest.main()
