#!/usr/bin/python
# Classification (U)

"""Program:  arg_default.py

    Description:  Unit testing of arg_default in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_default.py

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
import gen_libs
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
        test_empty_optdefdict -> Test adding two args from opt_req_list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = {}
        self.args_array2 = {"-c": "config"}

        self.opt_def_dict = {}
        self.opt_def_dict2 = {"-f": "file1"}
        self.opt_def_dict3 = {"-f": "file1", "-i": "sysmon"}

        self.arg = "-f"
        self.arg2 = "-i"

    @mock.patch("arg_parser.sys.exit")
    def test_empty_optdefdict(self, mock_exit):

        """Function:  test_empty_optdefdict

        Description:  Test with opt_def_dict being empty.

        Arguments:
            None

        """
        
        mock_exit.return_value = False

        self.assertFalse(arg_parser.arg_default(self.arg, self.args_array,
                                                self.opt_def_dict))


if __name__ == "__main__":
    unittest.main()
