#!/usr/bin/python
# Classification (U)

"""Program:  write_file2.py

    Description:  Unit testing of write_file2 in gen_libs.py.

    Usage:
        test/unit/gen_libs/write_file2.py

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
        test_with_no_args -> Test with no arguments passed.
        test_with_fhandle_none -> Test with f_handle set to None.
        test_with_line_none -> Test with line set to None.
        test_with_data -> Test with data passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_handle = "File_Handler"
        self.line = "Text_Message"

    def test_with_no_args(self):

        """Function:  test_with_no_args

        Description:  Test with no arguments passed.

        Arguments:

        """

        self.assertFalse(gen_libs.write_file2())

    def test_with_fhandle_none(self):

        """Function:  test_with_fhandle_none

        Description:  Test with f_handle set to None.

        Arguments:

        """

        self.assertFalse(gen_libs.write_file2(f_handle=self.f_handle))

    def test_with_line_none(self):

        """Function:  test_with_line_none

        Description:  Test with line set to None.

        Arguments:

        """

        self.assertFalse(gen_libs.write_file2(line=self.line))

    @mock.patch("gen_libs.print")
    def test_with_data(self, mock_print):

        """Function:  test_with_data

        Description:  Test with data passed.

        Arguments:

        """

        mock_print.return_value = True

        self.assertFalse(gen_libs.write_file2(self.f_handle, self.line))


if __name__ == "__main__":
    unittest.main()
