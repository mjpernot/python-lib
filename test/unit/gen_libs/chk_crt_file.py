# Classification (U)

"""Program:  chk_crt_file.py

    Description:  Unit testing of chk_crt_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/chk_crt_file.py

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
        test_exe_file
        test_no_exe_file
        test_multiple_errors6
        test_multiple_errors5
        test_multiple_errors4
        test_multiple_errors3
        test_multiple_errors2
        test_multiple_errors
        test_no_file_name
        test_file_not_exist
        test_create_file
        test_write_file
        test_no_write_file
        test_read_file
        test_no_read_file
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

        self.err_mask = "Error:  File %s does not exist."
        self.file_name = "TEST_FILE"
        self.base_dir = "test/unit/gen_libs/tmp"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.f_name = os.path.join(self.test_path, self.file_name)
        self.l_name = os.path.join(self.test_path, "TEST_LOG")
        self.prt_template = "Error:  File %s does not exist."
        self.prt_template2 = "Error: File %s is not writeable."
        self.prt_template3 = "Error: File %s is not readable."
        self.prt_template4 = "Error: File %s is not executable."

    def test_exe_file(self):

        """Function:  test_exe_file

        Description:  Test with checking execute permission on file.

        Arguments:

        """

        err_msg_chk = None
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("755", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, exe=True, no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_exe_file(self):

        """Function:  test_no_exe_file

        Description:  Test with checking no execute permission on file.

        Arguments:

        """

        err_msg_chk = self.prt_template4 % (self.f_name)
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("444", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, exe=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors6(self):

        """Function:  test_multiple_errors6

        Description:  Test with write and execute errors.

        Arguments:

        """

        err_msg_chk = self.prt_template2 % (self.f_name)
        err_msg_chk2 = self.prt_template4 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk = err_msg_chk.strip("\n")
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("444", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, exe=True, write=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors5(self):

        """Function:  test_multiple_errors5

        Description:  Test with read and execute errors.

        Arguments:

        """

        err_msg_chk = self.prt_template3 % (self.f_name)
        err_msg_chk2 = self.prt_template4 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk = err_msg_chk.strip("\n")
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("222", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, exe=True, read=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors4(self):

        """Function:  test_multiple_errors4

        Description:  Test with exist, read, and write errors.

        Arguments:

        """

        err_msg_chk = self.prt_template % (self.f_name)
        err_msg_chk2 = self.prt_template2 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk2 = self.prt_template3 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk = err_msg_chk.strip("\n")
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, read=True, write=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors3(self):

        """Function:  test_multiple_errors3

        Description:  Test with exist and write errors.

        Arguments:

        """

        err_msg_chk = self.prt_template % (self.f_name)
        err_msg_chk2 = self.prt_template2 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk = err_msg_chk.strip("\n")
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, write=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors2(self):

        """Function:  test_multiple_errors2

        Description:  Test with exist and read errors.

        Arguments:

        """

        err_msg_chk = self.prt_template % (self.f_name)
        err_msg_chk2 = self.prt_template3 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk = err_msg_chk.strip("\n")
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, read=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_multiple_errors(self):

        """Function:  test_multiple_errors

        Description:  Test with read and write errors.

        Arguments:

        """

        err_msg_chk = self.prt_template2 % (self.f_name)
        err_msg_chk2 = self.prt_template3 % (self.f_name)
        err_msg_chk = "\n".join([err_msg_chk, err_msg_chk2])
        err_msg_chk = err_msg_chk.strip("\n")
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("111", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, write=True, read=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_file_name(self):

        """Function:  test_no_file_name

        Description:  Test with no file name passed.

        Arguments:

        """

        err_msg_chk = "Error:  No value passed for filename."
        status, err_msg = gen_libs.chk_crt_file("", no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_file_not_exist(self):

        """Function:  test_file_not_exist

        Description:  Test with file does not exist.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.f_name)
        status, err_msg = gen_libs.chk_crt_file(self.f_name, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_create_file(self):

        """Function:  test_create_file

        Description:  Test with creating file.

        Arguments:

        """

        err_msg_chk = None
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, create=True, no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test with checking write permission on file.

        Arguments:

        """

        err_msg_chk = None
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, write=True, no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_write_file(self):

        """Function:  test_no_write_file

        Description:  Test with checking no write permission on file.

        Arguments:

        """

        err_msg_chk = self.prt_template2 % (self.f_name)
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("444", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, write=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_read_file(self):

        """Function:  test_read_file

        Description:  Test with checking read permission on file.

        Arguments:

        """

        err_msg_chk = None
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, read=True, no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_read_file(self):

        """Function:  test_no_read_file

        Description:  Test with checking no read permission on file.

        Arguments:

        """

        err_msg_chk = self.prt_template3 % (self.f_name)
        open(                                       # pylint:disable=R1732
            self.f_name, "a", encoding="UTF-8").close()
        os.chmod(self.f_name, int("333", 8))
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, read=True, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_print_set(self):

        """Function:  test_no_print_set

        Description:  Test with no_print option set.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.f_name)
        status, err_msg = gen_libs.chk_crt_file(self.f_name, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_print_file2(self):

        """Function:  test_print_file2

        Description:  Test with printing error messages to file.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.f_name)
        f_hdlr = open(                                  # pylint:disable=R1732
            self.l_name, "w", encoding="UTF-8")
        _, _ = gen_libs.chk_crt_file(self.f_name, f_hdlr=f_hdlr, no_print=True)
        f_hdlr.close()

        with open(self.l_name, mode="r", encoding="UTF-8") as f_hdlr:
            contents = f_hdlr.read()

        self.assertNotIn(err_msg_chk, contents)

    def test_print_file(self):

        """Function:  test_print_file

        Description:  Test with printing error messages to file.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.f_name)
        f_hdlr = open(                                  # pylint:disable=R1732
            self.l_name, "w", encoding="UTF-8")
        status, err_msg = gen_libs.chk_crt_file(
            self.f_name, f_hdlr=f_hdlr, no_print=True)
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
