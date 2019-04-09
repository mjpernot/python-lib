#!/usr/bin/python
# Classification (U)

"""Program:  arg_file_chk.py

    Description:  Unit testing of arg_file_chk in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_file_chk.py

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

class FileOpen(object):

    """Class:  FileOpen

    Description:  Class stub holder for file open class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        close -> Stub holder for close function.

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:
            None

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_name_loop_zero_items -> Test with name loop on zero items.
        test_name_loop_two_items -> Test with name loop on two items.
        test_name_loop_one_item -> Test with name loop on one item.
        test_isinstance_is_set -> Test with isinstance against a set.
        test_isinstance_is_string -> Test with isinstance against a string.
        test_isinstance_is_list -> Test with isinstance against a list.
        test_two_match_between_sets -> Test with two matches between sets.
        test_one_match_between_sets -> Test with one match between sets.
        test_one_match_empty_list -> Test 1 match between sets but empty list.
        test_no_match_between_sets -> Test with no match between sets passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.file_chk_list = ["-f"]
        self.args_array = {"-f": ["test/file1"], "-m": "Marker"}
        self.open = FileOpen()

    @mock.patch("arg_parser.open")
    def test_name_loop_zero_items(self, mock_open):

        """Function:  test_name_loop_zero_items

        Description:  Test with name loop on zero items.

        Arguments:
            None

        """

        self.args_array = {"-f": [], "-m": "Marker"}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_name_loop_two_items(self, mock_open):

        """Function:  test_name_loop_two_items

        Description:  Test with name loop on two items.

        Arguments:
            None

        """

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_name_loop_one_item(self, mock_open):

        """Function:  test_name_loop_one_item

        Description:  Test with name loop on one item.

        Arguments:
            None

        """

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_isinstance_is_set(self, mock_open):

        """Function:  test_isinstance_is_set

        Description:  Test with isinstance against a set.

        Arguments:
            None

        """

        self.args_array = {"-f": {"test/file1"}, "-m": "Marker"}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_isinstance_is_string(self, mock_open):

        """Function:  test_isinstance_is_string

        Description:  Test with isinstance against a string.

        Arguments:
            None

        """

        self.args_array = {"-f": "test/file1", "-m": "Marker"}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_isinstance_is_list(self, mock_open):

        """Function:  test_isinstance_is_list

        Description:  Test with isinstance against a list.

        Arguments:
            None

        """

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_two_match_between_sets(self, mock_open):

        """Function:  test_two_match_between_sets

        Description:  Test with two matches between sets.

        Arguments:
            None

        """

        self.file_chk_list = ["-f", "-g"]
        self.args_array = {"-f": "test/file1", "-g": "test2/file2"}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_one_match_between_sets(self, mock_open):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets.

        Arguments:
            None

        """

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    def test_one_match_empty_list(self):

        """Function:  test_one_match_empty_list

        Description:  Test with one match between sets but empty list.

        Arguments:
            None

        """

        self.args_array = {"-f": [], "-m": "Marker"}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between sets passed.

        Arguments:
            None

        """

        self.file_chk_list = ["-a"]

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))


if __name__ == "__main__":
    unittest.main()
