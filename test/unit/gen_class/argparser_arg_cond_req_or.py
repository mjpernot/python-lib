# Classification (U)

"""Program:  argparser_arg_cond_req_or.py

    Description:  Unit testing of arg_cond_req_or in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_cond_req_or.py

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
        test_opt_con_or_override
        test_multi_cond_req2
        test_multi_cond_req
        test_two_cond_req2
        test_two_cond_req
        test_two_args_present
        test_one_arg_present
        test_empty_opt_con_req
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        self.argv = [p_name]
        self.argv2 = [p_name, "-c"]
        self.argv3 = [p_name, "-c", "-f"]
        self.argv4 = [p_name, "-c", "-f", "-m"]
        self.argv5 = [p_name, "-c", "-d", "-f", "-m"]
        self.argv6 = [p_name, "-c", "-d", "-f"]

        self.opt_con_or = {}
        self.opt_con_or2 = {"-c": ["-f"]}
        self.opt_con_or3 = {"-c": ["-f", "-m"]}
        self.opt_con_or4 = {"-c": ["-f"], "-f": ["-m"]}
        self.opt_con_or5 = {"-c": ["-f", "-m"], "-d": ["-c"]}
        self.opt_con_or6 = {"-c": ["-f", "-m"], "-d": ["-g"]}

    def test_opt_con_or_override(self):

        """Function:  test_opt_con_or_override

        Description:  Test with passing in argument to override default
            attribute.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_con_or=self.opt_con_or6, do_parse=True)

        self.assertTrue(
            args_array.arg_cond_req_or(opt_con_or=self.opt_con_or3))

    def test_multi_cond_req2(self):

        """Function:  test_multi_cond_req2

        Description:  Test with multiple conditional requirements, one missing.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_con_or=self.opt_con_or6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_cond_req_or())

    def test_multi_cond_req(self):

        """Function:  test_multi_cond_req

        Description:  Test with multiple conditional requirements present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, opt_con_or=self.opt_con_or5, do_parse=True)

        self.assertTrue(args_array.arg_cond_req_or())

    def test_two_cond_req2(self):

        """Function:  test_two_cond_req2

        Description:  Test with two conditional requirements, one missing.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_con_or=self.opt_con_or4, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_cond_req_or())

    def test_two_cond_req(self):

        """Function:  test_two_cond_req

        Description:  Test with two conditional requirements.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_con_or=self.opt_con_or4, do_parse=True)

        self.assertTrue(args_array.arg_cond_req_or())

    def test_two_args_present(self):

        """Function:  test_two_args_present

        Description:  Test with two arguments are present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_con_or=self.opt_con_or3, do_parse=True)

        self.assertTrue(args_array.arg_cond_req_or())

    def test_one_arg_present(self):

        """Function:  test_one_arg_present

        Description:  Test with one argument is present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_con_or=self.opt_con_or2, do_parse=True)

        self.assertTrue(args_array.arg_cond_req_or())

    def test_empty_opt_con_req(self):

        """Function:  test_empty_opt_con_req

        Description:  Test with empty list for opt_con_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_con_or=self.opt_con_or, do_parse=True)

        self.assertTrue(args_array.arg_cond_req_or())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_con_or=self.opt_con_or2, do_parse=True)

        self.assertTrue(args_array.arg_cond_req_or())


if __name__ == "__main__":
    unittest.main()
