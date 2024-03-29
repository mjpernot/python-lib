# Classification (U)

"""Program:  arg_default.py

    Description:  Unit testing of arg_default in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_default.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

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
        test_arg_in_argsarray
        test_arg_in_optdefdict
        test_not_in_optdefdict
        test_empty_optdefdict

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "config"}
        self.args_array2 = {"-c": "config", "-f": "new_file"}
        self.results = {"-c": "config", "-f": "file1"}
        self.opt_def_dict = {}
        self.opt_def_dict2 = {"-f": "file1", "-i": "sysmon"}
        self.arg = "-f"
        self.arg2 = "-g"

    def test_arg_in_argsarray(self):

        """Function:  test_arg_in_argsarray

        Description:  Test with arg already in args_array.

        Note:  arg_default will overwrite an existing value if one is present.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_default(
            self.arg, self.args_array2, self.opt_def_dict2), self.results)

    def test_arg_in_optdefdict(self):

        """Function:  test_arg_in_optdefdict

        Description:  Test with arg in opt_def_dict.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_default(
            self.arg, self.args_array, self.opt_def_dict2), self.results)

    @mock.patch("arg_parser.sys.exit")
    def test_not_in_optdefdict(self, mock_exit):

        """Function:  test_not_in_optdefdict

        Description:  Test with arg not in opt_def_dict.

        Arguments:

        """

        mock_exit.return_value = False

        self.assertFalse(arg_parser.arg_default(self.arg2, self.args_array,
                                                self.opt_def_dict2))

    @mock.patch("arg_parser.sys.exit")
    def test_empty_optdefdict(self, mock_exit):

        """Function:  test_empty_optdefdict

        Description:  Test with opt_def_dict being empty.

        Arguments:

        """

        mock_exit.return_value = False

        self.assertFalse(arg_parser.arg_default(self.arg, self.args_array,
                                                self.opt_def_dict))


if __name__ == "__main__":
    unittest.main()
