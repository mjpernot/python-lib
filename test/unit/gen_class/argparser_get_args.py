# Classification (U)

"""Program:  argparser_get_args.py

    Description:  Unit testing of get_args in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_get_args.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_empty_args_array
        test_get_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.opt_val = ["-a"]

        self.argv = ["program.py", "-a", "value", "-b"]
        self.argv2 = ["program.py"]

        self.results = {"-a": "value", "-b": True}
        self.results2 = {}

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with argument exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.get_args(), self.results2)

    def test_get_arg(self):

        """Function:  test_get_arg

        Description:  Test with argument exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.get_args(), self.results)


if __name__ == "__main__":
    unittest.main()
