#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_exist.py

    Description:  Unit testing of arg_exist in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_exist.py

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
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-a"]
        self.argv3 = ["program.py", "-a", "-b"]

        self.arg = "-a"
        self.arg2 = "-b"
        self.arg3 = "-c"

    def test_empty_args_array(self):

        """Function:  test_empty_arg_sarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv, do_parse=True)

        self.assertFalse(args_array.arg_exist(self.arg))


if __name__ == "__main__":
    unittest.main()
