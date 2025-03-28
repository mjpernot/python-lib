# Classification (U)

"""Program:  rotate_files.py

    Description:  Unit testing of rotate_files in gen_libs.py.

    Usage:
        test/unit/gen_libs/rotate_files.py

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
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_all_default_values
        test_maxcnt_default_value
        test_cnt_default_value
        test_cnt_ltone_maxcnt
        test_cnt_eq_maxcnt
        test_cnt_gt_maxcnt

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "File1"
        self.cnt = 1
        self.max_cnt = 2

    @mock.patch("gen_libs.os")
    def test_multiple_recursions(self, mock_os):

        """Function:  test_multiple_recursions

        Description:  Test with multiple recursion calls.

        Arguments:

        """

        mock_os.path.isfile.side_effect = [True, True, True, True, True, True]
        mock_os.rename.return_value = True

        self.assertFalse(gen_libs.rotate_files(self.fname))

    @mock.patch("gen_libs.os")
    def test_all_default_values(self, mock_os):

        """Function:  test_all_default_values

        Description:  Test with all default values.

        Arguments:

        """

        mock_os.path.isfile.side_effect = [True, True, True, True, True, True]
        mock_os.rename.return_value = True

        self.assertFalse(gen_libs.rotate_files(self.fname))

    @mock.patch("gen_libs.os")
    def test_maxcnt_default_value(self, mock_os):

        """Function:  test_maxcnt_default_value

        Description:  Test with no max_cnt argument passed.

        Arguments:

        """

        mock_os.path.isfile.side_effect = [True, True, True]
        mock_os.rename.return_value = True

        self.assertFalse(gen_libs.rotate_files(self.fname, cnt=3))

    @mock.patch("gen_libs.os")
    def test_cnt_default_value(self, mock_os):

        """Function:  test_cnt_default_value

        Description:  Test with no cnt argument passed.

        Arguments:

        """

        mock_os.path.isfile.side_effect = [True, True, True]
        mock_os.rename.return_value = True

        self.assertFalse(gen_libs.rotate_files(self.fname,
                                               max_cnt=self.max_cnt))

    @mock.patch("gen_libs.os")
    def test_cnt_ltone_maxcnt(self, mock_os):

        """Function:  test_cnt_ltone_maxcnt

        Description:  Test with cnt less than max_cnt less one.

        Arguments:

        """

        mock_os.path.isfile.side_effect = [True, True]
        mock_os.rename.return_value = True

        self.assertFalse(gen_libs.rotate_files(self.fname, self.cnt,
                                               self.max_cnt))

    def test_cnt_eq_maxcnt(self):

        """Function:  test_cnt_eq_maxcnt

        Description:  Test with cnt equal to max_cnt.

        Arguments:

        """

        self.assertFalse(gen_libs.rotate_files(self.fname, 2, self.max_cnt))

    def test_cnt_gt_maxcnt(self):

        """Function:  test_cnt_gt_maxcnt

        Description:  Test with cnt greater than max_cnt.

        Arguments:

        """

        self.assertFalse(gen_libs.rotate_files(self.fname, 3, self.max_cnt))


if __name__ == "__main__":
    unittest.main()
