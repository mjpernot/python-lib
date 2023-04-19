# Classification (U)

"""Program:  help_func.py

    Description:  Unit testing of help_func in gen_libs.py.

    Usage:
        test/unit/gen_libs/help_func.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs
import gen_class
import version

__version__ = version.__version__


def holder():

    """Function:  holder

    Description:  Stub holder for func_name in help_func.

    Arguments:

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_args_help_option
        test_args_version_option
        test_args_both_options
        test_args_no_options
        test_help_option
        test_version_option
        test_both_options
        test_no_options

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = gen_class.ArgParser(["program"])
        self.args_array = {}
        self.args_array2 = {"-h": True}
        self.args_array3 = {"-v": True}
        self.args_array4 = {"-v": True, "-h": True}
        self.version = "1.0.0"
        self.funct_names = holder

    def test_args_help_option(self):

        """Function:  test_args_help_option

        Description:  Test with ArgParser instance with -h option.

        Arguments:

        """

        self.args.args_array = self.args_array2

        self.assertTrue(
            gen_libs.help_func(self.args, self.version, self.funct_names))

    def test_args_version_option(self):

        """Function:  test_args_version_option

        Description:  Test with ArgParser instance with -v option.

        Arguments:

        """

        self.args.args_array = self.args_array3

        with gen_libs.no_std_out():
            self.assertTrue(
                gen_libs.help_func(self.args, self.version, self.funct_names))

    def test_args_both_options(self):

        """Function:  test_args_both_options

        Description:  Test with ArgParser instance with -h and -v options.

        Arguments:

        """

        self.args.args_array = self.args_array4

        with gen_libs.no_std_out():
            self.assertTrue(
                gen_libs.help_func(self.args, self.version, self.funct_names))

    def test_args_no_options(self):

        """Function:  test_args_no_options

        Description:  Test with ArgParser instance with no -h or -v options.

        Arguments:

        """

        self.assertFalse(
            gen_libs.help_func(self.args, self.version, self.funct_names))

    def test_help_option(self):

        """Function:  test_help_option

        Description:  Test with -h option.

        Arguments:

        """

        self.assertTrue(
            gen_libs.help_func(
                self.args_array2, self.version, self.funct_names))

    def test_version_option(self):

        """Function:  test_version_option

        Description:  Test with -v option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(
                gen_libs.help_func(
                    self.args_array3, self.version, self.funct_names))

    def test_both_options(self):

        """Function:  test_both_options

        Description:  Test with -h and -v options.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(
                gen_libs.help_func(
                    self.args_array4, self.version, self.funct_names))

    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no -h or -v options in array.

        Arguments:

        """

        self.assertFalse(
            gen_libs.help_func(
                self.args_array, self.version, self.funct_names))


if __name__ == "__main__":
    unittest.main()
