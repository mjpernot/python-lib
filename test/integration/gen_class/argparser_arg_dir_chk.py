# Classification (U)

"""Program:  argparser_arg_dir_chk.py

    Description:  Integration testing of arg_dir_chk in
        gen_class.ArgParser class.

    Usage:
        test/integration/gen_class/argparser_arg_dir_chk.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_dir_perms_chk_override
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

        p_name = "program.py"

        self.base_path = "test/integration/gen_class/tmp"
        self.dir1 = os.path.join(self.base_path, "dir1")
        self.dir2 = os.path.join(self.base_path, "dir2")

        self.argv = [p_name]
        self.argv2 = [p_name, "-d", self.dir1]
        self.argv3 = [p_name, "-d", self.dir1, "-g", self.dir2]
        self.opt_val = ["-d", "-g"]
        self.dir_perms_chk = {}
        self.dir_perms_chk2 = {"-d": 1}
        self.dir_perms_chk3 = {"-d": 4}
        self.dir_perms_chk4 = {"-d": 2}
        self.dir_perms_chk5 = {"-g": 1}
        self.dir_perms_chk6 = {"-d": 4, "-g": 4}
        self.dir_perms_chk7 = {"-d": 6}

    def test_dir_perms_chk_override(self):

        """Function:  test_dir_perms_chk_override

        Description:  Test with passing in dir_perms_chk to override.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("333", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk3, do_parse=True)

        self.assertTrue(
            args_array.arg_dir_chk(dir_perms_chk=self.dir_perms_chk4))

    def test_multiple_dirs_no_access3(self):

        """Function:  test_multiple_dirs_no_access3

        Description:  Test with multiple directories with both no access.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("111", 8))
        os.mkdir(self.dir2)
        os.chmod(self.dir2, int("111", 8))
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_multiple_dirs_no_access2(self):

        """Function:  test_multiple_dirs_no_access2

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.mkdir(self.dir2)
        os.chmod(self.dir2, int("111", 8))
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_multiple_dirs_no_access(self):

        """Function:  test_multiple_dirs_no_access

        Description:  Test with multiple directories with one no access.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("111", 8))
        os.mkdir(self.dir2)
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_multiple_dirs_access(self):

        """Function:  test_multiple_dirs_access

        Description:  Test with multiple directories with access.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.mkdir(self.dir2)
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk6, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_dir_exist_with_rw4(self):

        """Function:  test_dir_exist_with_rw4

        Description:  Test with directory and with no read or write acess.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("111", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk7, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_dir_exist_with_rw3(self):

        """Function:  test_dir_exist_with_rw3

        Description:  Test with directory and with no write acess.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("555", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_dir_exist_with_rw2(self):

        """Function:  test_dir_exist_with_rw2

        Description:  Test with directory and with no read acess.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("333", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_dir_exist_with_rw(self):

        """Function:  test_dir_exist_with_rw

        Description:  Test with directory and with read and write.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("777", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk7, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_dir_exist_with_w2(self):

        """Function:  test_dir_exist_with_w2

        Description:  Test with directory and with no write access.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("555", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_dir_exist_with_w(self):

        """Function:  test_dir_exist_with_w

        Description:  Test with directory and with write.

        Arguments:

        """

        os.mkdir(self.dir1)
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk4, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_dir_exist_with_x(self):

        """Function:  test_dir_exist_with_x

        Description:  Test with directory and only with execute.

        Arguments:

        """

        os.mkdir(self.dir1)
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_dir_exist_no_x(self):

        """Function:  test_dir_exist_no_x

        Description:  Test with no execute on directory.

        Arguments:

        """

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int("444", 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_dir_not_exist(self):

        """Function:  test_dir_not_exist

        Description:  Test with no directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val,
            dir_perms_chk=self.dir_perms_chk5, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_perms_chk=self.dir_perms_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

    def test_empty_dir_perms_chk(self):

        """Function:  test_empty_dir_perms_chk

        Description:  Test with dir_perms_chk is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_perms_chk=self.dir_perms_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk())

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
