# Classification (U)

"""Program:  chk_perm.py

    Description:  Unit testing of chk_perm in gen_libs.py.

    Usage:
        test/unit/gen_libs/chk_perm.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
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
        setUp
        test_multi_perm_fail4
        test_multi_perm_fail3
        test_multi_perm_fail2
        test_multi_perm_fail
        test_execute_fail
        test_write_fail
        test_read_fail
        test_multi_perm_success4
        test_multi_perm_success3
        test_multi_perm_success2
        test_multi_perm_success
        test_execute_success
        test_write_success
        test_read_success

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.item = "/path/object"
        self.oct_perm = 7
        self.oct_perm2 = 6
        self.oct_perm3 = 5
        self.oct_perm4 = 4
        self.oct_perm5 = 3
        self.oct_perm6 = 2
        self.oct_perm7 = 1

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="rwx"))
    def test_multi_perm_fail4(self):

        """Function:  test_multi_perm_fail4

        Description:  Test with read permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm7))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="-wx"))
    def test_multi_perm_fail3(self):

        """Function:  test_multi_perm_fail3

        Description:  Test with read permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm5))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="r-x"))
    def test_multi_perm_fail2(self):

        """Function:  test_multi_perm_fail2

        Description:  Test with read permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm3))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="rw-"))
    def test_multi_perm_fail(self):

        """Function:  test_multi_perm_fail

        Description:  Test with read permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm2))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="--x"))
    def test_execute_fail(self):

        """Function:  test_execute_fail

        Description:  Test with execute permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm7))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="-w-"))
    def test_write_fail(self):

        """Function:  test_write_fail

        Description:  Test with write permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm6))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=False))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="r--"))
    def test_read_fail(self):

        """Function:  test_read_fail

        Description:  Test with read permission checked failed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.item, self.oct_perm4))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="rwx"))
    def test_multi_perm_success4(self):

        """Function:  test_multi_perm_success4

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm7))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="-wx"))
    def test_multi_perm_success3(self):

        """Function:  test_multi_perm_success3

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm5))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="r-x"))
    def test_multi_perm_success2(self):

        """Function:  test_multi_perm_success2

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm3))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="rw-"))
    def test_multi_perm_success(self):

        """Function:  test_multi_perm_success

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm2))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="--x"))
    def test_execute_success(self):

        """Function:  test_execute_success

        Description:  Test with execute permission checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm7))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="-w-"))
    def test_write_success(self):

        """Function:  test_write_success

        Description:  Test with write permission checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm6))

    @mock.patch("gen_libs.os.access", mock.Mock(return_value=True))
    @mock.patch("gen_libs.octal_to_str", mock.Mock(return_value="r--"))
    def test_read_success(self):

        """Function:  test_read_success

        Description:  Test with read permission checked successfully.

        Arguments:

        """

        self.assertTrue(gen_libs.chk_perm(self.item, self.oct_perm4))


if __name__ == "__main__":
    unittest.main()
