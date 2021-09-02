#!/usr/bin/python
# Classification (U)

"""Program:  chk_crt_file.py

    Description:  Unit testing of chk_crt_file in gen_libs.py.

    Usage:
        test/integration/gen_libs/chk_crt_file.py

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

# Global
PERM1 = "444"
PERM2 = "333"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_file_name
        test_file_not_exist
        test_create_file
        test_write_file
        test_no_write_file
        test_read_file
        test_no_read_file
        test_no_print_set
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
        self.base_dir = "test/integration/gen_libs/tmp"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.f_name = os.path.join(self.test_path, self.file_name)
        self.l_name = os.path.join(self.test_path, "TEST_LOG")

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
        status, err_msg = gen_libs.chk_crt_file(self.f_name, create=True,
                                                no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test with checking write permission on file.

        Arguments:

        """

        err_msg_chk = None
        open(self.f_name, "a").close()
        status, err_msg = gen_libs.chk_crt_file(self.f_name, write=True,
                                                no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_write_file(self):

        """Function:  test_no_write_file

        Description:  Test with checking no write permission on file.

        Arguments:

        """

        global PERM1

        err_msg_chk = "Error: File %s is not writeable." % (self.f_name)
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM1, 8))
        status, err_msg = gen_libs.chk_crt_file(self.f_name, write=True,
                                                no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_read_file(self):

        """Function:  test_read_file

        Description:  Test with checking read permission on file.

        Arguments:

        """

        err_msg_chk = None
        open(self.f_name, "a").close()
        status, err_msg = gen_libs.chk_crt_file(self.f_name, read=True,
                                                no_print=True)

        self.assertTrue(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_read_file(self):

        """Function:  test_no_read_file

        Description:  Test with checking no read permission on file.

        Arguments:

        """

        global PERM2

        err_msg_chk = "Error: File %s is not readable." % (self.f_name)
        open(self.f_name, "a").close()
        os.chmod(self.f_name, int(PERM2, 8))
        status, err_msg = gen_libs.chk_crt_file(self.f_name, read=True,
                                                no_print=True)

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

    def test_print_file(self):

        """Function:  test_print_file

        Description:  Test with printing error messages to file.

        Arguments:

        """

        err_msg_chk = self.err_mask % (self.f_name)
        f_hdlr = open(self.l_name, "w")
        status, err_msg = gen_libs.chk_crt_file(self.f_name, f_hdlr=f_hdlr,
                                                no_print=True)
        f_hdlr.close()

        self.assertFalse(err_msg_chk in open(self.l_name).read())
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
