# Classification (U)

"""Program:  perm_check.py

    Description:  Unit testing of perm_check in gen_libs.py.

    Usage:
        test/unit/gen_libs/perm_check.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


# Global
PERM1 = "777"
PERM2 = "444"
PERM3 = "222"
PERM4 = "111"
PERM5 = "333"
PERM6 = "000"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_exe_file
        test_no_exe_file
        test_multiple_errors3
        test_multiple_errors2
        test_multiple_errors
        test_write_file
        test_no_write_file
        test_read_file
        test_no_read_file
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.err_mask = "Error:  File %s does not exist."
        self.file_name = "TEST_FILE"
        self.base_dir = "test/unit/gen_libs/tmp"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.f_name = os.path.join(self.test_path, self.file_name)
        self.l_name = os.path.join(self.test_path, "TEST_LOG")
        self.prt_template = "\nError:  File %s does not exist."
        self.prt_template2 = "\nError: File %s is not writeable."
        self.prt_template3 = "\nError: File %s is not readable."
        self.prt_template4 = "\nError: File %s is not executable."

    def test_exe_file(self):

        """Function:  test_exe_file

        Description:  Test with checking execute permission on file.

        Arguments:

        """

        global PERM1

        err_msg_chk = ""
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM1, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, exe=True)
        f_hdlr.close()

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_exe_file(self):

        """Function:  test_no_exe_file

        Description:  Test with checking no execute permission on file.

        Arguments:

        """

        global PERM6

        err_msg_chk = self.prt_template4 % (self.f_name)
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM6, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, exe=True)
        f_hdlr.close()

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors3(self):

        """Function:  test_multiple_errors3

        Description:  Test with write and execute errors.

        Arguments:

        """

        global PERM2

        err_msg_chk = self.prt_template2 % (self.f_name)
        err_msg_chk2 = self.prt_template4 % (self.f_name)
        err_msg_chk = "".join([err_msg_chk, err_msg_chk2])
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM2, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, exe=True, write=True)
        f_hdlr.close()

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors2(self):

        """Function:  test_multiple_errors2

        Description:  Test with read and execute errors.

        Arguments:

        """

        global PERM3

        err_msg_chk = self.prt_template3 % (self.f_name)
        err_msg_chk2 = self.prt_template4 % (self.f_name)
        err_msg_chk = "".join([err_msg_chk, err_msg_chk2])
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM3, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, exe=True, read=True)
        f_hdlr.close()

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors(self):

        """Function:  test_multiple_errors

        Description:  Test with read and write errors.

        Arguments:

        """

        global PERM4

        err_msg_chk = self.prt_template2 % (self.f_name)
        err_msg_chk2 = self.prt_template3 % (self.f_name)
        err_msg_chk = "".join([err_msg_chk, err_msg_chk2])
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM4, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, write=True, read=True)
        f_hdlr.close()

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test with checking write permission on file.

        Arguments:

        """

        err_msg_chk = ""
        open(self.f_name, "a").close()
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, write=True)
        f_hdlr.close()

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_write_file(self):

        """Function:  test_no_write_file

        Description:  Test with checking no write permission on file.

        Arguments:

        """

        global PERM2

        err_msg_chk = self.prt_template2 % (self.f_name)
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM2, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, write=True)
        f_hdlr.close()

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_read_file(self):

        """Function:  test_read_file

        Description:  Test with checking read permission on file.

        Arguments:

        """

        err_msg_chk = ""
        open(self.f_name, "a").close()
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, read=True)
        f_hdlr.close()

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_read_file(self):

        """Function:  test_no_read_file

        Description:  Test with checking no read permission on file.

        Arguments:

        """

        global PERM5

        err_msg_chk = self.prt_template3 % (self.f_name)
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM5, 8))
        f_hdlr = open(os.devnull, "w")
        status, err_msg = gen_libs.perm_check(
            self.f_name, "File", f_hdlr, read=True)
        f_hdlr.close()

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.f_name):
            os.remove(self.f_name)

        if os.path.isfile(self.l_name):
            os.remove(self.l_name)


if __name__ == "__main__":
    unittest.main()
