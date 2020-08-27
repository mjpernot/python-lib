#!/usr/bin/python
# Classification (U)

"""Program:  arg_valid_val.py

    Description:  Unit testing of arg_valid_val in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_valid_val.py

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
        test_two_values_fail2 -> Test with two values and two failures.
        test_two_values_fail -> Test with two values and one failure.
        test_two_values_success -> Test with two values and is successful.
        test_value_fail -> Test with one value and is failure.
        test_value_success -> Test with one value and is successful.
        test_empty_both -> Test with empty dictionary for both arguments.
        test_empty_validfunc -> Test with empty dict for opt_valid_val.
        test_empty_argsarray -> Test with empty dictionary for args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": "value"}
        self.args_array3 = {"-a": "invalid"}
        self.args_array4 = {"-a": "value", "-b": "value2"}
        self.args_array5 = {"-a": "invalid", "-b": "value2"}
        self.args_array6 = {"-a": "invalid", "-b": "invalid"}

        self.opt_valid_val = {}
        self.opt_valid_val2 = {"-a": ["value", "value1"]}
        self.opt_valid_val3 = {"-a": ["value", "value1"], "-b": ["value2"]}

    def test_two_values_fail2(self):

        """Function:  test_two_values_fail2

        Description:  Test with two values and two failures.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_valid_val(self.args_array6,
                                                      self.opt_valid_val3))

    def test_two_values_fail(self):

        """Function:  test_two_values_fail

        Description:  Test with two values and one failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_valid_val(self.args_array5,
                                                      self.opt_valid_val3))

    def test_two_values_success(self):

        """Function:  test_two_values_success

        Description:  Test with two values and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_valid_val(self.args_array4,
                                                 self.opt_valid_val3))

    def test_value_fail(self):

        """Function:  test_value_fail

        Description:  Test with one value and is failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_valid_val(self.args_array3,
                                                      self.opt_valid_val2))

    def test_value_success(self):

        """Function:  test_value_success

        Description:  Test with one value and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_valid_val(self.args_array2,
                                                 self.opt_valid_val2))

    def test_empty_both(self):

        """Function:  test_empty_both

        Description:  Test with empty dictionary for both arguments.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_valid_val(self.args_array2,
                                                 self.opt_valid_val))

    def test_empty_validfunc(self):

        """Function:  test_empty_validfunc

        Description:  Test with empty dictionary for opt_valid_val.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_valid_val(self.args_array2,
                                                 self.opt_valid_val))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_valid_val(self.args_array,
                                                 self.opt_valid_val2))


if __name__ == "__main__":
    unittest.main()
