#!/usr/bin/python
# Classification (U)

"""Program:  arg_xor_dict.py

    Description:  Unit testing of arg_xor_dict in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_xor_dict.py

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
        test_multiple_miss2 -> Test with multiple key/list present.
        test_multiple_miss -> Test with multiple keys with one not present.
        test_multiple_mix -> Test with multiple key/list present.
        test_multiple_lists -> Test with multiple lists present.
        test_multiple_keys -> Test with multiple keys present.
        test_both_present -> Test with both key and list options present.
        test_list_only -> Test with list option present.
        test_key_only -> Test with key option present.
        test_empty_argsarray -> Test with empty args_array.
        test_empty_optxordict -> Test with empty list for opt_req_list.
        test_both_empty -> Test with both args with empty sets.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": True}
        self.args_array3 = {"-b": True}
        self.args_array4 = {"-a": True, "-b": True}
        self.args_array5 = {"-a": True, "-d": True}
        self.args_array6 = {"-c": True, "-e": True}
        self.args_array7 = {"-d": True, "-e": True}
        self.args_array8 = {"-a": True, "-e": True}

        self.opt_xor_dict = {}
        self.opt_xor_dict2 = {"-a": ["-b"]}
        self.opt_xor_dict3 = {"-a": ["-b", "-c"], "-d": ["-e"]}

    def test_multiple_miss2(self):

        """Function:  test_multiple_miss2

        Description:  Test with multiple keys with one failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_xor_dict(self.args_array7,
                                                     self.opt_xor_dict3))

    def test_multiple_miss(self):

        """Function:  test_multiple_miss

        Description:  Test with multiple keys with one not present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array2,
                                                self.opt_xor_dict3))

    def test_multiple_mix(self):

        """Function:  test_multiple_mix

        Description:  Test with multiple key/list present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array8,
                                                self.opt_xor_dict3))

    def test_multiple_lists(self):

        """Function:  test_multiple_lists

        Description:  Test with multiple lists present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array6,
                                                self.opt_xor_dict3))

    def test_multiple_keys(self):

        """Function:  test_multiple_keys

        Description:  Test with multiple keys present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array5,
                                                self.opt_xor_dict3))

    def test_both_present(self):

        """Function:  test_both_present

        Description:  Test with both key and list options present.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_xor_dict(self.args_array4,
                                                     self.opt_xor_dict2))

    def test_list_only(self):

        """Function:  test_list_only

        Description:  Test with list option present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array3,
                                                self.opt_xor_dict2))

    def test_key_only(self):

        """Function:  test_key_only

        Description:  Test with key option present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array2,
                                                self.opt_xor_dict2))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty args_array.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array,
                                                self.opt_xor_dict2))

    def test_empty_optxordict(self):

        """Function:  test_empty_optxordict

        Description:  Test with empty list for opt_xor_dict.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array2,
                                                self.opt_xor_dict))

    def test_both_empty(self):

        """Function:  test_both_empty

        Description:  Test with both args with empty sets.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_xor_dict(self.args_array,
                                                self.opt_xor_dict))


if __name__ == "__main__":
    unittest.main()
