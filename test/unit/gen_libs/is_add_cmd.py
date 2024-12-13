# Classification (U)

"""Program:  is_add_cmd.py

    Description:  Unit testing of is_add_cmd in gen_libs.py.

    Usage:
        test/unit/gen_libs/is_add_cmd.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list_boolean
        test_single_boolean
        test_single_value
        test_empty_argsarray
        test_empty_optarglist

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = gen_class.ArgParser(["program"])
        self.args2 = gen_class.ArgParser(["program"])
        self.args3 = gen_class.ArgParser(["program"])
        self.args4 = gen_class.ArgParser(["program"])
        self.setvalue = "--setvalue=OFF"
        self.args.args_array = {}
        self.args2.args_array = {"-a": "value1"}
        self.args3.args_array = {"-b": True}
        self.args4.args_array = {"-c": True}
        self.cmd = ["--test"]
        self.opt_arg_list = []
        self.opt_arg_list2 = {"-a": "--setvalue="}
        self.opt_arg_list3 = {"-b": self.setvalue}
        self.opt_arg_list4 = {"-c": [self.setvalue, "--setstd=ON"]}

        self.base = ["--test"]
        self.base2 = ["--test", "--setvalue=value1"]
        self.base3 = ["--test", self.setvalue]
        self.base4 = ["--test", self.setvalue, "--setstd=ON"]

    def test_args_list_boolean(self):

        """Function:  test_args_list_boolean

        Description:  Test with ArgParser instance with single argument with a
            list.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args4, self.cmd, self.opt_arg_list4), self.base4)

    def test_args_single_boolean(self):

        """Function:  test_args_single_boolean

        Description:  Test with ArgParser instance with single argument with a
            boolean.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args3, self.cmd, self.opt_arg_list3), self.base3)

    def test_args_single_value(self):

        """Function:  test_args_single_value

        Description:  Test with ArgParser instance with single argument with a
            value.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args2, self.cmd, self.opt_arg_list2), self.base2)

    def test_args_empty_argsarray(self):

        """Function:  test_args_empty_argsarray

        Description:  Test with ArgParser instance with empty args_array.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args, self.cmd, self.opt_arg_list2), self.base)

    def test_args_empty_optarglist(self):

        """Function:  test_args_empty_optarglist

        Description:  Test with ArgParser instance with empty opt_arg_list.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args, self.cmd, self.opt_arg_list), self.base)

    def test_list_boolean(self):

        """Function:  test_list_boolean

        Description:  Test with single argument with a list.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args4, self.cmd, self.opt_arg_list4), self.base4)

    def test_single_boolean(self):

        """Function:  test_single_boolean

        Description:  Test with single argument with a boolean.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args3, self.cmd, self.opt_arg_list3), self.base3)

    def test_single_value(self):

        """Function:  test_single_value

        Description:  Test with single argument with a value.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args2, self.cmd, self.opt_arg_list2), self.base2)

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty args_array.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args, self.cmd, self.opt_arg_list2), self.base)

    def test_empty_optarglist(self):

        """Function:  test_empty_optarglist

        Description:  Test with empty opt_arg_list.

        Arguments:

        """

        self.assertEqual(
            gen_libs.is_add_cmd(
                self.args, self.cmd, self.opt_arg_list), self.base)


if __name__ == "__main__":
    unittest.main()
