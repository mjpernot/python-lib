#!/usr/bin/python
# Classification (U)

"""Program:  is_add_cmd.py

    Description:  Unit testing of is_add_cmd in cmds_gen.py.

    Usage:
        test/unit/cmds_gen/is_add_cmd.py

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
import cmds_gen
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_list_boolean -> Test with single argument with a list.
        test_single_boolean -> Test with single argument with a boolean.
        test_single_value -> Test with single argument with a value.
        test_empty_argsarray -> Test with empty args_array.
        test_empty_optarglist -> Test with empty opt_arg_list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.setvalue = "--setvalue=OFF"
        self.args_array = {}
        self.args_array2 = {"-a": "value1"}
        self.args_array3 = {"-b": True}
        self.args_array4 = {"-c": True}
        self.cmd = ["--test"]
        self.opt_arg_list = []
        self.opt_arg_list2 = {"-a": "--setvalue="}
        self.opt_arg_list3 = {"-b": self.setvalue}
        self.opt_arg_list4 = {"-c": [self.setvalue, "--setstd=ON"]}

        self.base = ["--test"]
        self.base2 = ["--test", "--setvalue=value1"]
        self.base3 = ["--test", self.setvalue]
        self.base4 = ["--test", self.setvalue, "--setstd=ON"]

    def test_list_boolean(self):

        """Function:  test_list_boolean

        Description:  Test with single argument with a list.

        Arguments:

        """

        self.assertEqual(cmds_gen.is_add_cmd(self.args_array4, self.cmd,
                                             self.opt_arg_list4), self.base4)

    def test_single_boolean(self):

        """Function:  test_single_boolean

        Description:  Test with single argument with a boolean.

        Arguments:

        """

        self.assertEqual(cmds_gen.is_add_cmd(self.args_array3, self.cmd,
                                             self.opt_arg_list3), self.base3)

    def test_single_value(self):

        """Function:  test_single_value

        Description:  Test with single argument with a value.

        Arguments:

        """

        self.assertEqual(cmds_gen.is_add_cmd(self.args_array2, self.cmd,
                                             self.opt_arg_list2), self.base2)

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty args_array.

        Arguments:

        """

        self.assertEqual(cmds_gen.is_add_cmd(self.args_array, self.cmd,
                                             self.opt_arg_list2), self.base)

    def test_empty_optarglist(self):

        """Function:  test_empty_optarglist

        Description:  Test with empty opt_arg_list.

        Arguments:

        """

        self.assertEqual(cmds_gen.is_add_cmd(self.args_array, self.cmd,
                                             self.opt_arg_list), self.base)


if __name__ == "__main__":
    unittest.main()
