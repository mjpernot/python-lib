#!/usr/bin/python
# Classification (U)

"""Program:  print_dict.py

    Description:  Unit testing of print_dict in gen_libs.py.

    Usage:
        test/unit/gen_libs/print_dict.py

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
        setUp -> Unit testing initilization.
        test_non_dict -> Test with non-dictionary object.
        test_ofile_json -> Test with ofile and json_fmt arguments.
        test_set_nostd -> Test with no_std argument.
        test_set_json -> Test with json_fmt argument.
        test_set_ofile -> Test with ofile argument.
        test_set_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {}
        self.ofile = "Out_File"
        self.json_fmt = True
        self.no_std = True

    def test_non_dict(self):

        """Function:  test_non_dict

        Description:  Test with non-dictionary object.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict([1, 2, 3]),
                         (True, "Error: [1, 2, 3] -> Is not a dictionary"))

    @mock.patch("gen_libs.dict_2_std")
    @mock.patch("gen_libs.print_data")
    def test_ofile_json(self, mock_prt, mock_std):

        """Function:  test_ofile_json

        Description:  Test with ofile and json_fmt arguments.

        Arguments:

        """

        mock_prt.return_value = True
        mock_std.return_value = True

        self.assertEqual(gen_libs.print_dict(self.data, ofile=self.ofile,
                                             json_fmt=self.json_fmt),
                         (False, None))

    @mock.patch("gen_libs.dict_2_std")
    @mock.patch("gen_libs.print_data")
    def test_set_nostd(self, mock_prt, mock_std):

        """Function:  test_set_nostd

        Description:  Test with no_std argument.

        Arguments:

        """

        mock_prt.return_value = True
        mock_std.return_value = True

        self.assertEqual(gen_libs.print_dict(self.data, no_std=self.no_std),
                         (False, None))

    @mock.patch("gen_libs.dict_2_std")
    @mock.patch("gen_libs.print_data")
    def test_set_json(self, mock_prt, mock_std):

        """Function:  test_set_json

        Description:  Test with json_fmt argument.

        Arguments:

        """

        mock_prt.return_value = True
        mock_std.return_value = True

        self.assertEqual(gen_libs.print_dict(self.data,
                                             json_fmt=self.json_fmt),
                         (False, None))

    @mock.patch("gen_libs.dict_2_std")
    @mock.patch("gen_libs.print_data")
    def test_set_ofile(self, mock_prt, mock_std):

        """Function:  test_set_ofile

        Description:  Test with ofile argument.

        Arguments:

        """

        mock_prt.return_value = True
        mock_std.return_value = True

        self.assertEqual(gen_libs.print_dict(self.data, ofile=self.ofile),
                         (False, None))

    @mock.patch("gen_libs.dict_2_std")
    @mock.patch("gen_libs.print_data")
    def test_set_default(self, mock_prt, mock_std):

        """Function:  test_set_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_prt.return_value = True
        mock_std.return_value = True

        self.assertEqual(gen_libs.print_dict(self.data), (False, None))


if __name__ == "__main__":
    unittest.main()
