# Classification (U)

"""Program:  argparser_delete_arg.py

    Description:  Unit testing of delete_arg in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_delete_arg.py

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
        test_arg_not_exist2
        test_arg_not_exist
        test_delete_arg2
        test_delete_arg

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

        self.results = (True, None)
        self.results2 = (False, "Arg key does not exists")

        self.arg_results = {"-b": True}
        self.arg_results2 = {"-a": "value", "-b": True}

    def test_arg_not_exist2(self):

        """Function:  test_arg_exist2

        Description:  Test with key exists.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        args_array.delete_arg(self.arg_key2)

        self.assertEqual(args_array.args_array, self.arg_results2)

    def test_arg_not_exist(self):

        """Function:  test_arg_exist

        Description:  Test with key exists.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.delete_arg(self.arg_key2), self.results2)

    def test_delete_arg2(self):

        """Function:  test_delete_arg2

        Description:  Test with arg update.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        args_array.delete_arg(self.arg_key)

        self.assertEqual(args_array.args_array, self.arg_results)

    def test_delete_arg(self):

        """Function:  test_delete_arg

        Description:  Test with arg update.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.delete_arg(self.arg_key), self.results)


if __name__ == "__main__":
    unittest.main()
