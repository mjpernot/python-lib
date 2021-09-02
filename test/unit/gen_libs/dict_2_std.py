#!/usr/bin/python
# Classification (U)

"""Program:  dict_2_std.py

    Description:  Unit testing of dict_2_std in gen_libs.py.

    Usage:
        test/unit/gen_libs/dict_2_std.py

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
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_print_stdout
        test_print_file
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {"key": "value"}
        self.ofile = "test/unit/gen_libs/tmp/test_dict_2_std.txt"

    @mock.patch("gen_libs.prt_dict")
    def test_print_stdout(self, mock_prt):

        """Function:  test_print_stdout

        Description:  Test with printing data to standard out.

        Arguments:

        """

        mock_prt.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.dict_2_std(self.data))

    @mock.patch("gen_libs.prt_dict")
    def test_print_file(self, mock_prt):

        """Function:  test_print_file

        Description:  Test with printing data to file.

        Arguments:

        """

        mock_prt.return_value = True

        gen_libs.dict_2_std(self.data, ofile=self.ofile)

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
