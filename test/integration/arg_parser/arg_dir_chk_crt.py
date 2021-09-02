#!/usr/bin/python
# Classification (U)

"""Program:  arg_dir_chk_crt.py

    Description:  Unit testing of arg_dir_chk_crt in arg_parser.py.

    Usage:
        test/integration/arg_parser/arg_dir_chk_crt.py

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
import gen_libs
import version

__version__ = version.__version__


def raise_oserror():

    """Function:  raise_oserror

    Description:  Stub holder to return a raised OSError exception.

    Arguments:

    """

    raise OSError


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_chk_multiple_dirs
        test_match_create_dir_fail
        test_match_create_dir
        test_match_no_dir
        test_match_no_access
        test_one_match_between_sets
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_chk_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.path_dir1 = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/dir1")
        self.path_dir2 = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/dir2")
        self.args_array = {}
        self.args_array2 = {"-d": self.path_dir1}
        self.args_array3 = {"-d": self.path_dir1, "-g": self.path_dir2}
        self.dir_chk_list = []
        self.dir_chk_list2 = ["-d"]
        self.dir_chk_list3 = ["-d", "-g"]
        self.dir_chk_list4 = ["-d", "-i"]
        self.dir_chk_list5 = ["-g"]
        self.dir_crt_list = []
        self.dir_crt_list2 = ["-d"]
        self.dir_crt_list3 = ["-d", "-g"]

    def test_chk_multiple_dirs(self):

        """Function:  test_chk_multiple_dirs

        Description:  Test with creating multiple directories.

        Arguments:

        """

        arg_parser.arg_dir_chk_crt(
            self.args_array3, self.dir_chk_list3, self.dir_crt_list3)

        self.assertTrue(os.path.isdir(self.path_dir1))
        self.assertTrue(os.path.isdir(self.path_dir2))

    @unittest.skip("Need to figure out how to test this without mock.")
    @mock.patch("arg_parser.os")
    def test_match_create_dir_fail(self, mock_os):

        """Function:  test_match_create_dir_fail

        Description:  Test with failing to create directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = False
        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                       self.dir_chk_list2,
                                                       self.dir_crt_list2))

    def test_match_create_dir(self):

        """Function:  test_match_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        arg_parser.arg_dir_chk_crt(
            self.args_array2, self.dir_chk_list2, self.dir_crt_list2)

        self.assertTrue(os.path.isdir(self.path_dir1))

    def test_match_no_dir(self):

        """Function:  test_match_no_dir

        Description:  Test with directory does not exist.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                       self.dir_chk_list2))

    # Known bug:  The check for os.access should be checking in the
    #   dir_chk_list, not in dir_crt_list.
    #   New code arg_dir_chk_crt() should be:
    #       if is not directory and in dir_crt_list:
    #           create dir
    #       elif is not directory:
    #           dir does not exist
    #       elif not os.access to write:
    #           not writable
    @unittest.skip("Known bug")
    @mock.patch("arg_parser.os")
    def test_match_no_access(self, mock_os):

        """Function:  test_match_no_access

        Description:  Test with match between sets, but no access to directory.

        Arguments:

        """

        mock_os.path.isdir.return_value = True
        mock_os.access.return_value = False

        self.assertTrue(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                   self.dir_chk_list2))

    def test_one_match_between_sets(self):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets and is directory.

        Arguments:

        """

        os.makedirs(self.path_dir1)

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                    self.dir_chk_list2))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                    self.dir_chk_list5))

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array,
                                                    self.dir_chk_list2))

    def test_empty_dir_chk_list(self):

        """Function:  test_empty_dir_chk_list

        Description:  Test with dir_chk_list is empty.

        Arguments:

        """

        self.assertFalse(arg_parser.arg_dir_chk_crt(self.args_array2,
                                                    self.dir_chk_list))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.path_dir1):
            os.rmdir(self.path_dir1)

        if os.path.isdir(self.path_dir2):
            os.rmdir(self.path_dir2)


if __name__ == "__main__":
    unittest.main()
