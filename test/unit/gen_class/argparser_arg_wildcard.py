# Classification (U)

"""Program:  argparser_arg_wildcard.py

    Description:  Unit testing of arg_wildcard in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_wildcard.py

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
        test_opt_wildcard_override
        test_two_string_wildcard
        test_str_list_wildcard
        test_string_wildcard
        test_two_wildcard2
        test_two_wildcard
        test_one_wildcard2
        test_one_wildcard
        test_empty_opt_wildcard

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        base_dir = "./test/unit/gen_class"
        wild1 = os.path.join(base_dir, "argparser_arg_wild*")
        wild2 = os.path.join(base_dir, "unit*")
        file1 = os.path.join(base_dir, "argparser_arg_wildcard.py")
        file2 = os.path.join(base_dir, "unit_test_run.sh")
        file3 = os.path.join(base_dir, "unit_test_run3.sh")

        self.argv = [p_name]
        self.argv2 = [p_name, "-a", [wild1]]
        self.argv3 = [p_name, "-a", [wild1], "-b", [wild2]]
        self.argv4 = [p_name, "-a", [wild1, wild2]]
        self.argv5 = [p_name, "-a", [wild1, wild2], "-b", [wild2]]
        self.argv6 = [p_name, "-a", wild1]
        self.argv7 = [p_name, "-a", wild1, "-b", [wild2]]
        self.argv8 = [p_name, "-a", wild1, "-b", wild2]

        self.opt_val = ["-a", "-b"]

        self.opt_wildcard = []
        self.opt_wildcard2 = ["-a"]
        self.opt_wildcard3 = ["-a", "-b"]

        self.results = {}
        self.results2 = {"-a": [file1]}
        self.results3 = {"-a": [file1], "-b": [file2, file3]}
        self.results3["-b"].sort()
        self.results4 = {"-a": [file1, file2, file3]}
        self.results4["-a"].sort()
        self.results5 = {"-a": [file1, file2, file3], "-b": [file2, file3]}
        self.results5["-a"].sort()
        self.results5["-b"].sort()

    def test_opt_wildcard_override(self):

        """Function:  test_opt_wildcard_override

        Description:  Test with opt_wildcard passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv7, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard2,
            do_parse=True)
        args_array.arg_wildcard(opt_wildcard=self.opt_wildcard3)
        args_array.args_array["-b"].sort()

        self.assertEqual(args_array.args_array, self.results3)

    def test_two_string_wildcard(self):

        """Function:  test_two_string_wildcard

        Description:  Test with two string wildcards.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv8, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard3,
            do_parse=True)
        args_array.arg_wildcard()
        args_array.args_array["-b"].sort()

        self.assertEqual(args_array.args_array, self.results3)

    def test_str_list_wildcard(self):

        """Function:  test_str_list_wildcard

        Description:  Test with string and list wildcard.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv7, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard3,
            do_parse=True)
        args_array.arg_wildcard()
        args_array.args_array["-b"].sort()

        self.assertEqual(args_array.args_array, self.results3)

    def test_string_wildcard(self):

        """Function:  test_string_wildcard

        Description:  Test with a string wildcard.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard2,
            do_parse=True)
        args_array.arg_wildcard()

        self.assertEqual(args_array.args_array, self.results2)

    def test_two_wildcard2(self):

        """Function:  test_two_wildcard2

        Description:  Test with two wildcards.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard3,
            do_parse=True)
        args_array.arg_wildcard()

        self.assertEqual(
            args_array.args_array["-a"].sort(),
            self.results5["-a"].sort() and args_array.args_array["-b"].sort(),
            self.results5["-b"].sort())

    def test_two_wildcard(self):

        """Function:  test_two_wildcard

        Description:  Test with two wildcards.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard3,
            do_parse=True)
        args_array.arg_wildcard()
        args_array.args_array["-b"].sort()

        self.assertEqual(args_array.args_array, self.results3)

    def test_one_wildcard2(self):

        """Function:  test_one_wildcard2

        Description:  Test with one wildcard.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard2,
            do_parse=True)
        args_array.arg_wildcard()

        self.assertEqual(
            args_array.args_array["-a"].sort(), self.results4["-a"].sort())

    def test_one_wildcard(self):

        """Function:  test_one_wildcard

        Description:  Test with one wildcard.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard2,
            do_parse=True)
        args_array.arg_wildcard()

        self.assertEqual(args_array.args_array, self.results2)

    def test_empty_opt_wildcard(self):

        """Function:  test_empty_opt_wildcard

        Description:  Test with empty list for opt_wildcard.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, opt_wildcard=self.opt_wildcard,
            do_parse=True)
        args_array.arg_wildcard()

        self.assertEqual(args_array.args_array, self.results)


if __name__ == "__main__":
    unittest.main()
