#!/usr/bin/python
# Classification (U)

"""Program:  argparser_update_arg.py

    Description:  Unit testing of update_arg in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_update_arg.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_insert2
        test_insert
        test_arg_not_exist2
        test_arg_not_exist
        test_update_arg2
        test_update_arg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.opt_val = ["-a"]

        self.argv = ["program.py", "-a", "value", "-b"]

        self.arg_key = "-a"
        self.arg_key2 = "-c"
        self.arg_val = "value2"

        self.results = (True, None)
        self.results2 = (False, "Arg key does not exists")

        self.arg_results = {"-a": "value2", "-b": True}
        self.arg_results2 = {"-a": "value", "-b": True}
        self.arg_results3 = {"-a": "value", "-b": True, "-c": "value2"}

    def test_insert2(self):

        """Function:  test_insert2

        Description:  Test with overwrite option.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        args_array.update_arg(self.arg_key2, self.arg_val, insert=True)

        self.assertEqual(args_array.args_array, self.arg_results3)

    def test_insert(self):

        """Function:  test_insert

        Description:  Test with overwrite option.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.update_arg(
                self.arg_key2, self.arg_val, insert=True), self.results)

    def test_arg_not_exist2(self):

        """Function:  test_arg_exist2

        Description:  Test with key exists.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        args_array.update_arg(self.arg_key2, self.arg_val)

        self.assertEqual(args_array.args_array, self.arg_results2)

    def test_arg_not_exist(self):

        """Function:  test_arg_exist

        Description:  Test with key exists.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.update_arg(self.arg_key2, self.arg_val), self.results2)

    def test_update_arg2(self):

        """Function:  test_update_arg2

        Description:  Test with arg update.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        args_array.update_arg(self.arg_key, self.arg_val)

        self.assertEqual(args_array.args_array, self.arg_results)

    def test_update_arg(self):

        """Function:  test_update_arg

        Description:  Test with arg update.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.update_arg(self.arg_key, self.arg_val), self.results)


if __name__ == "__main__":
    unittest.main()
