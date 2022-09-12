# Classification (U)

"""Program:  argparser_arg_req_or_lst.py

    Description:  Unit testing of arg_req_or_lst in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_req_or_lst.py

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
        test_opt_or_override
        test_multiple_miss2
        test_multiple_miss
        test_multiple_mix
        test_multiple_lists
        test_multiple_keys
        test_missing_option
        test_both_present
        test_list_only
        test_key_only
        test_empty_args_array
        test_empty_opt_or
        test_both_empty

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
        self.argv4 = [p_name, "-b", "-c"]
        self.argv5 = [p_name, "-a", "-d"]
        self.argv6 = [p_name, "-c", "-e"]
        self.argv7 = [p_name, "-d", "-e"]
        self.argv8 = [p_name, "-a", "-e"]
        self.argv9 = [p_name, "-e"]

        self.opt_or = {}
        self.opt_or2 = {"-a": ["-b"]}
        self.opt_or3 = {"-a": ["-b", "-c"], "-d": ["-e"]}

    def test_opt_or_override(self):

        """Function:  test_opt_or_override

        Description:  Test with opt_or passed in to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_or=self.opt_or3, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst(opt_or=self.opt_or))

    def test_multiple_miss2(self):

        """Function:  test_multiple_miss2

        Description:  Test with multiple keys with one not present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv9, opt_or=self.opt_or3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_req_or_lst())

    def test_multiple_miss(self):

        """Function:  test_multiple_miss

        Description:  Test with multiple keys with one not present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_or=self.opt_or3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_req_or_lst())

    def test_multiple_mix(self):

        """Function:  test_multiple_mix

        Description:  Test with multiple key/list present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv8, opt_or=self.opt_or3, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_multiple_lists(self):

        """Function:  test_multiple_lists

        Description:  Test with multiple lists present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv6, opt_or=self.opt_or3, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_multiple_keys(self):

        """Function:  test_multiple_keys

        Description:  Test with multiple keys present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv5, opt_or=self.opt_or3, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_missing_option(self):

        """Function:  test_missing_option

        Description:  Test with both key and list options not present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv7, opt_or=self.opt_or2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_req_or_lst())

    def test_both_present(self):

        """Function:  test_both_present

        Description:  Test with both key and list options present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_or=self.opt_or2, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_list_only(self):

        """Function:  test_list_only

        Description:  Test with list option present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv4, opt_or=self.opt_or2, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_key_only(self):

        """Function:  test_key_only

        Description:  Test with key option present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_or=self.opt_or2, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_or=self.opt_or2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_req_or_lst())

    def test_empty_opt_or(self):

        """Function:  test_empty_opt_or

        Description:  Test with empty list for opt_or.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_or=self.opt_or, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())

    def test_both_empty(self):

        """Function:  test_both_empty

        Description:  Test with both args with empty sets.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_or=self.opt_or, do_parse=True)

        self.assertTrue(args_array.arg_req_or_lst())


if __name__ == "__main__":
    unittest.main()
