#!/usr/bin/python
# Classification (U)

"""Program:  _make_dir.py

    Description:  Unit testing of _make_dir in arg_parser.py.

    Usage:
        test/unit/arg_parser/_make_dir.py

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
import arg_parser
import gen_libs
import version

__version__ = version.__version__


def raise_oserror(dirname):

    """Function:  raise_oserror

    Description:  Stub holder to return a raised OSError exception.

    Arguments:

    """

    if dirname == "/dir/path/dirname":
        raise OSError(21, "Other Error")

    elif dirname == "/dir/path/dirname13":
        raise OSError(13, "Permission denied")

    elif dirname == "/dir/path/dirname17":
        raise OSError(17, "File exist")


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_create_dir_exist
        test_create_dir_perm
        test_create_dir_fail
        test_create_dir

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dirname = "/dir/path/dirname"
        self.dirname13 = "/dir/path/dirname13"
        self.dirname17 = "/dir/path/dirname17"
        self.status = False

    @mock.patch("arg_parser.os")
    def test_create_dir_exist(self, mock_os):

        """Function:  test_create_dir_exist

        Description:  Test with file exist to create directory.

        Arguments:

        """

        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._make_dir(self.dirname17, self.status))

    @mock.patch("arg_parser.os")
    def test_create_dir_perm(self, mock_os):

        """Function:  test_create_dir_perm

        Description:  Test with permission denied to create directory.

        Arguments:

        """

        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._make_dir(self.dirname13, self.status))

    @mock.patch("arg_parser.os")
    def test_create_dir_fail(self, mock_os):

        """Function:  test_create_dir_fail

        Description:  Test with failing to create directory.

        Arguments:

        """

        mock_os.makedirs = raise_oserror

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._make_dir(self.dirname, self.status))

    @mock.patch("arg_parser.os")
    def test_create_dir(self, mock_os):

        """Function:  test_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        mock_os.makedirs.return_value = True

        self.assertFalse(arg_parser._make_dir(self.dirname, self.status))


if __name__ == "__main__":
    unittest.main()
