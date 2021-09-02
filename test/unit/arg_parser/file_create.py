#!/usr/bin/python
# Classification (U)

"""Program:  file_create.py

    Description:  Unit testing of _file_create in arg_parser.py.

    Usage:
        test/unit/arg_parser/file_create.py

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


class FileOpen2(object):

    """Class:  FileOpen2

    Description:  Class stub holder for file open class.

    Methods:
        close

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:

        """

        raise IOError(10, "Some Error")


class FileOpen(object):

    """Class:  FileOpen

    Description:  Class stub holder for file open class.

    Methods:
        close

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_open_fail
        test_open_success
        test_errno_not_two
        test_option_not_in_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.option = "-f"
        self.file_crt_list = ["-f", "-g"]
        self.errno = 2
        self.strerror = "No file"
        self.name = "/dir_path/file1"
        self.exit_flag = False
        self.open = FileOpen()
        self.open2 = FileOpen2()

    @mock.patch("arg_parser.open")
    def test_open_fail(self, mock_open):

        """Function:  test_open_fail

        Description:  Test with file open returning failure.

        Arguments:

        """

        mock_open.return_value = self.open2

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(self.name, self.option,
                                                    self.file_crt_list,
                                                    self.errno, self.strerror,
                                                    self.exit_flag))

    @mock.patch("arg_parser.open")
    def test_open_success(self, mock_open):

        """Function:  test_open_success

        Description:  Test with file open returning successful.

        Arguments:

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser._file_create(self.name, self.option,
                                                 self.file_crt_list,
                                                 self.errno, self.strerror,
                                                 self.exit_flag))

    def test_errno_not_two(self):

        """Function:  test_errno_not_two

        Description:  Test with errno not set to two.

        Arguments:

        """

        self.errno = 10

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(self.name, self.option,
                                                    self.file_crt_list,
                                                    self.errno, self.strerror,
                                                    self.exit_flag))

    def test_option_not_in_list(self):

        """Function:  test_option_not_in_list

        Description:  Test with option not being in file_crt_list.

        Arguments:

        """

        self.option = "-a"

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(self.name, self.option,
                                                    self.file_crt_list,
                                                    self.errno, self.strerror,
                                                    self.exit_flag))


if __name__ == "__main__":
    unittest.main()
