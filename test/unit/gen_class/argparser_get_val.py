# Classification (U)

"""Program:  argparser_get_val.py

    Description:  Unit testing of get_val in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_get_val.py

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
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_passed_empty_string
        test_passed_tuple
        test_passed_dict
        test_passed_list
        test_passed_default
        test_default_value
        test_arg_not_exist
        test_get_val2
        test_get_val

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.opt_val = ["-a"]

        self.argv = ["program.py", "-a", "value", "-b"]

        self.key = "-a"
        self.key2 = "-c"
        self.key3 = "-b"

        self.def_val = "default_val"
        self.def_val2 = [1, 2, 3]
        self.def_val3 = {"key1": "value"}
        self.def_val4 = ("a", "b", "c")
        self.def_val5 = ""

        self.results = "value"
        self.results2 = "default_val"
        self.results3 = [1, 2, 3]
        self.results4 = {"key1": "value"}
        self.results5 = ("a", "b", "c")
        self.results6 = ""

    def test_passed_empty_string(self):

        """Function:  test_passed_empty_string

        Description:  Test with passed empty string return.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.get_val(
                self.key2, def_val=self.def_val5), self.results6)

    def test_passed_tuple(self):

        """Function:  test_passed_tuple

        Description:  Test with passed tuple return.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.get_val(
                self.key2, def_val=self.def_val4), self.results5)

    def test_passed_dict(self):

        """Function:  test_passed_dict

        Description:  Test with passed dictionary return.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.get_val(
                self.key2, def_val=self.def_val3), self.results4)

    def test_passed_list(self):

        """Function:  test_passed_list

        Description:  Test with passed list return.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.get_val(
                self.key2, def_val=self.def_val2), self.results3)

    def test_passed_default(self):

        """Function:  test_passed_default

        Description:  Test with passed default return.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.get_val(self.key2, def_val=self.def_val), self.results2)

    def test_default_value(self):

        """Function:  test_default_value

        Description:  Test with default return.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertIsNone(args_array.get_val(self.key2))

    def test_arg_not_exist(self):

        """Function:  test_arg_not_exist

        Description:  Test with argument does not exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertIsNone(args_array.get_val(self.key2))

    def test_get_val2(self):

        """Function:  test_get_val2

        Description:  Test with argument exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertTrue(args_array.get_val(self.key3))

    def test_get_val(self):

        """Function:  test_get_val

        Description:  Test with argument exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.get_val(self.key), self.results)


if __name__ == "__main__":
    unittest.main()
