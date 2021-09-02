#!/usr/bin/python
# Classification (U)

"""Program:  arg_cond_req.py

    Description:  Unit testing of arg_cond_req in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_cond_req.py

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
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_two_args_missing
        test_one_arg_missing
        test_two_args_required
        test_one_arg_required
        test_empty_optconreqlist
        test_empty_argsarray

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-c": "config"}
        self.args_array3 = {"-c": "config", "-f": "file1"}
        self.args_array4 = {"-c": "config", "-f": "file1", "-g": True}

        self.opt_con_req_list = {}
        self.opt_con_req_list2 = {"-c": ["-f"]}
        self.opt_con_req_list3 = {"-c": ["-f", "-g"]}

    def test_two_args_missing(self):

        """Function:  test_two_args_missing

        Description:  Test with two arguments required, but missing.

        Arguments:

        """

        with gen_libs.no_std_out():
            status = arg_parser.arg_cond_req(self.args_array2,
                                             self.opt_con_req_list3)

        self.assertFalse(status)

    def test_one_arg_missing(self):

        """Function:  test_one_arg_missing

        Description:  Test with one argument required, but missing.

        Arguments:

        """

        with gen_libs.no_std_out():
            status = arg_parser.arg_cond_req(self.args_array2,
                                             self.opt_con_req_list2)

        self.assertFalse(status)

    def test_two_args_required(self):

        """Function:  test_two_args_required

        Description:  Test with two arguments required and are present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array4,
                                                self.opt_con_req_list3))

    def test_one_arg_required(self):

        """Function:  test_one_arg_required

        Description:  Test with one argument required and is present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array3,
                                                self.opt_con_req_list2))

    def test_empty_optconreqlist(self):

        """Function:  test_empty_optconreqlist

        Description:  Test with empty list for opt_con_req_list.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array2,
                                                self.opt_con_req_list))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty list for def_array.

        Arguments:

        """

        with gen_libs.no_std_out():
            status = arg_parser.arg_cond_req(self.args_array,
                                             self.opt_con_req_list2)

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
