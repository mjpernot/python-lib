#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
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
        setUp -> Unit testing initilization.
        test_all_default_values -> Test with all default values.
        test_maxcnt_default_value -> Test with no max_cnt argument passed.
        test_cnt_default_value -> Test with no cnt argument passed.
        test_cnt_ltone_maxcnt -> Test with cnt less than max_cnt less one.
        test_cnt_eq_maxcnt -> Test with cnt equal to max_cnt.
        test_cnt_gt_maxcnt -> Test with cnt greater than max_cnt.

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
