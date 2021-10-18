#!/usr/bin/python
# Classification (U)

"""Program:  arg_wildcard.py

    Description:  Unit testing of arg_wildcard in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_wildcard.py

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
import arg_parser
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_two_string_wildcard
        test_str_list_wildcard
        test_string_wildcard
        test_two_wildcard2
        test_two_wildcard
        test_one_wildcard2
        test_one_wildcard
        test_empty_optwildcard

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        base_dir = "./test/unit/arg_parser"
        wild1 = os.path.join(base_dir, "arg_wild*")
        wild2 = os.path.join(base_dir, "unit*")
        file1 = os.path.join(base_dir, "arg_wildcard.py")
        file2 = os.path.join(base_dir, "unit_test_run.sh")

        self.args_array = {}
        self.args_array2 = {"-a": [wild1]}
        self.args_array3 = {"-a": [wild1], "-b": [wild2]}
        self.args_array4 = {"-a": [wild1, wild2]}
        self.args_array5 = {"-a": [wild1, wild2], "-b": [wild2]}
        self.args_array6 = {"-a": wild1}
        self.args_array7 = {"-a": wild1, "-b": [wild2]}
        self.args_array8 = {"-a": wild1, "-b": wild2}

        self.opt_wildcard = []
        self.opt_wildcard2 = ["-a"]
        self.opt_wildcard3 = ["-a", "-b"]

        self.test_array = {}
        self.test_array2 = {"-a": [file1]}
        self.test_array3 = {"-a": [file1], "-b": [file2]}
        self.test_array4 = {"-a": [file1, file2]}
        self.test_array5 = {"-a": [file1, file2], "-b": [file2]}

    def test_two_string_wildcard(self):

        """Function:  test_two_string_wildcard

        Description:  Test with two string wildcards.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array8, self.opt_wildcard3)

        self.assertEqual(n_array, self.test_array3)

    def test_str_list_wildcard(self):

        """Function:  test_str_list_wildcard

        Description:  Test with string and list wildcard.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array7, self.opt_wildcard3)

        self.assertEqual(n_array, self.test_array3)

    def test_string_wildcard(self):

        """Function:  test_string_wildcard

        Description:  Test with a string wildcard.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array6, self.opt_wildcard2)

        self.assertEqual(n_array, self.test_array2)

    def test_two_wildcard2(self):

        """Function:  test_two_wildcard2

        Description:  Test with two wildcards.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array5, self.opt_wildcard3)

        self.assertEqual(
            n_array["-a"].sort(),
            self.test_array5["-a"].sort() and n_array["-b"],
            self.test_array5["-b"])

    def test_two_wildcard(self):

        """Function:  test_two_wildcard

        Description:  Test with two wildcards.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array3, self.opt_wildcard3)

        self.assertEqual(n_array, self.test_array3)

    def test_one_wildcard2(self):

        """Function:  test_one_wildcard2

        Description:  Test with one wildcard.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array4, self.opt_wildcard2)

        self.assertEqual(n_array["-a"].sort(), self.test_array4["-a"].sort())

    def test_one_wildcard(self):

        """Function:  test_one_wildcard

        Description:  Test with one wildcard.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array2, self.opt_wildcard2)

        self.assertEqual(n_array, self.test_array2)

    def test_empty_optwildcard(self):

        """Function:  test_empty_optwildcard

        Description:  Test with empty list for opt_wildcard.

        Arguments:

        """

        n_array = arg_parser.arg_wildcard(self.args_array, self.opt_wildcard)

        self.assertEqual(n_array, self.test_array)


if __name__ == "__main__":
    unittest.main()
