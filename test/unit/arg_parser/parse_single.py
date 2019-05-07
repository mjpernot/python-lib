#!/usr/bin/python
# Classification (U)

"""Program:  parse_single.py

    Description:  Unit testing of _parse_single in arg_parser.py.

    Usage:
        test/unit/arg_parser/parse_single.py

    Arguments:
        None

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
import arg_parser
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_optvalset_arg_int -> Test opt_val_set set to integer value.
        test_optval_set -> Test with opt_val set with no value in arg.
        test_optvalset_two_arg -> Test with opt_val_set set to two arguments.
        test_optvalset_one_arg -> Test with opt_val_set set to one argument.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.argv = ["-c", "merge", "-d", "-M"]
        self.opt_val_list = ["-c", "-d", "-f", "-g"]
        self.opt_def_dict = {"-g": "def_val"}
        self.opt_val = ["-d"]

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_optvalset_arg_int(self, mock_int):

        """Function:  test_optvalset_arg_int

        Description:  Test with opt_val_set set to integer value.

        Arguments:
            None

        """

        mock_int.return_value = True

        self.argv = ["-c", "-1"]

        self.assertEqual(arg_parser._parse_single(self.argv, {},
                                                  self.opt_val_list, []),
                         (["-1"], {"-c": "-1"}))

    @mock.patch("arg_parser.gen_libs.chk_int")
    def test_optval_set(self, mock_int):

        """Function:  test_optval_set

        Description:  Test with opt_val set with no value in arg.

        Arguments:
            None

        """

        mock_int.return_value = False

        self.argv = ["-d"]

        self.assertEqual(arg_parser._parse_single(self.argv, {},
                                                  self.opt_val_list,
                                                  opt_val=self.opt_val),
                         (["-d"], {"-d": None}))

    def test_optvalset_two_arg(self):

        """Function:  test_optvalset_two_arg

        Description:  Test with opt_val_set set to two arguments.

        Arguments:
            None

        """

        self.argv = ["-c", "merge", "-d", "config"]

        self.assertEqual(arg_parser._parse_single(self.argv, {},
                                                  self.opt_val_list, []),
                         (["merge", "-d", "config"], {"-c": "merge"}))

    def test_optvalset_one_arg(self):

        """Function:  test_optvalset_one_arg

        Description:  Test with opt_val_set set to one argument.

        Arguments:
            None

        """

        self.argv = ["-c", "merge"]

        self.assertEqual(arg_parser._parse_single(self.argv, {},
                                                  self.opt_val_list, []),
                         (["merge"], {"-c": "merge"}))


if __name__ == "__main__":
    unittest.main()
