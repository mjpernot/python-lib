# Classification (U)

"""Program:  argparser_init.py

    Description:  Integration testing of ArgParser.__init__ in gen_class.py.

    Usage:
        test/integration/gen_class/argparser_init.py

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
        self.argv3 = [p_name, "-a"]
        self.argv4 = [p_name, "-a", "-b"]

        self.opt_val = ["-a"]

        self.results_arg_array = {}
        self.results_arg_array3 = {"-a": True}
        self.results_arg_array4 = {"-a": True, "-b": True}

    def test_do_parse_fail(self):

        """Function:  test_do_parse_fail

        Description:  Test with do parse option passed, but fails.

        Arguments:

        """

        with gen_libs.no_std_out():
            args_array = gen_class.ArgParser(
                self.argv3, opt_val=self.opt_val, do_parse=True)

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
