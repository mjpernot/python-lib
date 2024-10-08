# Classification (U)

"""Program:  print_data.py

    Description:  Unit testing of print_data in gen_libs.py.

    Usage:
        test/unit/gen_libs/print_data.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_print_stdout_pprint
        test_print_file_pprint
        test_print_stdout
        test_print_file
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = "Print_Data"
        self.ofile = "test/unit/gen_libs/tmp/test_print_data.txt"

    def test_print_stdout_pprint(self):

        """Function:  test_print_stdout_pprint

        Description:  Test with printing data to standard out with pprint.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.print_data(self.data, use_pprint=True))

    def test_print_file_pprint(self):

        """Function:  test_print_file_pprint

        Description:  Test with printing data to file with pprint.

        Arguments:

        """

        gen_libs.print_data(self.data, ofile=self.ofile, use_pprint=True)

        self.assertTrue(os.path.isfile(self.ofile))

    def test_print_stdout(self):

        """Function:  test_print_stdout

        Description:  Test with printing data to standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.print_data(self.data))

    def test_print_file(self):

        """Function:  test_print_file

        Description:  Test with printing data to file.

        Arguments:

        """

        gen_libs.print_data(self.data, ofile=self.ofile)

        self.assertTrue(os.path.isfile(self.ofile))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
