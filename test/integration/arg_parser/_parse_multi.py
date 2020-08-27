#!/usr/bin/python
# Classification (U)

"""Program:  _parse_multi.py

    Description:  Unit testing of _parse_multi in arg_parser.py.

    Usage:
        test/integration/arg_parser/_parse_multi.py

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
import arg_parser
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_multilist_two_val -> Test with multi_list set to two values.
        test_multilist_one_val -> Test with multi_list set to one value.
        test_multilist_def_arg -> Test with multi_list set to 1 arg using def.
        test_multilist_two_args -> Test multi_list set to 1 arg & 1 other arg.
        test_multilist_one_arg -> Test with multi_list set to one argument.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["-f", "file1", "file2"]
        self.opt_def_dict = {"-g": "def_val"}

    def test_multilist_two_val(self):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to two values.

        Arguments:

        """

        self.assertEqual(arg_parser._parse_multi(self.argv, {}, {}),
                         (["file2"], {"-f": ["file1", "file2"]}))

    def test_multilist_one_val(self):

        """Function:  test_multilist_one_val

        Description:  Test with multi_list set to one value.

        Arguments:

        """

        self.argv = ["-f", "file1"]

        self.assertEqual(arg_parser._parse_multi(self.argv, {}, {}),
                         (["file1"], {"-f": ["file1"]}))

    def test_multilist_def_arg(self):

        """Function:  test_multilist_def_arg

        Description:  Test with multi_list set to one arg using default.

        Arguments:

        """

        self.argv = ["-g"]

        self.assertEqual(arg_parser._parse_multi(self.argv, {},
                                                 self.opt_def_dict),
                         (["-g"], self.opt_def_dict))

    def test_multilist_two_args(self):

        """Function:  test_multilist_two_args

        Description:  Test with multi_list set to one arg and one other arg.

        Arguments:

        """

        self.argv = ["-f", "file1", "file2", "-M"]

        self.assertEqual(arg_parser._parse_multi(self.argv, {}, {}),
                         (["file2", "-M"], {"-f": ["file1", "file2"]}))

    def test_multilist_one_arg(self):

        """Function:  test_multilist_one_arg

        Description:  Test with multi_list set to one argument.

        Arguments:

        """

        self.assertEqual(arg_parser._parse_multi(self.argv, {}, {}),
                         (["file2"], {"-f": ["file1", "file2"]}))


if __name__ == "__main__":
    unittest.main()
