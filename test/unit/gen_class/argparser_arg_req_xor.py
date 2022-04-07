#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_req_xor.py

    Description:  Unit testing of arg_req_xor in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_req_xor.py

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
        test_opt_xor_override
        test_two_match_fail
        test_one_match_success
        test_empty_opt_xor
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

        self.opt_xor = {}
        self.opt_xor2 = {"-a": "-b"}
        self.opt_xor3 = {"-a": "-c"}

    def test_opt_xor_override(self):

        """Function:  test_opt_xor_override

        Description:  Test with opt_xor passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_xor=self.opt_xor2, do_parse=True)

        self.assertTrue(args_array.arg_req_xor(opt_xor=self.opt_xor3))

    def test_two_match_fail(self):

        """Function:  test_two_match_fail

        Description:  Test with two matches and is failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_xor=self.opt_xor2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_req_xor())

    def test_one_match_success(self):

        """Function:  test_one_match_success

        Description:  Test with one match and is successful.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_xor=self.opt_xor2, do_parse=True)

        self.assertTrue(args_array.arg_req_xor())

    def test_empty_opt_xor(self):

        """Function:  test_empty_opt_xor

        Description:  Test with empty dictionary for opt_xor.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_xor=self.opt_xor, do_parse=True)

        self.assertTrue(args_array.arg_req_xor())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_xor=self.opt_xor2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_req_xor())


if __name__ == "__main__":
    unittest.main()
