#!/usr/bin/python
# Classification (U)

"""Program:  arg_file_chk.py

    Description:  Unit testing of arg_file_chk in arg_parser.py.

    Usage:
        test/integration/arg_parser/arg_file_chk.py

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
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

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
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.path_file = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/arg_file_chk.txt")
        self.file_chk_list = ["-f"]
        self.args_array = {"-f": [self.path_file]}
        self.file_crt_list = ["-f"]

    def test_second_open_no_error(self):

        """Function:  test_second_open_no_error

        Description:  Test with second open no error.

        Arguments:

        """

        arg_parser.arg_file_chk(self.args_array, self.file_chk_list,
                                self.file_crt_list)

        self.assertTrue(os.path.isfile(self.path_file))

    @unittest.skip("Need to implement an error in the second open.")
    def test_second_open_error(self):

        """Function:  test_second_open_error

        Description:  Test with second open but returns error.

        Arguments:

        """

        arg_parser.arg_file_chk(self.args_array, self.file_chk_list,
                                self.file_crt_list)

    def test_filecrtlist_in_list(self):

        """Function:  test_filecrtlist_in_list

        Description:  Test with file_crt_list with option in list.

        Arguments:

        """

        arg_parser.arg_file_chk(self.args_array, self.file_chk_list,
                                self.file_crt_list)

        self.assertTrue(os.path.isfile(self.path_file))

    def test_filecrtlist_not_in_list(self):

        """Function:  test_filecrtlist_not_in_list

        Description:  Test with file_crt_list with option not in list.

        Arguments:

        """

        self.file_crt_list = ["-g"]

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list,
                                    self.file_crt_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_filecrtlist_empty_list(self):

        """Function:  test_filecrtlist_empty_list

        Description:  Test with file_crt_list passed with empty list.

        Arguments:

        """

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list, [])

        self.assertFalse(os.path.isfile(self.path_file))

    def test_filecrtlist_not_passed(self):

        """Function:  test_filecrtlist_not_passed

        Description:  Test with file_crt_list not being passed.

        Arguments:

        """

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_first_open_error_two(self):

        """Function:  test_first_open_error_two

        Description:  Test with first open and error 2 returned.

        Arguments:

        """

        arg_parser.arg_file_chk(self.args_array, self.file_chk_list,
                                self.file_crt_list)

        self.assertTrue(os.path.isfile(self.path_file))

    @unittest.skip("Need to implement an IOError 10 code.")
    def test_first_open_error_ten(self):

        """Function:  test_first_open_error_ten

        Description:  Test with first open and error 10 returned.

        Arguments:

        """

        self.assertTrue(arg_parser.arg_file_chk(self.args_array,
                                                self.file_chk_list))

    def test_first_open_no_errors(self):

        """Function:  test_first_open_no_errors

        Description:  Test with first open and no errors.

        Arguments:

        """

        fname = open(self.path_file, "w")
        fname.close()

        arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertTrue(os.path.isfile(self.path_file))

    def test_name_loop_zero_items(self):

        """Function:  test_name_loop_zero_items

        Description:  Test with name loop on zero items.

        Arguments:

        """

        self.args_array = {"-f": []}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    def test_name_loop_two_items(self):

        """Function:  test_name_loop_two_items

        Description:  Test with name loop on two items.

        Arguments:

        """

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_name_loop_one_item(self):

        """Function:  test_name_loop_one_item

        Description:  Test with name loop on one item.

        Arguments:

        """

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    @unittest.skip("Error:  need string or buffer, set found")
    def test_isinstance_is_set(self):

        """Function:  test_isinstance_is_set

        Description:  Test with isinstance against a set.

        Arguments:

        """

        self.args_array = {"-f": {self.path_file}}

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_isinstance_is_string(self):

        """Function:  test_isinstance_is_string

        Description:  Test with isinstance against a string.

        Arguments:

        """

        self.args_array = {"-f": self.path_file}

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_isinstance_is_list(self):

        """Function:  test_isinstance_is_list

        Description:  Test with isinstance against a list.

        Arguments:

        """

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_two_match_between_sets(self):

        """Function:  test_two_match_between_sets

        Description:  Test with two matches between sets.

        Arguments:

        """

        self.file_chk_list = ["-f", "-g"]
        self.args_array = {"-f": self.path_file, "-g": "test2/file2"}

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_one_match_between_sets(self):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets.

        Arguments:

        """

        with gen_libs.no_std_out():
            arg_parser.arg_file_chk(self.args_array, self.file_chk_list)

        self.assertFalse(os.path.isfile(self.path_file))

    def test_one_match_empty_list(self):

        """Function:  test_one_match_empty_list

        Description:  Test with one match between sets but empty list.

        Arguments:

        """

        self.args_array = {"-f": [], "-m": "Marker"}

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between sets passed.

        Arguments:

        """

        self.file_chk_list = ["-a"]

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.path_file):
            os.remove(self.path_file)


if __name__ == "__main__":
    unittest.main()
