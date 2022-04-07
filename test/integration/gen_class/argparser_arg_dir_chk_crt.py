#!/usr/bin/python
# Classification (U)

"""Program:  argparser_arg_dir_chk_crt.py

    Description:  Integration testing of arg_dir_chk_crt in
        gen_class.ArgParser class.

    Usage:
        test/integration/gen_class/argparser_arg_dir_chk_crt.py

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
PERM4 = "444"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_not_subset
        test_match_create_dir
        test_match_no_dir
        test_match_no_access
        test_one_match_between_sets
        test_no_match_between_sets
        test_empty_args_array
        test_empty_dir_chk
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_path = "test/integration/gen_class/tmp"
        self.dir3 = os.path.join(self.base_path, "dir3")
        self.dir4 = os.path.join(self.base_path, "dir4")
        self.dir5 = os.path.join(self.base_path, "dir5")
        self.dir6 = os.path.join(self.base_path, "dir6")

        self.argv = ["program.py"]
        self.argv2 = ["program.py", "-d", self.dir3]
        self.argv3 = ["program.py", "-d", self.dir3, "-g", self.dir4]
        self.argv4 = ["program.py", "-d", self.dir5]
        self.argv5 = ["program.py", "-d", self.dir6]

        self.opt_val = ["-d", "-g"]

        self.dir_chk = []
        self.dir_chk2 = ["-d"]
        self.dir_chk3 = ["-d", "-g"]
        self.dir_chk4 = ["-d", "-i"]
        self.dir_chk5 = ["-g"]

        self.dir_crt = []
        self.dir_crt2 = ["-d"]
        self.dir_crt3 = ["-g"]

    def test_not_subset(self):

        """Function:  test_not_subset

        Description:  Test with dir_crt_list not subset of dir_chk_list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, dir_chk=self.dir_chk4,
            dir_crt=self.dir_crt3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk_crt())

    def test_match_create_dir(self):

        """Function:  test_match_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            dir_crt=self.dir_crt2, do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_match_no_dir(self):

        """Function:  test_match_no_dir

        Description:  Test with directory does not exist.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk_crt())

    def test_match_no_access(self):

        """Function:  test_match_no_access

        Description:  Test with match between sets, but no access to directory.

        Arguments:

        """

        global PERM4

        os.mkdir(self.dir3)
        os.chmod(self.dir3, int(PERM4, 8))
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_dir_chk_crt())

    def test_one_match_between_sets(self):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets and is directory.

        Arguments:

        """

        os.mkdir(self.dir3)
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between arguments passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk5,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with args_array is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, dir_chk=self.dir_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def test_empty_dir_chk(self):

        """Function:  test_empty_dir_chk

        Description:  Test with dir_chk is empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, dir_chk=self.dir_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_dir_chk_crt())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.dir3):
            os.rmdir(self.dir3)

        if os.path.isdir(self.dir4):
            os.rmdir(self.dir4)


if __name__ == "__main__":
    unittest.main()
