#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_file_chk.py

    Description:  Unit testing of arg_file_chk in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_file_chk.py

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
import gen_class
import gen_libs
import version

__version__ = version.__version__


class FileOpen(object):

    """Class:  FileOpen

    Description:  Class stub holder for file open class.

    Methods:
        close

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_file_crt_override
        test_file_chk_override
        test_second_open_no_error
        test_second_open_error
        test_file_crt_in_list
        test_file_crt_not_in_list
        test_file_crt_empty_list
        test_file_crt_not_passed
        test_first_open_error_two
        test_first_open_error_ten
        test_first_open_no_errors
        test_name_loop_zero_items
        test_name_loop_two_items
        test_name_loop_one_item
        test_isinstance_is_set
        test_isinstance_is_string
        test_isinstance_is_list
        test_two_match_between_sets
        test_one_match_between_sets
        test_one_match_empty_list
        test_no_match_between_sets

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.path_file = "/path/file1"

        self.argv = [
            "program.py", "-f", [self.path_file], "-m", "Marker"]
        self.argv2 = [
            "program.py", "-f", self.path_file, "-g", "/path/file2"]
        self.argv3 = ["program.py", "-f", self.path_file, "-m", "Marker"]
        self.argv4 = [
            "program.py", "-f", (self.path_file), "-m", "Marker"]
        self.argv5 = [
            "program.py", "-f", [self.path_file, "/path/file3"],
            "-m", "Marker"]

        self.opt_val = ["-f", "-m", "-g"]

        self.file_chk = ["-f"]
        self.file_chk2 = ["-a"]
        self.file_chk3 = ["-f", "-g"]

        self.file_crt = ["-f"]
        self.file_crt2 = ["-g"]
        self.file_crt3 = []

        self.open = FileOpen()

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_file_crt_override(self, mock_crt):

        """Function:  test_file_crt_override

        Description:  Test with passing in file_crt to override.

        Arguments:

        """

        mock_crt.return_value = True

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt3)

        self.assertTrue(args_array.arg_file_chk(file_crt=self.file_crt))

    def test_file_chk_override(self):

        """Function:  test_file_chk_override

        Description:  Test with passing in file_chk to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk(file_chk=self.file_chk2))

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_second_open_no_error(self, mock_crt):

        """Function:  test_second_open_no_error

        Description:  Test with second open no error.

        Arguments:

        """

        mock_crt.return_value = True

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_second_open_error(self, mock_crt):

        """Function:  test_second_open_error

        Description:  Test with second open but returns error.

        Arguments:

        """

        mock_crt.return_value = False

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt)

        self.assertFalse(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_file_crt_in_list(self, mock_crt):

        """Function:  test_file_crt_in_list

        Description:  Test with file_crt with option in list.

        Arguments:

        """

        mock_crt.return_value = True

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_file_crt_not_in_list(self, mock_crt):

        """Function:  test_file_crt_not_in_list

        Description:  Test with file_crt with option not in list.

        Arguments:

        """

        mock_crt.return_value = False

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt2)

        self.assertFalse(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_file_crt_empty_list(self, mock_crt):

        """Function:  test_file_crt_empty_list

        Description:  Test with file_crt passed with empty list.

        Arguments:

        """

        mock_crt.return_value = False

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt3)

        self.assertFalse(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_file_crt_not_passed(self, mock_crt):

        """Function:  test_file_crt_not_passed

        Description:  Test with file_crt not being passed.

        Arguments:

        """

        mock_crt.return_value = False

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertFalse(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_first_open_error_two(self, mock_crt):

        """Function:  test_first_open_error_two

        Description:  Test with first open and error 2 returned.

        Arguments:

        """

        mock_crt.return_value = True

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk,
            file_crt=self.file_crt)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.ArgParser._file_chk_crt")
    def test_first_open_error_ten(self, mock_crt):

        """Function:  test_first_open_error_ten

        Description:  Test with first open and error 10 returned.

        Arguments:

        """

        mock_crt.return_value = False

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertFalse(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_first_open_no_errors(self, mock_open):

        """Function:  test_first_open_no_errors

        Description:  Test with first open and no errors.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    def test_name_loop_zero_items(self):

        """Function:  test_name_loop_zero_items

        Description:  Test with name loop on zero items.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)
        args_array.args_array["-f"] = []

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_name_loop_two_items(self, mock_open):

        """Function:  test_name_loop_two_items

        Description:  Test with name loop on two items.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_name_loop_one_item(self, mock_open):

        """Function:  test_name_loop_one_item

        Description:  Test with name loop on one item.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_isinstance_is_set(self, mock_open):

        """Function:  test_isinstance_is_set

        Description:  Test with isinstance against a set.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_isinstance_is_string(self, mock_open):

        """Function:  test_isinstance_is_string

        Description:  Test with isinstance against a string.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_isinstance_is_list(self, mock_open):

        """Function:  test_isinstance_is_list

        Description:  Test with isinstance against a list.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_two_match_between_sets(self, mock_open):

        """Function:  test_two_match_between_sets

        Description:  Test with two matches between sets.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, file_chk=self.file_chk3)

        self.assertTrue(args_array.arg_file_chk())

    @mock.patch("gen_class.open")
    def test_one_match_between_sets(self, mock_open):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)

        self.assertTrue(args_array.arg_file_chk())

    def test_one_match_empty_list(self):

        """Function:  test_one_match_empty_list

        Description:  Test with one match between sets but empty list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk)
        args_array.args_array["-f"] = []

        self.assertTrue(args_array.arg_file_chk())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between sets passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_chk=self.file_chk2)

        self.assertTrue(args_array.arg_file_chk())


if __name__ == "__main__":
    unittest.main()
