#!/usr/bin/python
# Classification (U)

"""Program:  arg_require.py

    Description:  Unit testing of arg_require in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_require.py

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
        test_two_require_one_fail -> Test with 2 required args, but 1 failure.
        test_two_require -> Test with two required arguments.
        test_one_require -> Test with one required argument.
        test_empty_argsarray -> Test with empty args_array.
        test_empty_optreqlist -> Test with empty list for opt_req_list.
        test_both_empty -> Test with both args with empty sets.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": True}
        self.args_array3 = {"-a": True, "-c": True}
        self.args_array4 = {"-a": True, "-d": True}

        self.opt_req_list = []
        self.opt_req_list2 = ["-a"]
        self.opt_req_list3 = ["-a", "-c"]

    def test_two_require_one_fail(self):

        """Function:  test_two_require_one_fail

        Description:  Test with two required arguments, but one failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_require(self.args_array4,
                                                   self.opt_req_list3))

    def test_two_require(self):

        """Function:  test_two_require

        Description:  Test with two required arguments.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_require(self.args_array3,
                                                self.opt_req_list3))

    def test_one_require(self):

        """Function:  test_one_require

        Description:  Test with one required argument.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_require(self.args_array2,
                                                self.opt_req_list2))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty args_array.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_require(self.args_array,
                                                   self.opt_req_list2))

    def test_empty_optreqlist(self):

        """Function:  test_empty_optreqlist

        Description:  Test with empty list for opt_req_list.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_require(self.args_array2,
                                                self.opt_req_list))

    def test_both_empty(self):

        """Function:  test_both_empty

        Description:  Test with both args with empty sets.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_require(self.args_array,
                                                self.opt_req_list))


if __name__ == "__main__":
    unittest.main()
