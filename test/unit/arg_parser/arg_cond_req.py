#!/usr/bin/python
# Classification (U)

"""Program:  arg_cond_req.py

    Description:  Unit testing of arg_cond_req in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_cond_req.py

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
import gen_libs
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
        test_two_args_missing -> Test with two arguments required, but missing.
        test_one_arg_missing -> Test with one argument required, but missing.
        test_two_args_required -> Test with 2 arguments required & are present.
        test_one_arg_required -> Test with 1 argument required and is present.
        test_empty_optconreqlist -> Test with empty list for opt_con_req_list.
        test_empty_arsarray -> Test with empty args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = {}
        self.args_array2 = {"-c": "config"}
        self.args_array3 = {"-c": "config", "-f": "file1"}

        self.opt_con_req_list = []
        self.opt_con_req_list2 = ["-c"]
        self.opt_con_req_list3 = ["-c", "-f"]
        self.opt_con_req_list4 = ["-c", "-f", "-m", "-d"]

    def test_two_args_missing(self):

        """Function:  test_two_args_missing

        Description:  Test with two arguments required, but missing.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array2,
                                                self.opt_con_req_list4))

    def test_one_arg_missing(self):

        """Function:  test_one_arg_missing

        Description:  Test with one argument required, but missing.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array2,
                                                self.opt_con_req_list3))

    def test_two_args_required(self):

        """Function:  test_two_args_required

        Description:  Test with two arguments required and are present.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array3,
                                                self.opt_con_req_lis3))

    def test_one_arg_required(self):

        """Function:  test_one_arg_required

        Description:  Test with one argument required and is present.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array2,
                                                self.opt_con_req_list2))

    def test_empty_optconreqlist(self):

        """Function:  test_empty_optconreqlist

        Description:  Test with empty list for opt_con_req_list.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array2,
                                                self.opt_con_req_list))

    def test_empty_arsarray(self):

        """Function:  test_empty_arsarray

        Description:  Test with empty list for def_array.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req(self.args_array,
                                                self.opt_con_req_list2))


if __name__ == "__main__":
    unittest.main()
