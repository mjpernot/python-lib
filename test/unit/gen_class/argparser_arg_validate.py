# Classification (U)

"""Program:  argparser_arg_validate.py

    Description:  Unit testing of arg_validate in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_validate.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


def validate_value(arg):

    """Function:  validate_value

    Description:  Test function.

    Arguments:

    """

    return arg == "value"


def validate_value2(arg):

    """Function:  validate_value2

    Description:  Test function.

    Arguments:

    """

    return arg == "value2"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_valid_func_override
        test_two_validate_fail2
        test_two_validate_fail
        test_two_validate_success
        test_validate_fail
        test_validate_success
        test_empty_valid_func
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        self.argv = [p_name]
        self.argv2 = [p_name, "-a", "value"]
        self.argv3 = [p_name, "-a", "value1"]
        self.argv4 = [p_name, "-a", "value", "-b", "value2"]
        self.argv5 = [p_name, "-a", "value1", "-b", "value2"]
        self.argv6 = [p_name, "-a", "value1", "-b", "value1"]

        self.opt_val = ["-a", "-b"]

        self.valid_func = {}
        self.valid_func2 = {"-a": validate_value}
        self.valid_func3 = {"-a": validate_value, "-b": validate_value2}
        self.valid_func4 = {"-a": validate_value2}

    def test_valid_func_override(self):

        """Function:  test_valid_func_override

        Description:  Test with valid_func passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, valid_func=self.valid_func4,
            do_parse=True)

        self.assertTrue(args_array.arg_validate(valid_func=self.valid_func2))

    def test_two_validate_fail2(self):

        """Function:  test_two_validate_fail2

        Description:  Test with two match and two failures.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, valid_func=self.valid_func3,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_validate())

    def test_two_validate_fail(self):

        """Function:  test_two_validate_fail

        Description:  Test with two match and one failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, valid_func=self.valid_func3,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_validate())

    def test_two_validate_success(self):

        """Function:  test_two_validate_success

        Description:  Test with two match and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, valid_func=self.valid_func3,
            do_parse=True)

        self.assertTrue(args_array.arg_validate())

    def test_validate_fail(self):

        """Function:  test_validate_fail

        Description:  Test with one match and is failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, valid_func=self.valid_func2,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_validate())

    def test_validate_success(self):

        """Function:  test_validate_success

        Description:  Test with one match and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, valid_func=self.valid_func2,
            do_parse=True)

        self.assertTrue(args_array.arg_validate())

    def test_empty_valid_func(self):

        """Function:  test_empty_valid_func

        Description:  Test with empty dictionary for valid_func.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, valid_func=self.valid_func,
            do_parse=True)

        self.assertTrue(args_array.arg_validate())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, valid_func=self.valid_func2,
            do_parse=True)

        self.assertTrue(args_array.arg_validate())


if __name__ == "__main__":
    unittest.main()
