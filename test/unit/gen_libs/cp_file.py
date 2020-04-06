#!/usr/bin/python
# Classification (U)

"""Program:  cp_file.py

    Description:  Unit testing of cp_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/cp_file.py

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
        test_cp_file -> Test copy of file in same directory.
        test_cp_file_dir -> Test copy of file in different directory.
        test_cp_file_same -> Test copy of file to same name.
        test_cp_file_diff -> Test copy of file to different name.
        test_fail_src_dir -> Test failure on missing source directory.
        test_fail_src_file -> Test failure on missing source file.
        test_fail_dest_dir -> Test failure on missing destination directory.
        test_fail_dest_perm -> Test failure on directory permission.
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.err_mask = "No such file or directory: %s"
        self.base_path = "test/unit/gen_libs/tmp"
        self.cp_file_dir = os.path.join(self.base_path, "cp_file_dir")
        self.cp_file_dir2 = os.path.join(self.base_path, "cp_file_dir2")
        self.dir_fail = os.path.join(self.base_path, "not_cp_file_dir")
        self.src_file = "src_cp_file.txt"
        self.dest_file = "src_cp_file2.txt"

        gen_libs.touch(os.path.join(self.cp_file_dir, self.src_file))

    def test_cp_file(self):

        """Function:  test_cp_file

        Description:  Test copy of file in same directory.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir,
                                           self.cp_file_dir, self.dest_file)),
                         (True, None))

    def test_cp_file_dir(self):

        """Function:  test_cp_file_dir

        Description:  Test copy of file in different directory.

        Arguments:

        """

        gen_libs.touch(os.path.join(self.cp_file_dir2, "testme"))

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir,
                                           self.cp_file_dir2, self.dest_file)),
                         (True, None))

    def test_cp_file_same(self):

        """Function:  test_cp_file_same

        Description:  Test copy of file to same name.

        Arguments:

        """

        gen_libs.touch(os.path.join(self.cp_file_dir2, "testme"))

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir,
                                           self.cp_file_dir2)), (True, None))

    def test_cp_file_diff(self):

        """Function:  test_cp_file_diff

        Description:  Test copy of file to different name.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir,
                                           self.cp_file_dir, self.dest_file)),
                         (True, None))

    def test_fail_src_dir(self):

        """Function:  test_fail_src_dir

        Description:  Test failure on missing source directory.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir2,
                                           self.cp_file_dir, self.dest_file)),
                         (False, self.err_mask % (self.cp_file_dir2)))

    def test_fail_src_file(self):

        """Function:  test_fail_src_file

        Description:  Test failure on missing source file.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_file(self.dest_file, self.cp_file_dir,
                                           self.cp_file_dir, self.src_file)),
                         (False, self.err_mask
                          % (os.path.join(self.cp_file_dir, self.dest_file))))

    def test_fail_dest_dir(self):

        """Function:  test_fail_dest_dir

        Description:  Test failure on missing destination directory.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir,
                                           self.cp_file_dir2, self.dest_file)),
                         (False, self.err_mask % (self.cp_file_dir2)))

    def test_fail_dest_perm(self):

        """Function:  test_fail_dest_perm

        Description:  Test failure on directory permission.

        Arguments:

        """

        gen_libs.touch(os.path.join(self.cp_file_dir2, self.src_file))
        os.chmod(self.cp_file_dir2, 0444)

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir,
                                           self.cp_file_dir2, self.dest_file)),
                         (False, "Permission denied"))

    @mock.patch("os.path.isdir", mock.Mock(return_value=True))
    @mock.patch("os.path.isfile", mock.Mock(return_value=True))
    def test_fail_else(self):

        """Function:  test_fail_else

        Description:  Test failure for if statement else clause.

        Arguments:

        """

        self.assertEqual((gen_libs.cp_file(self.src_file, self.cp_file_dir2,
                                           self.cp_file_dir, self.dest_file)),
                         (False, "No such file or directory"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        shutil.rmtree(self.cp_file_dir)

        if os.path.isdir(self.cp_file_dir2):
            os.chmod(self.cp_file_dir2, 0755)
            shutil.rmtree(self.cp_file_dir2)


if __name__ == "__main__":
    unittest.main()
