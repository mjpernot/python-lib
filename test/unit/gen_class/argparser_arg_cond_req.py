# Classification (U)

"""Program:  argparser_arg_cond_req.py

    Description:  Unit testing of arg_cond_req in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_cond_req.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_two_args_missing
        test_one_arg_missing
        test_two_args_required
        test_one_arg_required
        test_empty_opt_con_req
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        self.argv = [p_name, "-c"]
        self.argv2 = [p_name, "-c", "-f"]
        self.argv3 = [p_name, "-c", "-f", "-g"]
        self.argv4 = [p_name]

        self.opt_con_req = {}
        self.opt_con_req2 = {"-c": ["-f"]}
        self.opt_con_req3 = {"-c": ["-f", "-g"]}
        self.opt_con_req4 = {"-c": ["-a"]}

    def test_opt_con_req_override(self):

        """Function:  test_opt_con_req_override

        Description:  Test with passing in argument to method to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_con_req=self.opt_con_req4, do_parse=True)

        self.assertTrue(args_array.arg_cond_req(opt_con_req=self.opt_con_req3))

    def test_two_args_missing(self):

        """Function:  test_two_args_missing

        Description:  Test with two arguments required, but missing.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_con_req=self.opt_con_req3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_cond_req())

    def test_one_arg_missing(self):

        """Function:  test_one_arg_missing

        Description:  Test with one argument required, but missing.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_con_req=self.opt_con_req2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_cond_req())

    def test_two_args_required(self):

        """Function:  test_two_args_required

        Description:  Test with two arguments required and are present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_con_req=self.opt_con_req3, do_parse=True)

        self.assertTrue(args_array.arg_cond_req())

    def test_one_arg_required(self):

        """Function:  test_one_arg_required

        Description:  Test with one argument required and is present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_con_req=self.opt_con_req2, do_parse=True)

        self.assertTrue(args_array.arg_cond_req())

    def test_empty_opt_con_req(self):

        """Function:  test_empty_opt_con_req

        Description:  Test with empty list for opt_con_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_con_req=self.opt_con_req, do_parse=True)

        self.assertTrue(args_array.arg_cond_req())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty list for def_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_con_req=self.opt_con_req2, do_parse=True)

        self.assertTrue(args_array.arg_cond_req())


if __name__ == "__main__":
    unittest.main()
