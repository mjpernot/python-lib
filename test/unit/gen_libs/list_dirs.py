# Classification (U)

"""Program:  list_dirs.py

    Description:  Unit testing of list_dirs in gen_libs.py.

    Usage:
        test/unit/gen_libs/list_dirs.py

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
        test_list_dirs_one
        test_list_dirs_multi
        test_no_dirs
        test_no_path
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_path = "test/unit/gen_libs/tmp"
        self.dir_1 = os.path.join(self.base_path, "list_dir_1")
        self.dir_2 = os.path.join(self.base_path, "list_dir_2")
        self.dir_fail = os.path.join(self.base_path, "not_exist")

    def test_list_dirs_one(self):

        """Function:  test_list_dirs_one

        Description:  Test list one directory.

        Arguments:

        """

        os.makedirs(self.dir_1)
        dirs = gen_libs.list_dirs(self.base_path)

        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        self.assertEqual(dirs, ["list_dir_1"])

    def test_list_dirs_multi(self):

        """Function:  test_list_dirs_multi

        Description:  Test list multiple directories.

        Arguments:

        """

        os.makedirs(self.dir_1)
        os.makedirs(self.dir_2)
        data_list = gen_libs.list_dirs(self.base_path)

        if "__pycache__" in data_list:
            data_list.remove("__pycache__")

        self.assertIn(
            data_list,
            (['list_dir_1', 'list_dir_2'], ['list_dir_2', 'list_dir_1']))

    def test_no_dirs(self):

        """Function:  test_no_dirs

        Description:  Test with no directories.

        Arguments:

        """

        dirs = gen_libs.list_dirs(self.base_path)

        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        self.assertEqual(dirs, [])

    def test_no_path(self):

        """Function:  test_no_path

        Description:  Test with path directory that does not exist.

        Arguments:

        """

        self.assertEqual(gen_libs.list_dirs(self.dir_fail), [])

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.dir_1):
            os.rmdir(self.dir_1)

        if os.path.isdir(self.dir_2):
            os.rmdir(self.dir_2)


if __name__ == "__main__":
    unittest.main()
