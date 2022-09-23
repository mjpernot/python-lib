# Classification (U)

"""Program:  argparser_init.py

    Description:  Unit testing of ArgParser.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/argparser_init.py

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


def validate_value():

    """Function:  validate_value

    Description:  Test function.

    Arguments:

    """

    return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_opt_xor_val
        test_opt_wildcard
        test_opt_valid_val
        test_valid_func
        test_opt_xor
        test_opt_or
        test_xor_noreq
        test_file_crt
        test_file_perm_chk
        test_dir_crt
        test_dir_chk
        test_dir_perms_chk
        test_opt_con_or
        test_opt_con_req
        test_opt_req
        test_defaults
        test_opt_val_bin
        test_multi_val
        test_opt_def
        test_opt_val
        test_do_parse_fail
        test_do_parse2
        test_do_parse
        test_multiple_boolean_arg
        test_single_boolean_arg
        test_program_only
        test_empty_cmd_line

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "programname.py"

        self.argv = []
        self.argv2 = [p_name]
        self.results_arg_array = {}
        self.argv3 = [p_name, "-a"]
        self.results_arg_array3 = {"-a": True}
        self.argv4 = [p_name, "-a", "-b"]
        self.results_arg_array4 = {"-a": True, "-b": True}
        self.opt_val = ["-c", "-d", "-o", "-t", "-s", "-y"]
        self.results_opt_val = ["-c", "-d", "-o", "-t", "-s", "-y"]
        self.opt_def = {"-i": "sysmon:server_pkgs"}
        self.results_opt_def = {"-i": "sysmon:server_pkgs"}
        self.multi_val = ["-e", "-s"]
        self.results_multi_val = ["-e", "-s"]
        self.opt_val_bin = ["-F", "-L"]
        self.results_opt_val_bin = ["-F", "-L"]
        self.defaults = {"-c": 3, "-d": "test"}
        self.results_defaults = {"-c": 3, "-d": "test"}
        self.opt_req = ["-c", "-d"]
        self.results_opt_req = ["-c", "-d"]
        self.opt_con_req = {"-s": ["-t"]}
        self.results_opt_con_req = {"-s": ["-t"]}
        self.opt_con_or = {"-C": ["-l"], "-S": ["-r"]}
        self.results_opt_con_or = {"-C": ["-l"], "-S": ["-r"]}
        self.dir_perms_chk = {"-d": 4, "-g": 4}
        self.results_dir_perms_chk = {"-d": 4, "-g": 4}
        self.dir_chk = ["-o", "-d", "-p"]
        self.results_dir_chk = ["-o", "-d", "-p"]
        self.dir_crt = ["-o"]
        self.results_dir_crt = ["-o"]
        self.file_perm_chk = {"-a": 6, "-e": 4, "-q": 1}
        self.results_file_perm_chk = {"-a": 6, "-e": 4, "-q": 1}
        self.file_crt = ["-f"]
        self.results_file_crt = ["-f"]
        self.xor_noreq = {"-l": "-b"}
        self.results_xor_noreq = {"-l": "-b"}
        self.opt_or = {"-a": ["-b", "-c"], "-d": ["-e"]}
        self.results_opt_or = {"-a": ["-b", "-c"], "-d": ["-e"]}
        self.opt_xor = {"-I": ["-P"], "-P": ["-I"]}
        self.results_opt_xor = {"-I": ["-P"], "-P": ["-I"]}
        self.valid_func = {"-a": validate_value}
        self.results_valid_func = {"-a": validate_value}
        self.opt_valid_val = {"-k": ["and", "or"], "-g": ["a", "w"]}
        self.results_opt_valid_val = {"-k": ["and", "or"], "-g": ["a", "w"]}
        self.opt_wildcard = ["-a", "-b"]
        self.results_opt_wildcard = ["-a", "-b"]
        self.opt_xor_val = {"-a": ["-b", "-c"], "-d": ["-e"]}
        self.results_opt_xor_val = {"-a": ["-b", "-c"], "-d": ["-e"]}

    def test_opt_xor_val(self):

        """Function:  test_opt_xor_val

        Description:  Test with opt_xor_val argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_xor_val=self.opt_xor_val)

        self.assertEqual(args_array.opt_xor_val, self.results_opt_xor_val)

    def test_opt_wildcard(self):

        """Function:  test_opt_wildcard

        Description:  Test with opt_wildcard argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_wildcard=self.opt_wildcard)

        self.assertEqual(args_array.opt_wildcard, self.results_opt_wildcard)

    def test_opt_valid_val(self):

        """Function:  test_opt_valid_val

        Description:  Test with opt_valid_val argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_valid_val=self.opt_valid_val)

        self.assertEqual(args_array.opt_valid_val, self.results_opt_valid_val)

    def test_valid_func(self):

        """Function:  test_valid_func

        Description:  Test with valid_func argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, valid_func=self.valid_func)

        self.assertEqual(args_array.valid_func, self.results_valid_func)

    def test_opt_xor(self):

        """Function:  test_opt_xor

        Description:  Test with opt_xor argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_xor=self.opt_xor)

        self.assertEqual(args_array.opt_xor, self.results_opt_xor)

    def test_opt_or(self):

        """Function:  test_opt_or

        Description:  Test with opt_or argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_or=self.opt_or)

        self.assertEqual(args_array.opt_or, self.results_opt_or)

    def test_xor_noreq(self):

        """Function:  test_xor_noreq

        Description:  Test with xor_noreq argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, xor_noreq=self.xor_noreq)

        self.assertEqual(args_array.xor_noreq, self.results_xor_noreq)

    def test_file_crt(self):

        """Function:  test_file_crt

        Description:  Test with file_crt argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, file_crt=self.file_crt)

        self.assertEqual(args_array.file_crt, self.results_file_crt)

    def test_file_perm_chk(self):

        """Function:  test_file_perm_chk

        Description:  Test with file_perm_chk argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, file_perm_chk=self.file_perm_chk)

        self.assertEqual(args_array.file_perm_chk, self.results_file_perm_chk)

    def test_dir_crt(self):

        """Function:  test_dir_crt

        Description:  Test with dir_crt argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, dir_crt=self.dir_crt)

        self.assertEqual(args_array.dir_crt, self.results_dir_crt)

    def test_dir_chk(self):

        """Function:  test_dir_chk

        Description:  Test with dir_chk argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, dir_chk=self.dir_chk)

        self.assertEqual(args_array.dir_chk, self.results_dir_chk)

    def test_dir_perms_chk(self):

        """Function:  test_dir_perms_chk

        Description:  Test with dir_perms_chk argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, dir_perms_chk=self.dir_perms_chk)

        self.assertEqual(args_array.dir_perms_chk, self.results_dir_perms_chk)

    def test_opt_con_or(self):

        """Function:  test_opt_con_or

        Description:  Test with opt_con_or argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_con_or=self.opt_con_or)

        self.assertEqual(args_array.opt_con_or, self.results_opt_con_or)

    def test_opt_con_req(self):

        """Function:  test_opt_con_req

        Description:  Test with opt_con_req argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_con_req=self.opt_con_req)

        self.assertEqual(args_array.opt_con_req, self.results_opt_con_req)

    def test_opt_req(self):

        """Function:  test_opt_req

        Description:  Test with opt_req argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_req=self.opt_req)

        self.assertEqual(args_array.opt_req, self.results_opt_req)

    def test_defaults(self):

        """Function:  test_defaults

        Description:  Test with defaults argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, defaults=self.defaults)

        self.assertEqual(args_array.defaults, self.results_defaults)

    def test_opt_val_bin(self):

        """Function:  test_opt_val_bin

        Description:  Test with opt_val_bin argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val_bin=self.opt_val_bin)

        self.assertEqual(args_array.opt_val_bin, self.results_opt_val_bin)

    def test_multi_val(self):

        """Function:  test_multi_val

        Description:  Test with multi_val argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, multi_val=self.multi_val)

        self.assertEqual(args_array.multi_val, self.results_multi_val)

    def test_opt_def(self):

        """Function:  test_opt_def

        Description:  Test with opt_def argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_def=self.opt_def)

        self.assertEqual(args_array.opt_def, self.results_opt_def)

    def test_opt_val(self):

        """Function:  test_opt_val

        Description:  Test with opt_val argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, opt_val=self.opt_val)

        self.assertEqual(args_array.opt_val, self.results_opt_val)

    @mock.patch("gen_class.ArgParser.arg_parse2")
    def test_do_parse_fail(self, mock_parse):

        """Function:  test_do_parse_fail

        Description:  Test with do parse option passed, but fails.

        Arguments:

        """

        mock_parse.return_value = False

        with gen_libs.no_std_out():
            args_array = gen_class.ArgParser(self.argv4, do_parse=True)

        self.assertEqual(args_array.args_array, self.results_arg_array)

    def test_do_parse2(self):

        """Function:  test_do_parse2

        Description:  Test with do parse option passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv4, do_parse=True)

        self.assertEqual(args_array.argv, [])

    def test_do_parse(self):

        """Function:  test_do_parse

        Description:  Test with do parse option passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv4, do_parse=True)

        self.assertEqual(args_array.args_array, self.results_arg_array4)

    def test_multiple_boolean_arg(self):

        """Function:  test_multiple_boolean_arg

        Description:  Test with multiple boolean argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv4, do_parse=True)

        self.assertEqual(args_array.args_array, self.results_arg_array4)

    def test_single_boolean_arg(self):

        """Function:  test_single_boolean_arg

        Description:  Test with single boolean argument.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv3, do_parse=True)

        self.assertEqual(args_array.args_array, self.results_arg_array3)

    def test_program_only(self):

        """Function:  test_program_only

        Description:  Test with program name only.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv2, do_parse=True)

        self.assertEqual(args_array.args_array, self.results_arg_array)

    def test_empty_cmd_line(self):

        """Function:  test_empty_cmd_line

        Description:  Test with empty command line.

        Arguments:

        """

        args_array = gen_class.ArgParser(self.argv, do_parse=True)

        self.assertEqual(args_array.args_array, self.results_arg_array)


if __name__ == "__main__":
    unittest.main()
