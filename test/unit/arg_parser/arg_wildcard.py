#!/usr/bin/python
# Classification (U)

"""Program:  arg_wildcard.py

    Description:  Unit testing of arg_wildcard in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_wildcard.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_two_wildcard -> Test with two wildcard returns.
        test_one_wildcard -> Test with one wildcard return.
        test_empty_optwildcard -> Test with empty list for opt_wildcard.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.value = "value*"
        self.test = "test*"
        self.args_array = {}
        self.args_array2 = {self.value: []}
        self.args_array3 = {self.value: [], self.test: []}

        self.opt_wildcard = []
        self.opt_wildcard2 = [self.value]
        self.opt_wildcard3 = [self.value, self.test]

        self.test_array = {}
        self.test_array2 = {self.value: ["value1", "value2"]}
        self.test_array3 = {self.value: ["value1", "value2"],
                            self.test: ["test2"]}

    @mock.patch("arg_parser.glob")
    def test_two_wildcard(self, mock_glob):

        """Function:  test_two_wildcard

        Description:  Test with two wildcard returns.

        Arguments:

        """

        mock_glob.glob.side_effect = [["value1", "value2"], ["test2"]]

        self.assertEqual(arg_parser.arg_wildcard(self.args_array3,
                                                 self.opt_wildcard3),
                         self.test_array3)

    @mock.patch("arg_parser.glob")
    def test_one_wildcard(self, mock_glob):

        """Function:  test_one_wildcard

        Description:  Test with one wildcard return.

        Arguments:

        """

        mock_glob.glob.return_value = ["value1", "value2"]

        self.assertEqual(arg_parser.arg_wildcard(self.args_array2,
                                                 self.opt_wildcard2),
                         self.test_array2)

    def test_empty_optwildcard(self):

        """Function:  test_empty_optwildcard

        Description:  Test with empty list for opt_wildcard.

        Arguments:

        """

        self.assertEqual(arg_parser.arg_wildcard(self.args_array,
                                                 self.opt_wildcard),
                         self.test_array)


if __name__ == "__main__":
    unittest.main()
