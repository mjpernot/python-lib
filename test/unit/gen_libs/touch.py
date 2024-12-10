# Classification (U)

"""Program:  touch.py

    Description:  Unit testing of touch in gen_libs.py.

    Usage:
        test/unit/gen_libs/touch.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_touch_file
        test_existing_file
        test_create_path
        test_dir_create_fail
        test_file_create_fail
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.file = "touch.txt"
        self.base_path = "test/unit/gen_libs/tmp"
        self.file_name = os.path.join(self.base_path, self.file)
        self.exist_file = "test/unit/gen_libs/testfiles/touch.txt"
        self.dir_create = os.path.join(self.base_path, "touch", self.file)
        self.dir_path = os.path.join(self.base_path, "touch_fail")
        self.dir_fail = os.path.join(self.dir_path, "touch", self.file)
        self.file_fail = os.path.join(self.dir_path, self.file)

        self.file_msg = "ERROR: File create failure. Reason: Permission denied"
        self.dir_msg = \
            "ERROR: Directory create failure. Reason: Permission denied"

    def test_touch_file(self):

        """Function:  test_touch_file

        Description:  Test creating file.

        Arguments:

        """

        status, msg = gen_libs.touch(self.file_name)
        f_status = os.stat(self.file_name).st_size == 0
        self.assertEqual((status, msg, f_status), (True, None, True))

    def test_existing_file(self):

        """Function:  test_existing_file

        Description:  Test on existing file.

        Arguments:

        """

        status, msg = gen_libs.touch(self.exist_file)
        f_status = os.stat(self.exist_file).st_size > 0
        self.assertEqual((status, msg, f_status), (True, None, True))

    def test_create_path(self):

        """Function:  test_create_path

        Description:  Test creating part of path to file.

        Arguments:

        """

        self.assertEqual((gen_libs.touch(self.dir_create)), (True, None))

    def test_dir_create_fail(self):

        """Function:  test_dir_create_fail

        Description:  Test failure to create direcory path.

        Arguments:

        """

        os.makedirs(self.dir_path)
        os.chmod(self.dir_path, int("444", 8))

        self.assertEqual((gen_libs.touch(self.dir_fail)),
                         (False, self.dir_msg))

    def test_file_create_fail(self):

        """Function:  test_file_create_fail

        Description:  Test failure to create file.

        Arguments:

        """

        os.makedirs(self.dir_path)
        os.chmod(self.dir_path, int("444", 8))

        self.assertEqual((gen_libs.touch(self.file_fail)),
                         (False, self.file_msg))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file_name):
            os.remove(self.file_name)

        if os.path.isdir(os.path.join(self.base_path, "touch")):
            shutil.rmtree(os.path.join(self.base_path, "touch"))

        if os.path.isdir(self.dir_path):
            os.chmod(self.dir_path, int("755", 8))
            shutil.rmtree(self.dir_path)


if __name__ == "__main__":
    unittest.main()
