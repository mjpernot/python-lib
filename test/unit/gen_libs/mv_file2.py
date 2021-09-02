#!/usr/bin/python
# Classification (U)

"""Program:  mv_file2.py

    Description:  Unit testing of mv_file2 in gen_libs.py.

    Usage:
        test/unit/gen_libs/mv_file2.py

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
        test_default_set
        test_mv_file2

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.src_file_path = "/Path/File_Name"
        self.des_path = "/Dest_Path"
        self.new_fname = "New_File_Name"

    @mock.patch("gen_libs.shutil")
    def test_default_set(self, mock_move):

        """Function:  test_default_set

        Description:  Test with default setting.

        Arguments:

        """

        mock_move.move.return_value = True

        self.assertFalse(gen_libs.mv_file2(self.src_file_path, self.des_path))

    @mock.patch("gen_libs.shutil")
    def test_mv_file2(self, mock_move):

        """Function:  test_mv_file2

        Description:  Test mv_file2 function.

        Arguments:

        """

        mock_move.move.return_value = True

        self.assertFalse(gen_libs.mv_file2(self.src_file_path, self.des_path,
                                           self.new_fname))


if __name__ == "__main__":
    unittest.main()
