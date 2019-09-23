#!/usr/bin/python
# Classification (U)

"""Program:  pct_int.py

    Description:  Unit testing of pct_int in gen_libs.py.

    Usage:
        test/unit/gen_libs/pct_int.py

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
        test_pct_int6 -> Test with 1 and 1.
        test_pct_int5 -> Test with 0 and 0.
        test_pct_int4 -> Test with 2 and 5.
        test_pct_int3 -> Test with 5 and 2.
        test_pct_int2 -> Test with 100 and 10.
        test_pct_int1 -> Test with 10 and 100.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    @mock.patch("gen_libs.float_div")
    def test_pct_int6(self, mock_div):

        """Function:  test_pct_int6

        Description:  Test with 1 and 1.

        Arguments:

        """

        mock_div.return_value = 1.0

        self.assertEqual(gen_libs.pct_int(1, 1), 100.0)

    @mock.patch("gen_libs.float_div")
    def test_pct_int5(self, mock_div):

        """Function:  test_pct_int5

        Description:  Test with 0 and 0.

        Arguments:

        """

        mock_div.return_value = 0.0

        self.assertEqual(gen_libs.pct_int(0, 0), 0.0)

    @mock.patch("gen_libs.float_div")
    def test_pct_int4(self, mock_div):

        """Function:  test_pct_int4

        Description:  Test with 2 and 5.

        Arguments:

        """

        mock_div.return_value = 0.4

        self.assertEqual(gen_libs.pct_int(2, 5), 40.0)

    @mock.patch("gen_libs.float_div")
    def test_pct_int3(self, mock_div):

        """Function:  test_pct_int3

        Description:  Test with 5 and 2.

        Arguments:

        """

        mock_div.return_value = 2.5

        self.assertEqual(gen_libs.pct_int(5, 2), 250.0)

    @mock.patch("gen_libs.float_div")
    def test_pct_int2(self, mock_div):

        """Function:  test_pct_int2

        Description:  Test with 100 and 10.

        Arguments:

        """

        mock_div.return_value = 10.0

        self.assertEqual(gen_libs.pct_int(100, 10), 1000.0)

    @mock.patch("gen_libs.float_div")
    def test_pct_int1(self, mock_div):

        """Function:  test_pct_int1

        Description:  Test with 10 and 100.

        Arguments:

        """

        mock_div.return_value = 0.1

        self.assertEqual(gen_libs.pct_int(10, 100), 10.0)


if __name__ == "__main__":
    unittest.main()
