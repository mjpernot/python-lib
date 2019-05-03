#!/usr/bin/python
# Classification (U)

"""Program:  arg_dir_chk_crt.py

    Description:  Unit testing of arg_dir_chk_crt in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_dir_chk_crt.py

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
        test_second_open_no_error -> Test with second open no error.
        test_second_open_error -> Test with second open but returns error.
        test_filecrtlist_in_list -> Test file_crt_list with option in list.
        test_filecrtlist_not_in_list -> Test file_crt_list option not in list.
        test_filecrtlist_empty_list -> Test file_crt_list passed empty list.
        test_filecrtlist_not_passed -> Test file_crt_list not being passed.
        test_first_open_error_two -> Test with first open & error 2 returned.
        test_first_open_error_ten -> Test with first open & error 10 returned.
        test_first_open_no_errors -> Test with first open and no errors.
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

        test_empty_dirchklist -> Test with dir_chk_list is empty.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args_array = {}
        self.args_array2 = {"-f": ["/test_path/dir1"]}
        self.args_array3 = {}

        self.dir_chk_list = []
        self.dir_chk_list2 = []
        self.dir_chk_list3 = []

        self.dir_crt_list = []
        self.dir_crt_list2 = ["-f"]

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_second_open_no_error(self, mock_open, mock_crt):

        """Function:  test_second_open_no_error

        Description:  Test with second open no error.

        Arguments:
            None

        """

        mock_open.side_effect = [self.open3, self.open]
        mock_crt.return_value = False

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list,
                                                 self.file_crt_list))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_second_open_error(self, mock_open, mock_crt):

        """Function:  test_second_open_error

        Description:  Test with second open but returns error.

        Arguments:
            None

        """

        mock_open.side_effect = [self.open3, self.open2]
        mock_crt.return_value = True

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.file_chk_list,
                                                    self.file_crt_list))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_filecrtlist_in_list(self, mock_open, mock_crt):

        """Function:  test_filecrtlist_in_list

        Description:  Test with file_crt_list with option in list.

        Arguments:
            None

        """

        mock_open.side_effect = [self.open3, self.open]
        mock_crt.return_value = False

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list,
                                                 self.file_crt_list))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_filecrtlist_not_in_list(self, mock_open, mock_crt):

        """Function:  test_filecrtlist_not_in_list

        Description:  Test with file_crt_list with option not in list.

        Arguments:
            None

        """

        mock_open.return_value = self.open3
        mock_crt.return_value = True

        self.file_crt_list = ["-g"]

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.file_chk_list,
                                                    self.file_crt_list))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_filecrtlist_empty_list(self, mock_open, mock_crt):

        """Function:  test_filecrtlist_empty_list

        Description:  Test with file_crt_list passed with empty list.

        Arguments:
            None

        """

        mock_open.return_value = self.open3
        mock_crt.return_value = True

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.file_chk_list, []))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_filecrtlist_not_passed(self, mock_open, mock_crt):

        """Function:  test_filecrtlist_not_passed

        Description:  Test with file_crt_list not being passed.

        Arguments:
            None

        """

        mock_open.return_value = self.open3
        mock_crt.return_value = True

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.file_chk_list))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_first_open_error_two(self, mock_open, mock_crt):

        """Function:  test_first_open_error_two

        Description:  Test with first open and error 2 returned.

        Arguments:
            None

        """

        mock_open.side_effect = [self.open3, self.open]
        mock_crt.return_value = False

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list,
                                                 self.file_crt_list))

    @mock.patch("arg_parser._file_create")
    @mock.patch("arg_parser.open")
    def test_first_open_error_ten(self, mock_open, mock_crt):

        """Function:  test_first_open_error_ten

        Description:  Test with first open and error 10 returned.

        Arguments:
            None

        """

        mock_open.return_value = self.open2
        mock_crt.return_value = True

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_first_open_no_errors(self, mock_open):

        """Function:  test_first_open_no_errors

        Description:  Test with first open and no errors.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    def test_name_loop_zero_items(self):

        """Function:  test_name_loop_zero_items

        Description:  Test with name loop on zero items.

        Arguments:
            None

        """

        self.args_array = {"-f": [], "-m": "Marker"}

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_name_loop_two_items(self, mock_open):

        """Function:  test_name_loop_two_items

        Description:  Test with name loop on two items.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_name_loop_one_item(self, mock_open):

        """Function:  test_name_loop_one_item

        Description:  Test with name loop on one item.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_isinstance_is_set(self, mock_open):

        """Function:  test_isinstance_is_set

        Description:  Test with isinstance against a set.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.args_array = {"-f": {"test/file1"}, "-m": "Marker"}

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_isinstance_is_string(self, mock_open):

        """Function:  test_isinstance_is_string

        Description:  Test with isinstance against a string.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.args_array = {"-f": "test/file1", "-m": "Marker"}

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_isinstance_is_list(self, mock_open):

        """Function:  test_isinstance_is_list

        Description:  Test with isinstance against a list.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_two_match_between_sets(self, mock_open):

        """Function:  test_two_match_between_sets

        Description:  Test with two matches between sets.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.file_chk_list = ["-f", "-g"]
        self.args_array = {"-f": "test/file1", "-g": "test2/file2"}

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    @mock.patch("arg_parser.open")
    def test_one_match_between_sets(self, mock_open):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets.

        Arguments:
            None

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    def test_one_match_empty_list(self):

        """Function:  test_one_match_empty_list

        Description:  Test with one match between sets but empty list.

        Arguments:
            None

        """

        self.args_array = {"-f": [], "-m": "Marker"}

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between sets passed.

        Arguments:
            None

        """

        self.file_chk_list = ["-a"]

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))

    def test_empty_dirchklist(self):

        """Function:  test_empty_dirchklist

        Description:  Test with dir_chk_list is empty.

        Arguments:
            None

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                 self.file_chk_list))


if __name__ == "__main__":
    unittest.main()
