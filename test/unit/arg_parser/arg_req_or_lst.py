# Classification (U)

"""Program:  arg_req_or_lst.py

    Description:  Unit testing of arg_req_or_lst in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_req_or_lst.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_multiple_miss2
        test_multiple_miss
        test_multiple_mix
        test_multiple_lists
        test_multiple_keys
        test_missing_option
        test_both_present
        test_list_only
        test_key_only
        test_empty_argsarray
        test_empty_optreqlist
        test_both_empty

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": True}
        self.args_array3 = {"-a": True, "-b": True}
        self.args_array4 = {"-b": True, "-c": True}
        self.args_array5 = {"-a": True, "-d": True}
        self.args_array6 = {"-c": True, "-e": True}
        self.args_array7 = {"-d": True, "-e": True}
        self.args_array8 = {"-a": True, "-e": True}
        self.args_array9 = {"-e": True}

        self.opt_or_dict_list = {}
        self.opt_or_dict_list2 = {"-a": ["-b"]}
        self.opt_or_dict_list3 = {"-a": ["-b", "-c"], "-d": ["-e"]}

    def test_multiple_miss2(self):

        """Function:  test_multiple_miss2

        Description:  Test with multiple keys with one not present.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_req_or_lst(self.args_array9,
                                                       self.opt_or_dict_list3))

    def test_multiple_miss(self):

        """Function:  test_multiple_miss

        Description:  Test with multiple keys with one not present.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_req_or_lst(self.args_array2,
                                                       self.opt_or_dict_list3))

    def test_multiple_mix(self):

        """Function:  test_multiple_mix

        Description:  Test with multiple key/list present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array8,
                                                  self.opt_or_dict_list3))

    def test_multiple_lists(self):

        """Function:  test_multiple_lists

        Description:  Test with multiple lists present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array6,
                                                  self.opt_or_dict_list3))

    def test_multiple_keys(self):

        """Function:  test_multiple_keys

        Description:  Test with multiple keys present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array5,
                                                  self.opt_or_dict_list3))

    def test_missing_option(self):

        """Function:  test_missing_option

        Description:  Test with both key and list options not present.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_req_or_lst(self.args_array7,
                                                       self.opt_or_dict_list2))

    def test_both_present(self):

        """Function:  test_both_present

        Description:  Test with both key and list options present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array3,
                                                  self.opt_or_dict_list2))

    def test_list_only(self):

        """Function:  test_list_only

        Description:  Test with list option present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array4,
                                                  self.opt_or_dict_list2))

    def test_key_only(self):

        """Function:  test_key_only

        Description:  Test with key option present.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array2,
                                                  self.opt_or_dict_list2))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty args_array.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_req_or_lst(self.args_array,
                                                       self.opt_or_dict_list2))

    def test_empty_optreqlist(self):

        """Function:  test_empty_optreqlist

        Description:  Test with empty list for opt_req_list.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array2,
                                                  self.opt_or_dict_list))

    def test_both_empty(self):

        """Function:  test_both_empty

        Description:  Test with both args with empty sets.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_req_or_lst(self.args_array,
                                                  self.opt_or_dict_list))


if __name__ == "__main__":
    unittest.main()
