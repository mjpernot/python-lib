#!/usr/bin/python
# Classification (U)

"""Program:  argparser_parse_multi.py

    Description:  Unit testing of _parse_multi in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_parse_multi.py

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
import mock

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
        test_multilist_two_val
        test_multilist_one_val
        test_multilist_def_arg
        test_multilist_two_args
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

        self.opt_def = {"-g": "def_val"}

        self.results = ["file2"]
        self.resultsa = {"-f": ["file1", "file2"]}
        self.results2 = ["file2", "-M"]
        self.results3 = ["-g"]
        self.results3a = {"-g": "def_val"}
        self.results4 = ["file1"]
        self.results4a = {"-f": ["file1"]}

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_two_val(self, mock_int):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to two values.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results, self.resultsa))

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_one_val(self, mock_int):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv4)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results4, self.results4a))

    @mock.patch("arg_parser.arg_default")
    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_def_arg(self, mock_int, mock_def):

        """Function:  test_multilist_def_arg

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        mock_int.return_value = False
        mock_def.return_value = self.opt_def

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results3, self.results3a))

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_two_args(self, mock_int):

        """Function:  test_multilist_two_args

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv2)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results2, self.resultsa))

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_multilist_one_arg(self, mock_int):

        """Function:  test_multilist_one_arg

        Description:  Test with multi_list set to one argument.

        Arguments:

        """

        mock_int.return_value = False

        args_array = gen_class.ArgParser(self.argv)
        args_array.parse_multi()

        self.assertEqual((args_array.argv, args_array.args_array),
                         (self.results, self.resultsa))


if __name__ == "__main__":
    unittest.main()
