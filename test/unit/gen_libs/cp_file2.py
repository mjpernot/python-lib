#!/usr/bin/python
# Classification (U)

"""Program:  cp_file2.py

    Description:  Unit testing of cp_file2 in gen_libs.py.

    Usage:
        test/unit/gen_libs/cp_file2.py

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
        test_cp_file2 -> Test cp_file2 function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "src_cp_file2.txt"
        self.new_fname = "dest_cp_file2.txt"
        self.src_dir = "test/unit/gen_libs/tmp"
        self.dest_dir = "test/unit/gen_libs/tmp2"

    @mock.patch("gen_libs.shutil")
    def test_cp_file2(self, mock_util):

        """Function:  test_cp_file2

        Description:  Test copy of file in same directory.

        Arguments:

        """

        mock_util.copy2.return_value = True

        self.assertFalse(gen_libs.cp_file2(self.fname, self.src_dir,
                                           self.dest_dir, self.new_fname))


if __name__ == "__main__":
    unittest.main()
