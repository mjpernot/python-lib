#!/usr/bin/python
# Classification (U)

"""Program:  arg_validate.py

    Description:  Unit testing of arg_validate in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_validate.py

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


def validate_value(arg):

    """Function:  validate_value

    Description:  Test function.

    Arguments:
        (input) arg -> Test value being tested.

    """

    return arg == "value"


def validate_value2(arg):

    """Function:  validate_value2

    Description:  Test function.

    Arguments:
        (input) arg -> Test value being tested.

    """

    return arg == "value2"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_two_validate_fail2 -> Test with two match and two failures.
        test_two_validate_fail -> Test with two match and one failure.
        test_two_validate_success -> Test with two match and is successful.
        test_validate_fail -> Test with one match and is failure.
        test_validate_success -> Test with one match and is successful.
        test_empty_validfunc -> Test with empty dict for valid_func.
        test_empty_argsarray -> Test with empty dictionary for args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": "value"}
        self.args_array3 = {"-a": "value1"}
        self.args_array4 = {"-a": "value", "-b": "value2"}
        self.args_array5 = {"-a": "value1", "-b": "value2"}

        self.valid_func = {}
        self.valid_func2 = {"-a": validate_value}
        self.valid_func3 = {"-a": validate_value, "-b": validate_value2}

    def test_two_validate_fail2(self):

        """Function:  test_two_validate_fail2

        Description:  Test with two match and two failures.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_validate(self.args_array4,
                                                self.valid_func3))

    def test_two_validate_fail(self):

        """Function:  test_two_validate_fail

        Description:  Test with two match and one failure.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_validate(self.args_array4,
                                                self.valid_func3))

    def test_two_validate_success(self):

        """Function:  test_two_validate_success

        Description:  Test with two match and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_validate(self.args_array4,
                                                self.valid_func3))

    def test_validate_fail(self):

        """Function:  test_validate_fail

        Description:  Test with one match and is failure.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(arg_parser.arg_validate(self.args_array3,
                                                     self.valid_func2))

    def test_validate_success(self):

        """Function:  test_validate_success

        Description:  Test with one match and is successful.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_validate(self.args_array2,
                                                self.valid_func2))

    def test_empty_validfunc(self):

        """Function:  test_empty_validfunc

        Description:  Test with empty dictionary for valid_func.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_validate(self.args_array2,
                                                self.valid_func))

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_validate(self.args_array,
                                                self.valid_func2))


if __name__ == "__main__":
    unittest.main()
