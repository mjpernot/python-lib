#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      chk_crt_file.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_libs        => v1.34.0 or higher
#
###############################################################################

"""Program:  chk_crt_file.py

    Description:  Unit testing of chk_crt_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/chk_crt_file.py

    Arguments:
        None

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

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_no_file_name -> Test with no file name passed.
        test_file_not_exist -> Test with file does not exist.
        test_create_file -> Test with creating file.
        test_write_file -> Test with checking write permission on file.
        test_no_write_file -> Test with checking no write permission on file.
        test_read_file -> Test with checking read permission on file.
        test_no_read_file -> Test with checking no read permission on file.
        test_no_print_set -> Test with no_print option set.
        test_print_file -> Test with printing error messages to file.
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.file_name = "TEST_FILE"
        self.base_dir = "test/unit/gen_libs/tmp"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.f_name = os.path.join(self.test_path, self.file_name)
        self.l_name = os.path.join(self.test_path, "TEST_LOG")

    def test_no_file_name(self):

        """Function:  test_no_file_name

        Description:  Test with no file name passed.

        Arguments:
            None

        """

        err_msg_chk = "Error:  No value passed for filename."

        status, err_msg = gen_libs.chk_crt_file("", no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_file_not_exist(self):

        """Function:  test_file_not_exist

        Description:  Test with file does not exist.

        Arguments:
            None

        """

        err_msg_chk = "Error:  File %s does not exist." % (self.f_name)

        status, err_msg = gen_libs.chk_crt_file(self.f_name, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_create_file(self):

        """Function:  test_create_file

        Description:  Test with creating file.

        Arguments:
            None

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
            None

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
            None

        """

        err_msg_chk = "Error: File %s is not writable." % (self.f_name)

        open(self.f_name, "a").close()
        os.chmod(self.f_name, 0444)

        status, err_msg = gen_libs.chk_crt_file(self.f_name, write=True,
                                                no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_read_file(self):

        """Function:  test_read_file

        Description:  Test with checking read permission on file.

        Arguments:
            None

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
            None

        """

        err_msg_chk = "Error: File %s is not readable." % (self.f_name)

        open(self.f_name, "a").close()
        os.chmod(self.f_name, 0333)

        status, err_msg = gen_libs.chk_crt_file(self.f_name, read=True,
                                                no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_no_print_set(self):

        """Function:  test_no_print_set

        Description:  Test with no_print option set.

        Arguments:
            None

        """

        err_msg_chk = "Error:  File %s does not exist." % (self.f_name)

        status, err_msg = gen_libs.chk_crt_file(self.f_name, no_print=True)

        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def test_print_file(self):

        """Function:  test_print_file

        Description:  Test with printing error messages to file.

        Arguments:
            None

        """

        err_msg_chk = "Error:  File %s does not exist." % (self.f_name)
        f_hdlr = open(self.l_name, "w")

        status, err_msg = gen_libs.chk_crt_file(self.f_name, f_hdlr=f_hdlr,
                                                no_print=True)

        f_hdlr.close()

        if err_msg_chk in open(self.l_name).read():
            f_status = True

        else:
            f_status = False

        self.assertFalse(f_status)
        self.assertFalse(status)
        self.assertEqual(err_msg, err_msg_chk)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:
            None

        """

        if os.path.isfile(self.f_name):
            os.remove(self.f_name)

        if os.path.isfile(self.l_name):
            os.remove(self.l_name)


if __name__ == "__main__":
    unittest.main()