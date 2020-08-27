#!/usr/bin/python
# Classification (U)

"""Program:  arg_add_def.py

    Description:  Unit testing of arg_add_def in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_add_def.py

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
        setUp -> Unit testing initilization.
        test_optreqlist_two_args -> Test adding two args from opt_req_list.
        test_optreqlist_zero_arg -> Test adding zero args from opt_req_list.
        test_optreqlist_one_arg -> Test with adding one arg from opt_req_list.
        test_argsarray_only -> Test with args_array passed only.
        test_defarray_two_args -> Test with adding two args from def_array.
        test_defarray_one_arg -> Test with adding one arg from def_array.
        test_empty_defarray -> Test with empty list for def_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-f": "file1"}

        self.def_array = {}
        self.def_array2 = {"-n": "1"}
        self.def_array3 = {"-n": "1", "-i": "sysmon"}
        self.def_array4 = {"-n": "1", "-i": "sysmon", "-g": "no"}

        self.opt_req_list = []
        self.opt_req_list2 = ["-m"]
        self.opt_req_list3 = ["-n"]
        self.opt_req_list4 = ["-n", "-i"]

    def test_optreqlist_two_args(self):

        """Function:  test_optreqlist_two_args

        Description:  Test with adding two args from opt_req_list.

        Arguments:

        """

        test_array = dict(self.args_array)
        test_array["-n"] = "1"
        test_array["-i"] = "sysmon"

        self.assertEqual(arg_parser.arg_add_def(self.args_array,
                                                self.def_array4,
                                                self.opt_req_list4),
                         test_array)

    def test_optreqlist_zero_arg(self):

        """Function:  test_optreqlist_zero_arg

        Description:  Test with adding zero args from opt_req_list.

        Arguments:

        """

        test_array = dict(self.args_array)

        self.assertEqual(arg_parser.arg_add_def(self.args_array,
                                                self.def_array3,
                                                self.opt_req_list2),
                         test_array)

    def test_optreqlist_one_arg(self):

        """Function:  test_optreqlist_one_arg

        Description:  Test with adding one arg from opt_req_list.

        Arguments:

        """

        test_array = dict(self.args_array)
        test_array["-n"] = "1"

        self.assertEqual(arg_parser.arg_add_def(self.args_array,
                                                self.def_array3,
                                                self.opt_req_list3),
                         test_array)

    def test_argsarray_only(self):

        """Function:  test_argsarray_only

        Description:  Test with args_array passed only.

        Arguments:

        """

        test_array = dict(self.args_array)

        self.assertEqual(arg_parser.arg_add_def(self.args_array), test_array)

    def test_defarray_two_args(self):

        """Function:  test_defarray_two_args

        Description:  Test with adding two args from def_array.

        Arguments:

        """

        test_array = dict(self.args_array)
        test_array["-n"] = "1"
        test_array["-i"] = "sysmon"

        self.assertEqual(arg_parser.arg_add_def(self.args_array,
                                                self.def_array3,
                                                self.opt_req_list),
                         test_array)

    def test_defarray_one_arg(self):

        """Function:  test_defarray_one_arg

        Description:  Test with adding one arg from def_array.

        Arguments:

        """

        test_array = dict(self.args_array)
        test_array["-n"] = "1"

        self.assertEqual(arg_parser.arg_add_def(self.args_array,
                                                self.def_array2,
                                                self.opt_req_list),
                         test_array)

    def test_empty_defarray(self):

        """Function:  test_empty_defarray

        Description:  Test with empty list for def_array.

        Arguments:

        """

        test_array = dict(self.args_array)

        self.assertEqual(arg_parser.arg_add_def(self.args_array,
                                                self.def_array,
                                                self.opt_req_list),
                         test_array)


if __name__ == "__main__":
    unittest.main()
