# Classification (U)

"""Program:  argparser_arg_set_path.py

    Description:  Unit testing of arg_set_path in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_arg_set_path.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_path_no_cmd
        test_no_path_cmd
        test_path_no_cmd
        test_path_cmd
        test_trailing_slash
        test_arg_not_present
        test_arg_present
        test_empty_both
        test_empty_arg_opt
        test_empty_args_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_name = "program.py"
        self.argv = [p_name]
        self.argv2 = [p_name, "-a", "/dir/path", "-c", "/dir/diff_path"]
        self.argv3 = [p_name, "-a", "/dir/path/"]
        self.opt_val = ["-a", "-c"]
        self.arg_opt = None
        self.arg_opt2 = "-a"
        self.arg_opt3 = "-b"
        self.cmd = "mysql"
        self.results = ""
        self.results2 = "/dir/path/"
        self.results3 = "/dir/path/mysql"
        self.results4 = "mysql"

    def test_no_path_no_cmd(self):

        """Function:  test_no_path_no_cmd

        Description:  Test with path, but no command passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.arg_set_path(self.arg_opt3), self.results)

    def test_no_path_cmd(self):

        """Function:  test_no_path_cmd

        Description:  Test with no path, but command passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.arg_set_path(
                self.arg_opt3, cmd=self.cmd), self.results4)

    def test_path_no_cmd(self):

        """Function:  test_path_no_cmd

        Description:  Test with path, but no command passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.arg_set_path(self.arg_opt2), self.results2)

    def test_path_cmd(self):

        """Function:  test_path_cmd

        Description:  Test with path and command passed.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(
            args_array.arg_set_path(
                self.arg_opt2, cmd=self.cmd), self.results3)

    def test_trailing_slash(self):

        """Function:  test_trailing_slash

        Description:  Test with trailing slash already present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv3, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.arg_set_path(self.arg_opt2), self.results2)

    def test_arg_not_present(self):

        """Function:  test_arg_not_present

        Description:  Test with argument not present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.arg_set_path(self.arg_opt3), self.results)

    def test_arg_present(self):

        """Function:  test_arg_present

        Description:  Test with argument present.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.arg_set_path(self.arg_opt2), self.results2)

    def test_empty_both(self):

        """Function:  test_empty_both

        Description:  Test with both args empty.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.arg_set_path(self.arg_opt), self.results)

    def test_empty_arg_opt(self):

        """Function:  test_empty_arg_opt

        Description:  Test with empty string for arg_opt.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv2, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.arg_set_path(self.arg_opt), self.results)

    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty dictionary for args_array.

        Arguments:

        """

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, do_parse=True)

        self.assertEqual(args_array.arg_set_path(self.arg_opt2), self.results)


if __name__ == "__main__":
    unittest.main()
