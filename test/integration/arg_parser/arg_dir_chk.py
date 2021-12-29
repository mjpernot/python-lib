#!/usr/bin/python
# Classification (U)

"""Program:  arg_dir_chk.py

    Description:  Integration testing of arg_dir_chk in arg_parser.py.

    Usage:
        test/integration/arg_parser/arg_dir_chk.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiple_dirs_no_access3
        test_multiple_dirs_no_access2
        test_multiple_dirs_no_access
        test_multiple_dirs_access
        test_dir_exist_with_rw4
        test_dir_exist_with_rw3
        test_dir_exist_with_rw2
        test_dir_exist_with_rw
        test_dir_exist_with_w2
        test_dir_exist_with_w
        test_dir_exist_with_r2
        test_dir_exist_with_r
        test_dir_exist_with_x
        test_dir_exist_no_x
        test_dir_not_exist
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_perms_chk
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        base = "0o"
        perm7 = "777"
        perm5 = "555"
        perm4 = "444"
        perm3 = "333"
        perm2 = "222"
        perm1 = "111"
        self.base_perm7 = int(base + perm7, 8)
        self.base_perm5 = int(base + perm5, 8)
        self.base_perm4 = int(base + perm4, 8)
        self.base_perm3 = int(base + perm3, 8)
        self.base_perm2 = int(base + perm2, 8)
        self.base_perm1 = int(base + perm1, 8)
        self.path_dir0 = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/arg_dir_chk0")
        self.path_dir1 = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/arg_dir_chk1")
        self.path_dir2 = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/arg_dir_chk2")
        os.makedirs(self.path_dir1)
        os.makedirs(self.path_dir2)
        self.args_array = {}
        self.args_array2 = {"-d": self.path_dir1}
        self.args_array3 = {"-d": self.path_dir1, "-g": self.path_dir2}
        self.args_array4 = {"-d": self.path_dir0}
        self.dir_perms_chk = {}
        self.dir_perms_chk2 = {"-d": 1}
        self.dir_perms_chk3 = {"-d": 4}
        self.dir_perms_chk4 = {"-d": 2}
        self.dir_perms_chk5 = {"-g": 1}
        self.dir_perms_chk6 = {"-d": 4, "-g": 4}

    def test_multiple_dirs_no_access3(self):

        """Function:  test_multiple_dirs_no_access3

        Description:  Test with multiple directories with both no access.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm3)
        os.chmod(self.path_dir2, self.base_perm3)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array3, self.dir_perms_chk6))

        os.chmod(self.path_dir1, self.base_perm7)
        os.chmod(self.path_dir2, self.base_perm7)

    def test_multiple_dirs_no_access2(self):

        """Function:  test_multiple_dirs_no_access2

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm7)
        os.chmod(self.path_dir2, self.base_perm3)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array3, self.dir_perms_chk6))

        os.chmod(self.path_dir1, self.base_perm7)
        os.chmod(self.path_dir2, self.base_perm7)

    def test_multiple_dirs_no_access(self):

        """Function:  test_multiple_dirs_no_access

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm3)
        os.chmod(self.path_dir2, self.base_perm7)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array3, self.dir_perms_chk6))

        os.chmod(self.path_dir1, self.base_perm7)
        os.chmod(self.path_dir2, self.base_perm7)

    def test_multiple_dirs_access(self):

        """Function:  test_multiple_dirs_access

        Description:  Test with multiple directories with access.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm7)
        os.chmod(self.path_dir2, self.base_perm7)

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array3, self.dir_perms_chk6))

    def test_dir_exist_with_rw4(self):

        """Function:  test_dir_exist_with_rw4

        Description:  Test with directory and with no read or write acess.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm1)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_exist_with_rw3(self):

        """Function:  test_dir_exist_with_rw3

        Description:  Test with directory and with no write acess.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm5)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_exist_with_rw2(self):

        """Function:  test_dir_exist_with_rw2

        Description:  Test with directory and with no read acess.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm3)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk3))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_exist_with_rw(self):

        """Function:  test_dir_exist_with_rw

        Description:  Test with directory and with read and write.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm7)

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

    def test_dir_exist_with_w2(self):

        """Function:  test_dir_exist_with_w2

        Description:  Test with directory and with no write access.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm1)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_exist_with_w(self):

        """Function:  test_dir_exist_with_w

        Description:  Test with directory and with write.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm3)

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk4))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_exist_with_x(self):

        """Function:  test_dir_exist_with_x

        Description:  Test with directory and only with execute.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm1)

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk2))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_exist_no_x(self):

        """Function:  test_dir_exist_no_x

        Description:  Test with no execute on directory.

        Arguments:

        """

        os.chmod(self.path_dir1, self.base_perm4)

        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk2))

        os.chmod(self.path_dir1, self.base_perm7)

    def test_dir_not_exist(self):

        """Function:  test_dir_not_exist

        Description:  Test with no directory.

        Arguments:

        """


        with gen_libs.no_std_out():
            self.assertFalse(
                arg_parser.arg_dir_chk(self.args_array4, self.dir_perms_chk2))

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk5))

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array, self.dir_perms_chk2))

    def test_empty_dir_perms_chk(self):

        """Function:  test_empty_dir_perms_chk

        Description:  Test with dir_perms_chk is empty.

        Arguments:

        """

        self.assertTrue(
            arg_parser.arg_dir_chk(self.args_array2, self.dir_perms_chk))

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
