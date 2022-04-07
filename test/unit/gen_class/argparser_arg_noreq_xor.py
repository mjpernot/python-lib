#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_noreq_xor.py

    Description:  Unit testing of arg_noreq_xor in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_noreq_xor.py

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
        test_xor_norep_override
        test_two_match_two_fail
        test_two_match_one_fail
        test_two_match_success
        test_one_match_fail
        test_one_match_success
        test_empty_xor_noreq
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        self.argv = [p_name]
        self.argv2 = [p_name, "-a"]
        self.argv3 = [p_name, "-a", "-b"]
        self.argv4 = [p_name, "-a", "-c"]
        self.argv5 = [p_name, "-a", "-c", "-d"]
        self.argv6 = [p_name, "-a", "-b", "-c", "-d"]

        self.xor_noreq = {}
        self.xor_noreq2 = {"-a": "-b"}
        self.xor_noreq3 = {"-a": "-b", "-c": "-d"}
        self.xor_noreq4 = {"-a": "-b", "-c": "-e"}

    def test_xor_norep_override(self):

        """Function:  test_xor_norep_override

        Description:  Test with passing xor_norep to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, xor_noreq=self.xor_noreq3, do_parse=True)

        self.assertTrue(args_array.arg_noreq_xor(xor_noreq=self.xor_noreq4))

    def test_two_match_two_fail(self):

        """Function:  test_two_match_two_fail

        Description:  Test with two matches and both are failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, xor_noreq=self.xor_noreq3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_noreq_xor())

    def test_two_match_one_fail(self):

        """Function:  test_two_match_one_fail

        Description:  Test with two matches and one is failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, xor_noreq=self.xor_noreq3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_noreq_xor())

    def test_two_match_success(self):

        """Function:  test_two_match_success

        Description:  Test with two matches and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, xor_noreq=self.xor_noreq3, do_parse=True)

        self.assertTrue(args_array.arg_noreq_xor())

    def test_one_match_fail(self):

        """Function:  test_one_match_fail

        Description:  Test with one match and is failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, xor_noreq=self.xor_noreq2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_noreq_xor())

    def test_one_match_success(self):

        """Function:  test_one_match_success

        Description:  Test with one match and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, xor_noreq=self.xor_noreq2, do_parse=True)

        self.assertTrue(args_array.arg_noreq_xor())

    def test_empty_xornoreqlist(self):

        """Function:  test_empty_xornoreqlist

        Description:  Test with empty dictionary for xor_noreq_list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, xor_noreq=self.xor_noreq, do_parse=True)

        self.assertTrue(args_array.arg_noreq_xor())

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, xor_noreq=self.xor_noreq2, do_parse=True)

        self.assertTrue(args_array.arg_noreq_xor())


if __name__ == "__main__":
    unittest.main()
