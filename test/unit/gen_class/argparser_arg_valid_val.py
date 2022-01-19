#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_valid_val.py

    Description:  Unit testing of arg_valid_val in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_valid_val.py

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
import gen_class
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_two_values_fail2
        test_two_values_fail
        test_two_values_success
        test_value_fail
        test_value_success
        test_empty_both
        test_empty_valid_func
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-a", "value"]
        self.argv3 = ["program.py", "-a", "invalid"]
        self.argv4 = ["program.py", "-a", "value", "-b", "value2"]
        self.argv5 = ["program.py", "-a", "invalid", "-b", "value2"]
        self.argv6 = ["program.py", "-a", "invalid", "-b", "invalid"]

        self.opt_val = ["-a", "-b"]

        self.opt_valid_val = {}
        self.opt_valid_val2 = {"-a": ["value", "value1"]}
        self.opt_valid_val3 = {"-a": ["value", "value1"], "-b": ["value2"]}

    def test_two_values_fail2(self):

        """Function:  test_two_values_fail2

        Description:  Test with two values and two failures.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_valid_val())

    def test_two_values_fail(self):

        """Function:  test_two_values_fail

        Description:  Test with two values and one failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_valid_val())

    def test_two_values_success(self):

        """Function:  test_two_values_success

        Description:  Test with two values and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val3, do_parse=True)

        self.assertTrue(args_array.arg_valid_val())

    def test_value_fail(self):

        """Function:  test_value_fail

        Description:  Test with one value and is failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_valid_val())

    def test_value_success(self):

        """Function:  test_value_success

        Description:  Test with one value and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val2, do_parse=True)

        self.assertTrue(args_array.arg_valid_val())

    def test_empty_both(self):

        """Function:  test_empty_both

        Description:  Test with empty dictionary for both arguments.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val, do_parse=True)

        self.assertTrue(args_array.arg_valid_val())

    def test_empty_valid_func(self):

        """Function:  test_empty_valid_func

        Description:  Test with empty dictionary for opt_valid_val.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val, do_parse=True)

        self.assertTrue(args_array.arg_valid_val())

    def test_empty_args_array(self):

        """Function:  test_empty_arg_sarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val,
            opt_valid_val=self.opt_valid_val2, do_parse=True)

        self.assertTrue(args_array.arg_valid_val())


if __name__ == "__main__":
    unittest.main()
