# Classification (U)

"""Program:  argparser_arg_default.py

    Description:  Unit testing of arg_default in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_default.py

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
        test_opt_def_override
        test_arg_in_args_array
        test_arg_in_opt_def
        test_arg_not_in_opt_def
        test_empty_opt_def

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py", "-c"]
        self.argv2 = ["program.py", "-c", "-f"]

        self.opt_def = {}
        self.opt_def2 = {"-f": "file1", "-i": "sysmon"}

        self.arg = "-f"
        self.arg2 = "-g"

        self.results = {"-c": True, "-f": True}

    def test_opt_def_override(self):

        """Function:  test_opt_def_override

        Description:  Test with passing in opt_def to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_def=self.opt_def, do_parse=True)

        self.assertTrue(args_array.arg_default(
            arg=self.arg, opt_def=self.opt_def2))

    def test_arg_in_args_array2(self):

        """Function:  test_arg_in_args_array2

        Description:  Test with arg already in args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_def=self.opt_def2, do_parse=True)
        args_array.arg_default(arg=self.arg)

        self.assertEqual(args_array.args_array, self.results)

    def test_arg_in_args_array(self):

        """Function:  test_arg_in_args_array

        Description:  Test with arg already in args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_def=self.opt_def2, do_parse=True)

        self.assertTrue(args_array.arg_default(arg=self.arg))

    def test_arg_in_opt_def(self):

        """Function:  test_arg_in_opt_def

        Description:  Test with arg in opt_def.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_def=self.opt_def2, do_parse=True)

        self.assertTrue(args_array.arg_default(arg=self.arg))

    def test_arg_not_in_opt_def(self):

        """Function:  test_arg_not_in_opt_def

        Description:  Test with arg not in opt_def.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_def=self.opt_def2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_default(arg=self.arg2))

    def test_empty_opt_def(self):

        """Function:  test_empty_opt_def

        Description:  Test with opt_def being empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_def=self.opt_def, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_default(arg=self.arg))


if __name__ == "__main__":
    unittest.main()
