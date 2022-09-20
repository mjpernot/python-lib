# Classification (U)

"""Program:  make_dir.py

    Description:  Integration testing of make_dir in gen_libs.py.

    Usage:
        test/integration/gen_libs/make_dir.py

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
        test_create_dir_exist
        test_create_dir2
        test_create_dir
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_path = "test/integration/gen_libs/tmp"
        self.dir1 = os.path.join(self.base_path, "dir1")

    def test_create_dir_exist(self):

        """Function:  test_create_dir_exist

        Description:  Test with file exist to create directory.

        Arguments:

        """

        os.mkdir(self.dir1)

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.make_dir(self.dir1))

    def test_create_dir2(self):

        """Function:  test_create_dir2

        Description:  Test with creating directory.

        Arguments:

        """

        gen_libs.make_dir(self.dir1)

        self.assertTrue(os.path.isdir(self.dir1))

    def test_create_dir(self):

        """Function:  test_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        self.assertTrue(gen_libs.make_dir(self.dir1))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.dir1):
            os.rmdir(self.dir1)


if __name__ == "__main__":
    unittest.main()
