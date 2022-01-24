#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_require.py

    Description:  Unit testing of arg_require in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_require.py

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
        test_opt_req_override
        test_two_require_one_fail
        test_two_require
        test_one_require
        test_empty_args_array
        test_empty_opt_req
        test_both_empty

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-a"]
        self.argv3 = ["program.py", "-a", "-c"]
        self.argv4 = ["program.py", "-a", "-d"]

        self.opt_req = []
        self.opt_req2 = ["-a"]
        self.opt_req3 = ["-a", "-c"]
        self.opt_req4 = ["-a", "-d"]

    def test_opt_req_override(self):

        """Function:  test_opt_req_override

        Description:  Test with opt_req passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_req=self.opt_req3, do_parse=True)

        self.assertTrue(args_array.arg_require(opt_req=self.opt_req4))

    def test_two_require_one_fail(self):

        """Function:  test_two_require_one_fail

        Description:  Test with two required arguments, but one failure.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_req=self.opt_req3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_require())

    def test_two_require(self):

        """Function:  test_two_require

        Description:  Test with two required arguments.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_req=self.opt_req3, do_parse=True)

        self.assertTrue(args_array.arg_require())

    def test_one_require(self):

        """Function:  test_one_require

        Description:  Test with one required argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_req=self.opt_req2, do_parse=True)

        self.assertTrue(args_array.arg_require())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_req=self.opt_req2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_require())

    def test_empty_opt_req(self):

        """Function:  test_empty_opt_req

        Description:  Test with empty list for opt_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_req=self.opt_req, do_parse=True)

        self.assertTrue(args_array.arg_require())

    def test_both_empty(self):

        """Function:  test_both_empty

        Description:  Test with both args with empty sets.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_req=self.opt_req, do_parse=True)

        self.assertTrue(args_array.arg_require())


if __name__ == "__main__":
    unittest.main()
