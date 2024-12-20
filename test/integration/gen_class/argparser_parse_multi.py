# Classification (U)

"""Program:  argparser_parse_multi.py

    Description:  Integration testing of _parse_multi in
        gen_class.ArgParser class.

    Usage:
        test/integration/gen_class/argparser_parse_multi.py

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
        test_opt_def_override2
        test_opt_def_override
        test_opt_def_fail2
        test_opt_def_fail
        test_multilist_two_val2
        test_multilist_two_val
        test_multilist_one_val2
        test_multilist_one_val
        test_multilist_def_arg2
        test_multilist_def_arg
        test_multilist_two_args2
        test_multilist_two_args
        test_multilist_one_arg2
        test_multilist_one_arg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["-f", "file1", "file2"]
        self.argv2 = ["-f", "file1", "file2", "-M"]
        self.argv3 = ["-g"]
        self.argv4 = ["-f", "file1"]

        self.opt_def = {"-g": ["def_val"]}
        self.opt_def2 = {"-h": ["def_val"]}

        self.results = ["file2"]
        self.resultsa = {"-f": ["file1", "file2"]}
        self.results2 = ["file2", "-M"]
        self.results3 = ["-g"]
        self.results3a = {"-g": ["def_val"]}
        self.results4 = ["file1"]
        self.results4a = {"-f": ["file1"]}
        self.results5a = {}

    def test_opt_def_override2(self):

        """Function:  test_opt_def_override2

        Description:  Test with opt_def passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def2)

        self.assertTrue(args_array.parse_multi(opt_def=self.opt_def))

    def test_opt_def_override(self):

        """Function:  test_opt_def_override

        Description:  Test with opt_def passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def2)
        args_array.parse_multi(opt_def=self.opt_def)

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results3, self.results3a))

    def test_opt_def_fail2(self):

        """Function:  test_opt_def_fail2

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def2)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.parse_multi())

    def test_opt_def_fail(self):

        """Function:  test_opt_def_fail

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def2)

        with gen_libs.no_std_out():
            args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results3, self.results5a))

    def test_multilist_two_val2(self):

        """Function:  test_multilist_one_val2

        Description:  Test with multi_list set to two values.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv)

        self.assertTrue(args_array.parse_multi())

    def test_multilist_two_val(self):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to two values.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results, self.resultsa))

    def test_multilist_one_val2(self):

        """Function:  test_multilist_one_val2

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv4)

        self.assertTrue(args_array.parse_multi())

    def test_multilist_one_val(self):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv4)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results4, self.results4a))

    def test_multilist_def_arg2(self):

        """Function:  test_multilist_def_arg2

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def)

        self.assertTrue(args_array.parse_multi())

    def test_multilist_def_arg(self):

        """Function:  test_multilist_def_arg

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results3, self.results3a))

    def test_multilist_two_args2(self):

        """Function:  test_multilist_two_args2

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2)

        self.assertTrue(args_array.parse_multi())

    def test_multilist_two_args(self):

        """Function:  test_multilist_two_args

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results2, self.resultsa))

    def test_multilist_one_arg2(self):

        """Function:  test_multilist_one_arg2

        Description:  Test with multi_list set to one argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv)

        self.assertTrue(args_array.parse_multi())

    def test_multilist_one_arg(self):

        """Function:  test_multilist_one_arg

        Description:  Test with multi_list set to one argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results, self.resultsa))


if __name__ == "__main__":
    unittest.main()
