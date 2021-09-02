#!/usr/bin/python
# Classification (U)

"""Program:  make_zip.py

    Description:  Unit testing of make_zip in gen_libs.py.

    Usage:
        test/unit/gen_libs/make_zip.py

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


class ZipFile(object):

    """Class:  ZipFile

    Description:  Class which is a representation of the zipfile class.

    Methods:
        __init__
        write
        close

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

        self.in_fname = None
        self.out_fname = None

    def write(self, in_fname, out_fname=None):

        """Method:  write

        Description:  Mock representation of zipfile.ZipFile.write method.

        Arguments:
            (input) in_fname
            (input) out_fname

        """

        self.in_fname = in_fname
        self.out_fname = out_fname

        return True

    def close(self):

        """Method:  close

        Description:  Mock representation of zipfile.ZipFile.close method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_path_sep
        test_relative_path
        test_abs_path

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.zip_file_path = "/destination/path/file.zip"
        self.cur_file_dir = "/source/directory/path/"
        self.cur_file_dir2 = "/source/directory/path"
        self.files_to_zip = ["File1", "File2", "File3"]
        self.is_rel_path = True

    @mock.patch("gen_libs.zipfile.ZipFile")
    def test_path_sep(self, mock_zip):

        """Function:  test_path_sep

        Description:  Test missing path seperator.

        Arguments:

        """

        mock_zip.return_value = ZipFile()

        self.assertFalse(gen_libs.make_zip(self.zip_file_path,
                                           self.cur_file_dir2,
                                           self.files_to_zip,
                                           self.is_rel_path))

    @mock.patch("gen_libs.zipfile.ZipFile")
    def test_relative_path(self, mock_zip):

        """Function:  test_relative_path

        Description:  Test the relative path way.

        Arguments:

        """

        mock_zip.return_value = ZipFile()

        self.assertFalse(gen_libs.make_zip(self.zip_file_path,
                                           self.cur_file_dir,
                                           self.files_to_zip,
                                           self.is_rel_path))

    @mock.patch("gen_libs.zipfile.ZipFile")
    def test_abs_path(self, mock_zip):

        """Function:  test_abs_path

        Description:  Test the absolute path way.

        Arguments:

        """

        mock_zip.return_value = ZipFile()

        self.assertFalse(gen_libs.make_zip(self.zip_file_path,
                                           self.cur_file_dir,
                                           self.files_to_zip))


if __name__ == "__main__":
    unittest.main()
