#!/usr/bin/python
# Classification (U)

"""Program:  cp_dir.py

    Description:  Unit testing of cp_dir in gen_libs.py.

    Usage:
        test/unit/gen_libs/cp_dir.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil

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
        test_cp_dir -> Test copy of directory to another directory.
        test_cp_dir_same -> Test copy of directory to same name.
        test_fail_src_dir -> Test failure on missing source directory.
        test_fail_dest_dir -> Test failure on destination dir already exists.
        test_fail_dest_perm -> Test failure on directory permission.
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_path = "test/unit/gen_libs/tmp"
        self.cp_dir_dir = os.path.join(self.base_path, "cp_dir_dir")
        self.cp_dir_dir2 = os.path.join(self.base_path, "cp_dir_dir2")

    def test_cp_dir(self):

        """Function:  test_cp_dir

        Description:  Test copy of file in same directory.

        Arguments:

        """

        os.makedirs(self.cp_dir_dir)

        self.assertEqual((gen_libs.cp_dir(self.cp_dir_dir, self.cp_dir_dir2)),
                         (True, None))

    def test_cp_dir_same(self):

        """Function:  test_cp_dir_same

        Description:  Test copy of directory to same name.

        Arguments:

        """

        os.makedirs(self.cp_dir_dir)

        self.assertEqual((gen_libs.cp_dir(self.cp_dir_dir, self.cp_dir_dir)), (
            False, "Directory not copied.  Exist Error Message: [Errno 17] "
            "File exists: '%s'" % (self.cp_dir_dir)))

    def test_fail_src_dir(self):

        """Function:  test_fail_src_dir

        Description:  Test failure on missing source directory.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_dir(
            self.cp_dir_dir, self.cp_dir_dir2)), (
                False, "Directory not copied.  Exist Error Message: [Errno 2] "
                "No such file or directory: '%s'" % (self.cp_dir_dir)))

    def test_fail_dest_dir(self):

        """Function:  test_fail_dest_dir

        Description:  Test failure on destination directory already exists.

        Arguments:

        """

        os.makedirs(self.cp_dir_dir)
        os.makedirs(self.cp_dir_dir2)

        self.assertEqual((gen_libs.cp_dir(
            self.cp_dir_dir, self.cp_dir_dir2)), (
                False,
                "Directory not copied.  Exist Error Message: [Errno 17] "
                "File exists: '%s'" % (self.cp_dir_dir2)))

    def test_fail_dest_perm(self):

        """Function:  test_fail_dest_perm

        Description:  Test failure on directory permission.

        Arguments:

        """

        os.makedirs(self.cp_dir_dir)
        os.chmod(self.cp_dir_dir, 0000)

        self.assertEqual((gen_libs.cp_dir(
            self.cp_dir_dir, self.cp_dir_dir2)), (
                False,
                "Directory not copied.  Exist Error Message: [Errno 13] "
                "Permission denied: '%s'" % (self.cp_dir_dir)))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.cp_dir_dir):
            os.chmod(self.cp_dir_dir, 0755)
            shutil.rmtree(self.cp_dir_dir)

        if os.path.isdir(self.cp_dir_dir2):
            shutil.rmtree(self.cp_dir_dir2)


if __name__ == "__main__":
    unittest.main()
