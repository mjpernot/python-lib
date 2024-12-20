# Classification (U)

"""Program:  file_cleanup.py

    Description:  Unit testing of file_cleanup in gen_libs.py.

    Usage:
        test/unit/gen_libs/file_cleanup.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_no_removal
        test_remove_file
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir_path = "test/unit/gen_libs/tmp/tmp"
        os.makedirs(self.dir_path)
        self.fname = os.path.join(self.dir_path, "file1.txt")

        with open(self.fname, "w", encoding="UTF-8"):
            os.utime(self.fname, None)

    def test_no_removal(self):

        """Function:  test_no_removal

        Description:  Test with no files to remove.

        Arguments:

        """

        gen_libs.file_cleanup(self.dir_path, 1)

        self.assertTrue(os.path.isfile(self.fname))

    def test_remove_file(self):

        """Function:  test_remove_file

        Description:  Test with removing old file.

        Arguments:

        """

        gen_libs.file_cleanup(self.dir_path, 0)

        if os.path.isfile(self.fname):
            status = False

        else:
            status = True

        self.assertTrue(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.fname):
            os.remove(self.fname)

        os.rmdir(self.dir_path)


if __name__ == "__main__":
    unittest.main()
