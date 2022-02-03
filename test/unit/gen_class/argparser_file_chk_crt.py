#!/usr/bin/python
# Classification (U)

"""Program:  argparser_file_chk_crt.py

    Description:  Unit testing of _file_chk_crt in gen_class.ArgParser class.

    Usage:
        test/unit/gen_class/argparser_file_chk_crt.py

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


class FileOpen3(object):

    """Class:  FileOpen3

    Description:  Class stub holder for file open class.

    Methods:
        close

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:

        """

        raise IOError(2, "Some Error")


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
        test_file_crt_override
        test_open_fail
        test_open_success
        test_errno_not_two
        test_errno_two
        test_errno_two_success
        test_option_not_in_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.argv = ["program.py", "-f", "/dir_path/file1"]
        self.opt_val = ["-f", "-a"]
        self.file_crt = ["-f", "-g"]
        self.file_crt2 = ["-g"]
        self.option = "-f"
        self.open = FileOpen()
        self.open2 = FileOpen2()
        self.open3 = FileOpen3()

    @mock.patch("__builtin__.open")
    def test_file_crt_override(self, mock_open):

        """Function:  test_file_crt_override

        Description:  Test with passing file_crt to override.

        Arguments:

        """

        mock_open.side_effect = [self.open3, self.open]

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt2,
            do_parse=True)

        self.assertTrue(
            args_array._file_chk_crt(
                args_array.args_array[self.option], self.option,
                file_crt=self.file_crt))

    @mock.patch("__builtin__.open")
    def test_open_fail(self, mock_open):

        """Function:  test_open_fail

        Description:  Test with file open returning failure.

        Arguments:

        """

        mock_open.return_value = self.open2

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(
                args_array._file_chk_crt(
                    args_array.args_array[self.option], self.option))

    @mock.patch("__builtin__.open")
    def test_open_success(self, mock_open):

        """Function:  test_open_success

        Description:  Test with file open returning successful.

        Arguments:

        """

        mock_open.return_value = self.open

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt,
            do_parse=True)

        self.assertTrue(
            args_array._file_chk_crt(
                args_array.args_array[self.option], self.option))

    @mock.patch("__builtin__.open")
    def test_errno_not_two(self, mock_open):

        """Function:  test_errno_not_two

        Description:  Test with errno not set to two.

        Arguments:

        """

        mock_open.return_value = self.open2

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(
                args_array._file_chk_crt(
                    args_array.args_array[self.option], self.option))

    @mock.patch("__builtin__.open")
    def test_errno_two(self, mock_open):

        """Function:  test_errno_two

        Description:  Test with errno set to two.

        Arguments:

        """

        mock_open.side_effect = [self.open3, self.open2]

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(
                args_array._file_chk_crt(
                    args_array.args_array[self.option], self.option))

    @mock.patch("__builtin__.open")
    def test_errno_two_success(self, mock_open):

        """Function:  test_errno_two_success

        Description:  Test with file failing with err 2 and then opening.

        Arguments:

        """

        mock_open.side_effect = [self.open3, self.open]

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt,
            do_parse=True)

        self.assertTrue(
            args_array._file_chk_crt(
                args_array.args_array[self.option], self.option))

    @mock.patch("__builtin__.open")
    def test_option_not_in_list(self, mock_open):

        """Function:  test_option_not_in_list

        Description:  Test with option not being in file_crt_list.

        Arguments:

        """

        mock_open.return_value = self.open3

        args_array = gen_class.ArgParser(
            self.argv, opt_val=self.opt_val, file_crt=self.file_crt2,
            do_parse=True)

        with gen_libs.no_std_out():
            self.assertFalse(
                args_array._file_chk_crt(
                    args_array.args_array[self.option], self.option))


if __name__ == "__main__":
    unittest.main()
