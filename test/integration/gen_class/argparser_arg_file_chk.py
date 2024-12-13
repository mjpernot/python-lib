# Classification (U)

"""Program:  argparser_arg_file_chk.py

    Description:  Integration testing of arg_file_chk in
        gen_class.ArgParser class.

    Usage:
        test/integration/gen_class/argparser_arg_file_chk.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_incorrect_perms
        test_file_crt_override
        test_file_chk_override
        test_file_crt_in_list
        test_file_crt_not_in_list
        test_file_crt_empty_list
        test_file_crt_not_passed
        test_open_error_two
        test_open_no_errors
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
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"

        self.base_path = "test/integration/gen_class/tmp"
        self.file = os.path.join(self.base_path, "file1")
        self.file2 = os.path.join(self.base_path, "file2")
        self.file3 = os.path.join(self.base_path, "file3")

        self.argv = [p_name, "-f", [self.file], "-m", "Marker"]
        self.argv2 = [p_name, "-f", self.file, "-g", self.file2]
        self.argv3 = [p_name, "-f", self.file, "-m", "Marker"]
        self.argv4 = [p_name, "-f", (self.file), "-m", "Marker"]
        self.argv5 = [p_name, "-f", [self.file, self.file3], "-m", "Marker"]

        self.opt_val = ["-f", "-m", "-g"]

        self.file_chk = {"-f": 6}
        self.file_chk2 = {"-a": 6}
        self.file_chk3 = {"-f": 6, "-g": 6}
        self.file_chk4 = {"-f": 7}

        self.file_crt = ["-f"]
        self.file_crt2 = ["-g"]
        self.file_crt3 = []

    def test_incorrect_perms(self):

        """Function:  test_incorrect_perms

        Description:  Test with incorrect permissions.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk4,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_file_chk())

    def test_file_crt_override(self):

        """Function:  test_file_crt_override

        Description:  Test with passing in file_crt to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            file_crt=self.file_crt3, do_parse=True)

        self.assertTrue(args_array.arg_file_chk(file_crt=self.file_crt))

    def test_file_chk_override(self):

        """Function:  test_file_chk_override

        Description:  Test with passing in file_chk to override.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk(file_perm_chk=self.file_chk2))

    def test_file_crt_in_list(self):

        """Function:  test_file_crt_in_list

        Description:  Test with file_crt with option in list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            file_crt=self.file_crt, do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_file_crt_not_in_list(self):

        """Function:  test_file_crt_not_in_list

        Description:  Test with file_crt with option not in list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            file_crt=self.file_crt2, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_file_chk())

    def test_file_crt_empty_list(self):

        """Function:  test_file_crt_empty_list

        Description:  Test with file_crt passed with empty list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            file_crt=self.file_crt3, do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_file_chk())

    def test_file_crt_not_passed(self):

        """Function:  test_file_crt_not_passed

        Description:  Test with file_crt not being passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(args_array.arg_file_chk())

    def test_open_error_two(self):

        """Function:  test_open_error_two

        Description:  Test with open and error 2 returned.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            file_crt=self.file_crt, do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_open_no_errors(self):

        """Function:  test_open_no_errors

        Description:  Test with open and no errors.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_name_loop_zero_items(self):

        """Function:  test_name_loop_zero_items

        Description:  Test with name loop on zero items.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)
        args_array.args_array["-f"] = []

        self.assertTrue(args_array.arg_file_chk())

    def test_name_loop_two_items(self):

        """Function:  test_name_loop_two_items

        Description:  Test with name loop on two items.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()   # pylint:disable=R1732
        open(self.file3, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv5, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_name_loop_one_item(self):

        """Function:  test_name_loop_one_item

        Description:  Test with name loop on one item.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_isinstance_is_set(self):

        """Function:  test_isinstance_is_set

        Description:  Test with isinstance against a set.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv4, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_isinstance_is_string(self):

        """Function:  test_isinstance_is_string

        Description:  Test with isinstance against a string.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_isinstance_is_list(self):

        """Function:  test_isinstance_is_list

        Description:  Test with isinstance against a list.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_two_match_between_sets(self):

        """Function:  test_two_match_between_sets

        Description:  Test with two matches between sets.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()   # pylint:disable=R1732
        open(self.file2, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, file_perm_chk=self.file_chk3,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_one_match_between_sets(self):

        """Function:  test_one_match_between_sets

        Description:  Test with one match between sets.

        Arguments:

        """

        open(self.file, "w", encoding="UTF-8").close()  # pylint:disable=R1732
        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def test_one_match_empty_list(self):

        """Function:  test_one_match_empty_list

        Description:  Test with one match between sets but empty list.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk,
            do_parse=True)
        args_array.args_array["-f"] = []

        self.assertTrue(args_array.arg_file_chk())

    def test_no_match_between_sets(self):

        """Function:  test_no_match_between_sets

        Description:  Test with no match between sets passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_perm_chk=self.file_chk2,
            do_parse=True)

        self.assertTrue(args_array.arg_file_chk())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)

        if os.path.isfile(self.file2):
            os.remove(self.file2)

        if os.path.isfile(self.file3):
            os.remove(self.file3)


if __name__ == "__main__":
    unittest.main()
