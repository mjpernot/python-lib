#!/usr/bin/python
# Classification (U)

"""Program:  arg_noreq_xor.py

    Description:  Unit testing of arg_noreq_xor in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_noreq_xor.py

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
        test_two_match_two_fail
        test_two_match_one_fail
        test_two_match_success -> Test with two matches and is successful
        test_one_match_fail
        test_one_match_success
        test_empty_xornoreqlist
        test_empty_argsarray

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": True}
        self.args_array3 = {"-a": True, "-b": True}
        self.args_array4 = {"-a": True, "-c": True}
        self.args_array5 = {"-a": True, "-c": True, "-d": True}
        self.args_array6 = {"-a": True, "-b": True, "-c": True, "-d": True}

        self.xor_noreq_list = {}
        self.xor_noreq_list2 = {"-a": "-b"}
        self.xor_noreq_list3 = {"-a": "-b", "-c": "-d"}

    def test_two_match_two_fail(self):

        """Function:  test_two_match_two_fail

        Description:  Test with two matches and both are failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_noreq_xor(self.args_array6,
                                                      self.xor_noreq_list3))

    def test_two_match_one_fail(self):

        """Function:  test_two_match_one_fail

        Description:  Test with two matches and one is failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_noreq_xor(self.args_array5,
                                                      self.xor_noreq_list3))

    def test_two_match_success(self):

        """Function:  test_two_match_success

        Description:  Test with two matches and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_noreq_xor(self.args_array4,
                                                 self.xor_noreq_list3))

    def test_one_match_fail(self):

        """Function:  test_one_match_fail

        Description:  Test with one match and is failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_noreq_xor(self.args_array3,
                                                      self.xor_noreq_list2))

    def test_one_match_success(self):

        """Function:  test_one_match_success

        Description:  Test with one match and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_noreq_xor(self.args_array2,
                                                 self.xor_noreq_list2))

    def test_empty_xornoreqlist(self):

        """Function:  test_empty_xornoreqlist

        Description:  Test with empty dictionary for xor_noreq_list.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_noreq_xor(self.args_array2,
                                                 self.xor_noreq_list))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_noreq_xor(self.args_array,
                                                 self.xor_noreq_list2))


if __name__ == "__main__":
    unittest.main()
