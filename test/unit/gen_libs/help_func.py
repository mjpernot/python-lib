#!/usr/bin/python
# Classification (U)

"""Program:  help_func.py

    Description:  Unit testing of help_func in gen_libs.py.

    Usage:
        test/unit/gen_libs/help_func.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


def holder():

    """Function:  holder

    Description:  Stub holder for func_name in help_func.

    Arguments:

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_help_option -> Test with -h option.
        test_version_option -> Test with -v option.
        test_both_options -> Test with -h and -v options.
        test_no_options -> Test with no -h or -v options in array.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {}
        self.args_array2 = {"-h": True}
        self.args_array3 = {"-v": True}
        self.args_array4 = {"-v": True, "-h": True}
        self.version = "1.0.0"
        self.func_name = holder

    def test_help_option(self):

        """Function:  test_help_option

        Description:  Test with -h option.

        Arguments:

        """

        self.assertTrue(gen_libs.help_func(self.args_array2, self.version,
                                           self.func_name))

    def test_version_option(self):

        """Function:  test_version_option

        Description:  Test with -v option.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(gen_libs.help_func(self.args_array3, self.version,
                                               self.func_name))

    def test_both_options(self):

        """Function:  test_both_options

        Description:  Test with -h and -v options.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(gen_libs.help_func(self.args_array4, self.version,
                                               self.func_name))

    def test_no_options(self):

        """Function:  test_no_options

        Description:  Test with no -h or -v options in array.

        Arguments:

        """

        self.assertFalse(gen_libs.help_func(self.args_array, self.version,
                                            self.func_name))


if __name__ == "__main__":
    unittest.main()
