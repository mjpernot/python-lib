#!/usr/bin/python
# Classification (U)

"""Program:  arg_req_xor.py

    Description:  Unit testing of arg_req_xor in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_req_xor.py

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
        setUp -> Unit testing initilization.
        test_two_match_fail -> Test with one match and is failure.
        test_one_match_success -> Test with one match and is successful.
        test_empty_optxorlist -> Test with empty dict for opt_xor_list.
        test_empty_argsarray -> Test with empty dictionary for args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": True}
        self.args_array3 = {"-a": True, "-b": True}

        self.opt_xor_list = {}
        self.opt_xor_list2 = {"-a": "-b"}

    def test_two_match_fail(self):

        """Function:  test_two_match_fail

        Description:  Test with two matches and is failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_req_xor(self.args_array3,
                                                    self.opt_xor_list2))

    def test_one_match_success(self):

        """Function:  test_one_match_success

        Description:  Test with one match and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_xor(self.args_array2,
                                               self.opt_xor_list2))

    def test_empty_optxorlist(self):

        """Function:  test_empty_optxorlist

        Description:  Test with empty dictionary for opt_xor_list.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_xor(self.args_array2,
                                               self.opt_xor_list))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_req_xor(self.args_array,
                                                    self.opt_xor_list2))


if __name__ == "__main__":
    unittest.main()
