# Classification (U)

"""Program:  crt_file_time.py

    Description:  Unit testing of crt_file_time in gen_libs.py.

    Usage:
        test/unit/gen_libs/crt_file_time.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_true_seconds
        test_false_seconds
        test_default_seconds
        test_no_trailing_slash
        test_trailing_slash
        test_ext_no_sep
        test_no_ext
        test_crt_file_time

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.indate = "20190610_0415"
        self.indate2 = "20220321_113545"
        self.fname = "File_name"
        self.path = "/dir/path"
        self.path2 = "/dir/path/"
        self.ext = ".txt"
        self.ext2 = "txt"
        self.result = "/dir/path/File_name.20190610_0415.txt"
        self.result2 = "/dir/path/File_name.20190610_0415"
        self.result3 = "/dir/path/File_name.20220321_113545"

    @mock.patch("gen_libs.time")
    def test_true_seconds(self, mock_date):

        """Function:  test_true_seconds

        Description:  Test with option setting for secs set to True.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate2

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path, secs=True), self.result3)

    @mock.patch("gen_libs.time")
    def test_false_seconds(self, mock_date):

        """Function:  test_false_seconds

        Description:  Test with option setting for secs set to False.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path, self.ext, secs=False), self.result)

    @mock.patch("gen_libs.time")
    def test_default_seconds(self, mock_date):

        """Function:  test_default_seconds

        Description:  Test with default option setting for secs.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path, self.ext), self.result)

    @mock.patch("gen_libs.time")
    def test_no_trailing_slash(self, mock_date):

        """Function:  test_no_trailing_slash

        Description:  Test with no trailing slash in path.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path, self.ext2), self.result)

    @mock.patch("gen_libs.time")
    def test_trailing_slash(self, mock_date):

        """Function:  test_trailing_slash

        Description:  Test with trailing slash in path.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path2, self.ext2), self.result)

    @mock.patch("gen_libs.time")
    def test_ext_no_sep(self, mock_date):

        """Function:  test_ext_no_sep

        Description:  Test with no seperator in extension.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path, self.ext2), self.result)

    @mock.patch("gen_libs.time")
    def test_no_ext(self, mock_date):

        """Function:  test_no_ext

        Description:  Test with no extension passed.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(self.fname, self.path), self.result2)

    @mock.patch("gen_libs.time")
    def test_crt_file_time(self, mock_date):

        """Function:  test_crt_file_time

        Description:  Test crt_file_time function.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(
            gen_libs.crt_file_time(
                self.fname, self.path, self.ext), self.result)


if __name__ == "__main__":
    unittest.main()
