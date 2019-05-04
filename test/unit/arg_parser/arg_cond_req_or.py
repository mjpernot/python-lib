#!/usr/bin/python
# Classification (U)

"""Program:  arg_cond_req_or.py

    Description:  Unit testing of arg_cond_req_or in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_cond_req_or.py

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
        test_multi_cond_req2 -> Test multi conditional requirements, 1 missing.
        test_multi_cond_req -> Test multiple conditional requirements present.
        test_two_cond_req2 -> Test two conditional requirements, one missing.
        test_two_cond_req -> Test with two conditional requirements.
        test_two_args_present -> Test with two arguments are present.
        test_one_arg_present -> Test with one argument is present.
        test_empty_optconreqdict -> Test with empty dict for opt_con_req_dict.
        test_empty_argsarray -> Test with empty args_array.

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
        self.args_array4 = {"-c": "config", "-f": "file1", "-m": "file2"}
        self.args_array5 = {"-c": "config", "-d": "dir", "-f": "file1",
                            "-m": "file2"}
        self.args_array6 = {"-c": "config", "-d": "dir", "-f": "file1"}

        self.opt_con_req_dict = {}
        self.opt_con_req_dict2 = {"-c": ["-f"]}
        self.opt_con_req_dict3 = {"-c": ["-f", "-m"]}
        self.opt_con_req_dict4 = {"-c": ["-f"] , "-f": ["-m"]}
        self.opt_con_req_dict5 = {"-c": ["-f", "-m"] , "-d": ["-c"]}
        self.opt_con_req_dict6 = {"-c": ["-f", "-m"] , "-d": ["-g"]}

    def test_multi_cond_req2(self):

        """Function:  test_multi_cond_req2

        Description:  Test with multiple conditional requirements, one missing.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            status = arg_parser.arg_cond_req_or(self.args_array6,
                                                self.opt_con_req_dict6)

        self.assertFalse(status)

    def test_multi_cond_req(self):

        """Function:  test_multi_cond_req

        Description:  Test with multiple conditional requirements present.

        Arguments:
            None

        """
        
        self.assertTrue(arg_parser.arg_cond_req_or(self.args_array5,
                                                   self.opt_con_req_dict5))

    def test_two_cond_req2(self):

        """Function:  test_two_cond_req2

        Description:  Test with two conditional requirements, one missing.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            status = arg_parser.arg_cond_req_or(self.args_array3,
                                                self.opt_con_req_dict4)

        self.assertFalse(status)

    def test_two_cond_req(self):

        """Function:  test_two_cond_req

        Description:  Test with two conditional requirements.

        Arguments:
            None

        """
        
        self.assertTrue(arg_parser.arg_cond_req_or(self.args_array4,
                                                   self.opt_con_req_dict4))

    def test_two_args_present(self):

        """Function:  test_two_args_present

        Description:  Test with two arguments are present.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req_or(self.args_array4,
                                                   self.opt_con_req_dict3))

    def test_one_arg_present(self):

        """Function:  test_one_arg_present

        Description:  Test with one argument is present.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req_or(self.args_array3,
                                                   self.opt_con_req_dict2))

    def test_empty_optconreqlist(self):

        """Function:  test_empty_optconreqlist

        Description:  Test with empty list for opt_con_req_list.

        Arguments:
            None

        """

        self.assertTrue(arg_parser.arg_cond_req_or(self.args_array2,
                                                   self.opt_con_req_dict))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty list for def_array.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            status = arg_parser.arg_cond_req_or(self.args_array,
                                                self.opt_con_req_dict2)

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
