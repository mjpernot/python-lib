# Classification (U)

"""Program:  argparser_parse_single.py

    Description:  Integration testing of _parse_single in
        gen_class.ArgParser class.

    Usage:
        test/integration/gen_class/argparser_parse_single.py

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
        test_opt_val_bin_override2
        test_opt_val_bin_override
        test_opt_def_override2
        test_opt_def_override
        test_opt_def2
        test_opt_def
        test_opt_val_arg_int2
        test_opt_val_arg_int
        test_opt_val2
        test_opt_val
        test_opt_val_two_arg2
        test_opt_val_two_arg
        test_opt_val_one_arg2
        test_opt_val_one_arg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["-c", "merge", "-d", "-M"]
        self.argv2 = ["-c", "merge"]
        self.argv3 = ["-c", "merge", "-d", "config"]
        self.argv4 = ["-d"]
        self.argv5 = ["-c", "-1"]
        self.argv6 = ["-g"]

        self.opt_val = ["-c", "-d", "-f", "-g"]

        self.opt_def = {"-g": "def_val"}
        self.opt_def2 = {"-h": "def_val"}

        self.opt_val_bin = ["-d"]
        self.opt_val_bin2 = ["-a"]

        self.results = ["merge"]
        self.resultsa = {"-c": "merge"}
        self.results2 = ["merge", "-d", "config"]
        self.results3 = ["-d"]
        self.results3a = {"-d": None}
        self.results4 = ["-1"]
        self.results4a = {"-c": "-1"}
        self.results5 = ["-g"]
        self.results5a = {"-g": "def_val"}
        self.results6a = {}

    def test_opt_val_bin_override2(self):

        """Function:  test_opt_val_bin_override2

        Description:  Test with opt_val_bin passed in as override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, opt_val_bin=self.opt_val_bin2)

        self.assertTrue(args_array.parse_single(opt_val_bin=self.opt_val_bin))

    def test_opt_val_bin_override(self):

        """Function:  test_opt_val_bin_override2

        Description:  Test with opt_val_bin passed in as override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, opt_val_bin=self.opt_val_bin2)
        args_array.parse_single(opt_val_bin=self.opt_val_bin)

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results3, self.results3a))

    def test_opt_def_override2(self):

        """Function:  test_opt_def_override2

        Description:  Test with opt_def passed in as an override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_def=self.opt_def2)

        self.assertTrue(args_array.parse_single(opt_def=self.opt_def))

    def test_opt_def_override(self):

        """Function:  test_opt_def_override

        Description:  Test with opt_def passed in as an override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_def=self.opt_def2)

        args_array.parse_single(opt_def=self.opt_def)

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results5, self.results5a))

    def test_opt_def_fail2(self):

        """Function:  test_opt_def_fail2

        Description:  Test with opt_def set.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_def=self.opt_def2)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.parse_single())

    def test_opt_def_fail(self):

        """Function:  test_opt_def_fail

        Description:  Test with opt_def set.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_def=self.opt_def2)

        with gen_libs.no_std_out():
            args_array.parse_single()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results5, self.results6a))

    def test_opt_def2(self):

        """Function:  test_opt_def2

        Description:  Test with opt_def set.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_def=self.opt_def)
        self.assertTrue(args_array.parse_single())

    def test_opt_def(self):

        """Function:  test_opt_def

        Description:  Test with opt_def set.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_def=self.opt_def)
        args_array.parse_single()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results5, self.results5a))

    def test_opt_val_arg_int2(self):

        """Function:  test_opt_val_arg_int2

        Description:  Test with opt_val set to integer value.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv5, opt_val=self.opt_val)

        self.assertTrue(args_array.parse_single())

    def test_opt_val_arg_int(self):

        """Function:  test_opt_val_arg_int

        Description:  Test with opt_val set to integer value.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv5, opt_val=self.opt_val)
        args_array.parse_single()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results4, self.results4a))

    def test_opt_val2(self):

        """Function:  test_opt_val2

        Description:  Test with opt_val set with no value in arg.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, opt_val_bin=self.opt_val_bin)

        self.assertTrue(args_array.parse_single())

    def test_opt_val(self):

        """Function:  test_opt_val

        Description:  Test with opt_val set with no value in arg.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, opt_val_bin=self.opt_val_bin)
        args_array.parse_single()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results3, self.results3a))

    def test_opt_val_two_arg2(self):

        """Function:  test_opt_val_two_arg2

        Description:  Test with opt_val set to two arguments.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_val=self.opt_val)

        self.assertTrue(args_array.parse_single())

    def test_opt_val_two_arg(self):

        """Function:  test_opt_val_two_arg

        Description:  Test with opt_val set to two arguments.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_val=self.opt_val)
        args_array.parse_single()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results2, self.resultsa))

    def test_opt_val_one_arg2(self):

        """Function:  test_opt_val_one_arg2

        Description:  Test with opt_val set to one argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, opt_val=self.opt_val)

        self.assertTrue(args_array.parse_single())

    def test_opt_val_one_arg(self):

        """Function:  test_opt_val_one_arg

        Description:  Test with opt_val set to one argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, opt_val=self.opt_val)
        args_array.parse_single()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results, self.resultsa))


if __name__ == "__main__":
    unittest.main()
