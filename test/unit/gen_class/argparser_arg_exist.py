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
import unittest

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
        test_arg_not_exist2
        test_arg_not_exist
        test_arg_exist2
        test_arg_exist
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        self.argv = [p_name]
        self.argv2 = [p_name, "-a"]
        self.argv3 = [p_name, "-a", "-b"]

        self.arg = "-a"
        self.arg2 = "-b"
        self.arg3 = "-c"

    def test_arg_not_exist2(self):

        """Function:  test_arg_not_exist2

        Description:  Test with argument does not exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, do_parse=True)

        self.assertFalse(args_array.arg_exist(self.arg3))

    def test_arg_not_exist(self):

        """Function:  test_arg_not_exist

        Description:  Test with argument does not exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, do_parse=True)

        self.assertFalse(args_array.arg_exist(self.arg2))

    def test_arg_exist2(self):

        """Function:  test_arg_exist2

        Description:  Test with argument exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, do_parse=True)

        self.assertTrue(args_array.arg_exist(self.arg))

    def test_arg_exist(self):

        """Function:  test_arg_exist

        Description:  Test with argument exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, do_parse=True)

        self.assertTrue(args_array.arg_exist(self.arg))

    def test_empty_args_array(self):

        """Function:  test_empty_arg_sarray

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv, do_parse=True)

        self.assertFalse(args_array.arg_exist(self.arg))


if __name__ == "__main__":
    unittest.main()
