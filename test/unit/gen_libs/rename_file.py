# Classification (U)

"""Program:  rename_file.py

    Description:  Unit testing of rename_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/rename_file.py

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
        test_rename_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "File1"
        self.new_fname = "New_File1"
        self.dir_path = "/Dir_Path/"

    @mock.patch("gen_libs.os")
    def test_rename_file(self, mock_os):

        """Function:  test_rename_file

        Description:  Test rename_file function.

        Arguments:

        """

        mock_os.rename.return_value = True

        self.assertFalse(gen_libs.rename_file(self.fname, self.new_fname,
                                              self.dir_path))


if __name__ == "__main__":
    unittest.main()
