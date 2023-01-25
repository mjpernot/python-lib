# Classification (U)

"""Program:  chk_perm.py

    Description:  Integration testing of chk_perm in gen_libs.py.

    Usage:
        test/integration/gen_libs/chk_perm.py

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
PERM = "000"
PERM1 = "111"


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
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_path = "test/integration/gen_class/tmp"
        self.dir1 = os.path.join(self.base_path, "dir1")

        self.oct_perm = 7
        self.oct_perm2 = 6
        self.oct_perm3 = 5
        self.oct_perm4 = 4
        self.oct_perm5 = 3
        self.oct_perm6 = 2
        self.oct_perm7 = 1

    def test_multi_perm_fail4(self):

        """Function:  test_multi_perm_fail4

        Description:  Test with read permission checked failed.

        Arguments:

        """

        global PERM

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm7))

    def test_multi_perm_fail3(self):

        """Function:  test_multi_perm_fail3

        Description:  Test with read permission checked failed.

        Arguments:

        """

        global PERM

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm5))

    def test_multi_perm_fail2(self):

        """Function:  test_multi_perm_fail2

        Description:  Test with read permission checked failed.

        Arguments:

        """

        global PERM

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm3))

    def test_multi_perm_fail(self):

        """Function:  test_multi_perm_fail

        Description:  Test with read permission checked failed.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm2))

    def test_execute_fail(self):

        """Function:  test_execute_fail

        Description:  Test with execute permission checked failed.

        Arguments:

        """

        global PERM

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm7))

    def test_write_fail(self):

        """Function:  test_write_fail

        Description:  Test with write permission checked failed.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm6))

    def test_read_fail(self):

        """Function:  test_read_fail

        Description:  Test with read permission checked failed.

        Arguments:

        """

        global PERM1

        os.mkdir(self.dir1)
        os.chmod(self.dir1, int(PERM1, 8))

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.chk_perm(self.dir1, self.oct_perm4))

    def test_multi_perm_success4(self):

        """Function:  test_multi_perm_success4

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm7))

    def test_multi_perm_success3(self):

        """Function:  test_multi_perm_success3

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm5))

    def test_multi_perm_success2(self):

        """Function:  test_multi_perm_success2

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm3))

    def test_multi_perm_success(self):

        """Function:  test_multi_perm_success

        Description:  Test with multiple permissions checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm2))

    def test_execute_success(self):

        """Function:  test_execute_success

        Description:  Test with execute permission checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm7))

    def test_write_success(self):

        """Function:  test_write_success

        Description:  Test with write permission checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm6))

    def test_read_success(self):

        """Function:  test_read_success

        Description:  Test with read permission checked successfully.

        Arguments:

        """

        os.mkdir(self.dir1)

        self.assertTrue(gen_libs.chk_perm(self.dir1, self.oct_perm4))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.dir1):
            os.rmdir(self.dir1)


if __name__ == "__main__":
    unittest.main()
