#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_dir_crt.py

    Description:  Integration testing of arg_dir_crt in
        gen_class.ArgParser class.

    Usage:
        test/integration/gen_class/argparser_arg_dir_crt.py

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
import gen_libs
import version

__version__ = version.__version__

# Global
PERM1 = "111"
PERM3 = "333"
PERM4 = "444"
PERM5 = "555"
PERM7 = "777"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_create_two_dir2
        test_create_two_dir
        test_create_one_dir2
        test_create_one_dir
        test_dir_perms_crt_override
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
        test_dir_not_exist2
        test_dir_not_exist
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_perms_crt
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_path = "test/integration/gen_class/tmp"
        self.dir1 = os.path.join(self.base_path, "dir1")
        self.dir2 = os.path.join(self.base_path, "dir2")

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-d", self.dir1]
        self.argv3 = ["program.py", "-d", self.dir1, "-g", self.dir2]
        self.opt_val = ["-d", "-g"]
        self.dir_perms_crt = {}
        self.dir_perms_crt2 = {"-d": 1}
        self.dir_perms_crt3 = {"-d": 4}
        self.dir_perms_crt4 = {"-d": 2}
        self.dir_perms_crt5 = {"-g": 1}
        self.dir_perms_crt6 = {"-d": 4, "-g": 4}
        self.dir_perms_crt7 = {"-d": 6}

    def test_create_two_dir2(self):

        """Function:  test_create_two_dir2

        Description:  Test with two directories to create.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)
        args_array.arg_dir_crt()

        self.assertTrue(os.path.isdir(self.dir1) and os.path.isdir(self.dir2))

    def test_create_two_dir(self):

        """Function:  test_create_two_dir

        Description:  Test with two directories to create.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_create_one_dir2(self):

        """Function:  test_create_one_dir2

        Description:  Test with one directory exist and one does not.

        Arguments:

        """

        os.mkdir(self.dir1)

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)
        args_array.arg_dir_crt()

        self.assertTrue(os.path.isdir(self.dir1) and os.path.isdir(self.dir2))

    def test_create_one_dir(self):

        """Function:  test_create_one_dir

        Description:  Test with one directory exist and one does not.

        Arguments:

        """

        os.mkdir(self.dir1)

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_dir_perms_crt_override(self):

        """Function:  test_dir_perms_crt_override

        Description:  Test with passing in dir_perms_crt to override.

        Arguments:

        """

        global PERM3

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM3, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt3, do_parse=True)

        self.assertTrue(
            args_array.arg_dir_crt(dir_perms_crt=self.dir_perms_crt4))

    def test_multiple_dirs_no_access3(self):

        """Function:  test_multiple_dirs_no_access3

        Description:  Test with multiple directories with both no access.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))
        os.mkdir(self.dir2)
        os.chmod(self.dir2, int(PERM1, 8))
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_multiple_dirs_no_access2(self):

        """Function:  test_multiple_dirs_no_access2

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.mkdir(self.dir2)
        os.chmod(self.dir2, int(PERM1, 8))
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_multiple_dirs_no_access(self):

        """Function:  test_multiple_dirs_no_access

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))
        os.mkdir(self.dir2)
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_multiple_dirs_access(self):

        """Function:  test_multiple_dirs_access

        Description:  Test with multiple directories with access.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.mkdir(self.dir2)
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt6, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_dir_exist_with_rw4(self):

        """Function:  test_dir_exist_with_rw4

        Description:  Test with directory and with no read or write acess.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt7, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_dir_exist_with_rw3(self):

        """Function:  test_dir_exist_with_rw3

        Description:  Test with directory and with no write acess.

        Arguments:

        """

        global PERM5

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM5, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt4, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_dir_exist_with_rw2(self):

        """Function:  test_dir_exist_with_rw2

        Description:  Test with directory and with no read acess.

        Arguments:

        """

        global PERM3

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM3, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_dir_exist_with_rw(self):

        """Function:  test_dir_exist_with_rw

        Description:  Test with directory and with read and write.

        Arguments:

        """

        global PERM7

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM7, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt7, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_dir_exist_with_w2(self):

        """Function:  test_dir_exist_with_w2

        Description:  Test with directory and with no write access.

        Arguments:

        """

        global PERM5

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM5, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt4, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_dir_exist_with_w(self):

        """Function:  test_dir_exist_with_w

        Description:  Test with directory and with write.

        Arguments:

        """

        os.mkdir(self.dir1)
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt4, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_dir_exist_with_x(self):

        """Function:  test_dir_exist_with_x

        Description:  Test with directory and only with execute.

        Arguments:

        """

        os.mkdir(self.dir1)
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt2, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_dir_exist_no_x(self):

        """Function:  test_dir_exist_no_x

        Description:  Test with no execute on directory.

        Arguments:

        """

        global PERM4

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM4, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_crt())

    def test_dir_not_exist2(self):

        """Function:  test_dir_not_exist2

        Description:  Test with no directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt2, do_parse=True)
        args_array.arg_dir_crt()

        self.assertTrue(os.path.isdir(self.dir1))

    def test_dir_not_exist(self):

        """Function:  test_dir_not_exist

        Description:  Test with no directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt2, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_crt=self.dir_perms_crt5, do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_perms_crt=self.dir_perms_crt2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def test_empty_dir_perms_crt(self):

        """Function:  test_empty_dir_perms_crt

        Description:  Test with dir_perms_crt is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_perms_crt=self.dir_perms_crt,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_crt())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.dir1):
            os.rmdir(self.dir1)

        if os.path.isdir(self.dir2):
            os.rmdir(self.dir2)


if __name__ == "__main__":
    unittest.main()
