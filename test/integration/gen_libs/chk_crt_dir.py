# Classification (U)

"""Program:  chk_crt_dir.py

    Description:  Unit testing of chk_crt_dir in gen_libs.py.

    Usage:
        test/integration/gen_libs/chk_crt_dir.py

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

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_dir_name
        test_dir_not_exist
        test_create_dir
        test_write_dir
        test_no_write_dir
        test_read_dir
        test_no_read_dir
        test_no_print_set
        test_print_file2
        test_print_file
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.err_mask = "Error: Directory: %s does not exist."
        self.dir_name = "TEST_DIR"
        self.file_name = "TEST_FILE"
        self.base_dir = "test/integration/gen_libs/tmp"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.d_name = os.path.join(self.test_path, self.dir_name)
        self.f_name = os.path.join(self.test_path, self.file_name)

    def test_no_dir_name(self):

        """Function:  test_no_dir_name

        Description:  Test with no directory name passed.

        Arguments:

        """

        err_msg_chk = "Error:  No value passed for directory name"
        status, err_msg = gen_libs.chk_crt_dir("", no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_dir_not_exist(self):

        """Function:  test_dir_not_exist

        Description:  Test with directory does not exist.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.d_name)
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_create_dir(self):

        """Function:  test_create_dir

        Description:  Test with creating directory.

        Arguments:

        """

        err_msg_chk = None
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, create=True,
                                               no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_write_dir(self):

        """Function:  test_write_dir

        Description:  Test with checking write permission on directory.

        Arguments:

        """

        err_msg_chk = None
        os.makedirs(self.d_name)
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, write=True,
                                               no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_write_dir(self):

        """Function:  test_no_write_dir

        Description:  Test with checking no write permission on directory.

        Arguments:

        """

        err_msg_chk = f"Error: Directory {self.d_name} is not writeable."
        os.makedirs(self.d_name)
        os.chmod(self.d_name, int("444", 8))
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, write=True,
                                               no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_read_dir(self):

        """Function:  test_read_dir

        Description:  Test with checking read permission on directory.

        Arguments:

        """

        err_msg_chk = None
        os.makedirs(self.d_name)
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, read=True,
                                               no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_read_dir(self):

        """Function:  test_no_read_dir

        Description:  Test with checking no read permission on directory.

        Arguments:

        """

        err_msg_chk = f"Error: Directory {self.d_name} is not readable."
        os.makedirs(self.d_name)
        os.chmod(self.d_name, int("333", 8))
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, read=True,
                                               no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_print_set(self):

        """Function:  test_no_print_set

        Description:  Test with no_print option set.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.d_name)
        status, err_msg = gen_libs.chk_crt_dir(self.d_name, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_print_file2(self):

        """Function:  test_print_file2

        Description:  Test with printing error messages to file.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.d_name)
        with open(self.f_name, "w", encoding="UTF-8") as f_hdlr:
            _, _ = gen_libs.chk_crt_dir(
                self.d_name, f_hdlr=f_hdlr, no_print=True)

        with open(self.f_name, "r", encoding="UTF-8") as f_hdlr:
            contents = f_hdlr.read()

        self.assertNotIn(err_msg_chk, contents)

    def test_print_file(self):

        """Function:  test_print_file

        Description:  Test with printing error messages to file.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.d_name)
        with open(self.f_name, "w", encoding="UTF-8") as f_hdlr:
            status, err_msg = gen_libs.chk_crt_dir(
                self.d_name, f_hdlr=f_hdlr, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.d_name):
            os.rmdir(self.d_name)

        if os.path.isfile(self.f_name):
            os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()
