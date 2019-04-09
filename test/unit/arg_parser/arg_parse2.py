#!/usr/bin/python
# Classification (U)

"""Program:  arg_parse2.py

    Description:  Unit testing of arg_parse2 in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_parse2.py

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

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.argv = []
        self.opt_val_list = []
        self.opt_def_dict = None
        self.multi_list = []
        self.opt_val = []

    def test_second_open_no_error(self):

        """Function:  test_second_open_no_error

        Description:  Test with second open no error.

        Arguments:
            None

        """

        self.assertEqual(arg_parser.arg_parse2(self.argv, self.opt_val_list))



if __name__ == "__main__":
    unittest.main()
