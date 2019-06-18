#!/usr/bin/python
# Classification (U)

"""Program:  arg_set_path.py

    Description:  Unit testing of arg_set_path in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_set_path.py

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
import arg_parser
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_arg_not_present -> Test with argument not present.
        test_arg_present -> Test with argument present.
        test_empty_both -> Test with both args empty.
        test_empty_argopt -> Test with empty string for arg_opt.
        test_empty_argsarray -> Test with empty dictionary for args_array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-a": "/dir/path", "-c": "/dir/diff_path"}

        self.arg_opt = None
        self.arg_opt2 = "-a"
        self.arg_opt3 = "-b"

        self.ret = ""
        self.ret2 = "/dir/path/"

    def test_arg_not_present(self):

        """Function:  test_arg_not_present

        Description:  Test with argument not present.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_set_path(self.args_array2,
                                                 self.arg_opt3), self.ret)

    def test_arg_present(self):

        """Function:  test_arg_present

        Description:  Test with argument present.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_set_path(self.args_array2,
                                                 self.arg_opt2), self.ret2)

    def test_empty_both(self):

        """Function:  test_empty_both

        Description:  Test with both args empty.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_set_path(self.args_array2,
                                                 self.arg_opt), self.ret)

    def test_empty_argopt(self):

        """Function:  test_empty_argopt

        Description:  Test with empty string for arg_opt.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_set_path(self.args_array2,
                                                 self.arg_opt), self.ret)

    def test_empty_argsarray(self):

        """Function:  test_empty_argsarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_set_path(self.args_array,
                                                 self.arg_opt2), self.ret)


if __name__ == "__main__":
    unittest.main()
