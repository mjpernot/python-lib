#!/usr/bin/python
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
        setUp -> Unit testing initilization.
        test_list_dirs_one -> Test list one directory.
        test_list_dirs_multi -> Test list multiple directories.
        test_no_dirs -> Test with no directories.
        test_no_path -> Test with path directory that does not exist.
        tearDown -> Cleanup of unit testing.

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

        self.assertEqual(gen_libs.list_dirs(self.base_path), ["list_dir_1"])

    def test_list_dirs_multi(self):

        """Function:  test_list_dirs_multi

        Description:  Test list multiple directories.

        Arguments:

        """

        os.makedirs(self.dir_1)
        os.makedirs(self.dir_2)

        data_list = gen_libs.list_dirs(self.base_path)

        self.assertTrue(
            data_list == ["list_dir_1",
                          "list_dir_2"] or data_list == ["list_dir_2",
                                                         "list_dir_1"])

    def test_no_dirs(self):

        """Function:  test_no_dirs

        Description:  Test with no directories.

        Arguments:

        """

        self.assertEqual(gen_libs.list_dirs(self.base_path), [])

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
