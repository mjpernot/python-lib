# Classification (U)

"""Program:  argparser_arg_add_def.py

    Description:  Unit testing of arg_add_def in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_add_def.py

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
        test_both_override2
        test_both_override
        test_opt_req_override
        test_defaults_override
        test_opt_req_two_args2
        test_opt_req_two_args
        test_opt_req_zero_arg
        test_opt_req_one_arg
        test_args_array_only
        test_defaults_two_args
        test_defaults_one_arg
        test_empty_defaults

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py", "-f"]

        self.defaults = {}
        self.defaults2 = {"-n": "1"}
        self.defaults3 = {"-n": "1", "-i": "sysmon"}
        self.defaults4 = {"-n": "1", "-i": "sysmon", "-g": "no"}
        self.defaults5 = {"-a": 11}
        self.defaults6 = {"-n": "1", "-i": "sysmon", "-b": "no"}

        self.opt_req = []
        self.opt_req2 = ["-n"]
        self.opt_req3 = ["-m"]
        self.opt_req4 = ["-n", "-i"]
        self.opt_req5 = ["-i"]
        self.opt_req6 = ["-b"]
        self.opt_req7 = ["-b", "-i"]

        self.results = {"-f": True}
        self.results2 = {"-f": True, "-n": "1"}
        self.results3 = {"-f": True, "-n": "1", "-i": "sysmon"}
        self.results4 = {"-f": True, "-a": 11}
        self.results5 = {"-f": True, "-i": "sysmon"}
        self.results6 = {"-f": True, "-b": "no"}
        self.results7 = {"-f": True, "-b": "no", "-i": "sysmon"}

    def test_both_override2(self):

        """Function:  test_both_override2

        Description:  Test with passing in opt_req and defaults to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req2,
            do_parse=True)
        args_array.arg_add_def(defaults=self.defaults6, opt_req=self.opt_req7)

        self.assertEqual(args_array.args_array, self.results7)

    def test_both_override(self):

        """Function:  test_both_override

        Description:  Test with passing in opt_req and defaults to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req2,
            do_parse=True)
        args_array.arg_add_def(defaults=self.defaults6, opt_req=self.opt_req6)

        self.assertEqual(args_array.args_array, self.results6)

    def test_opt_req_override(self):

        """Function:  test_opt_req_override

        Description:  Test with passing in opt_req to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req2,
            do_parse=True)
        args_array.arg_add_def(opt_req=self.opt_req5)

        self.assertEqual(args_array.args_array, self.results5)

    def test_defaults_override(self):

        """Function:  test_defaults_override

        Description:  Test with passing in defaults to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults2, opt_req=self.opt_req,
            do_parse=True)
        args_array.arg_add_def(defaults=self.defaults5)

        self.assertEqual(args_array.args_array, self.results4)

    def test_opt_req_two_args2(self):

        """Function:  test_opt_req_two_args2

        Description:  Test with adding two args from opt_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults4, opt_req=self.opt_req4,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results3)

    def test_opt_req_two_args(self):

        """Function:  test_opt_req_two_args

        Description:  Test with adding two args from opt_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req4,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results3)

    def test_opt_req_zero_arg(self):

        """Function:  test_opt_req_zero_arg

        Description:  Test with adding zero args from opt_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req3,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results)

    def test_opt_req_one_arg(self):

        """Function:  test_opt_req_one_arg

        Description:  Test with adding one arg from opt_req.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req2,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results2)

    def test_args_array_only(self):

        """Function:  test_args_array_only

        Description:  Test with args_array only and no other attributes.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv, do_parse=True)

        self.assertEqual(args_array.args_array, self.results)

    def test_defaults_two_args(self):

        """Function:  test_defaults_two_args

        Description:  Test with adding two args from defaults.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults3, opt_req=self.opt_req,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results3)

    def test_defaults_one_arg(self):

        """Function:  test_defaults_one_arg

        Description:  Test with adding one arg from defaults.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults2, opt_req=self.opt_req,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results2)

    def test_empty_defaults(self):

        """Function:  test_empty_defaults

        Description:  Test with empty list for defaults.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, defaults=self.defaults, opt_req=self.opt_req,
            do_parse=True)
        args_array.arg_add_def()

        self.assertEqual(args_array.args_array, self.results)


if __name__ == "__main__":
    unittest.main()
