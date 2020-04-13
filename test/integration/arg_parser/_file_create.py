#!/usr/bin/python
# Classification (U)

"""Program:  _file_create.py

    Description:  Unit testing of _file_create in arg_parser.py.

    Usage:
        test/integration/arg_parser/_file_create.py

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
import arg_parser
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_open_fail3 -> Test with unable to open file to write.
        test_open_fail2 -> Test with no -f in file_crt_list list.
        test_open_fail -> Test with errno set to non-two value.
        test_open_success -> Test with file open returning successful.
        test_errno_not_two -> Test with errno not set to two.
        test_option_not_in_list -> Test with option not being in file_crt_list.
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.option = "-f"
        self.file_crt_list = ["-f"]
        self.file_crt_list2 = ["-g"]
        self.errno = 2
        self.errno2 = 1
        self.strerror = "No file"
        self.status = False
        self.name = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/file_create.txt")
        self.name2 = os.path.join(
            os.getcwd(), "test/integration/arg_parser/tmp/tmp/file_create.txt")

    def test_open_fail3(self):

        """Function:  test_open_fail3

        Description:  Test with unable to open file to write.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(
                self.name2, self.option, self.file_crt_list, self.errno,
                self.strerror, self.status))

    def test_open_fail2(self):

        """Function:  test_open_fail2

        Description:  Test with no -f in file_crt_list list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(
                self.name, self.option, self.file_crt_list2, self.errno,
                self.strerror, self.status))

    def test_open_fail(self):

        """Function:  test_open_fail

        Description:  Test with errno set to non-two value.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(
                self.name, self.option, self.file_crt_list, self.errno2,
                self.strerror, self.status))

    def test_open_success(self):

        """Function:  test_open_success

        Description:  Test with file open returning successful.

        Arguments:

        """

        self.assertFalse(arg_parser._file_create(
            self.name, self.option, self.file_crt_list, self.errno,
            self.strerror, self.status))

        self.assertTrue(os.path.isfile(self.name))

    def test_errno_not_two(self):

        """Function:  test_errno_not_two

        Description:  Test with errno not set to two.

        Arguments:

        """

        self.errno = 10

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(
                self.name, self.option, self.file_crt_list, self.errno,
                self.strerror, self.status))

    def test_option_not_in_list(self):

        """Function:  test_option_not_in_list

        Description:  Test with option not being in file_crt_list.

        Arguments:

        """

        self.option = "-a"

        with gen_libs.no_std_out():
            self.assertTrue(arg_parser._file_create(
                self.name, self.option, self.file_crt_list, self.errno,
                self.strerror, self.status))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.name):
            os.remove(self.name)


if __name__ == "__main__":
    unittest.main()
