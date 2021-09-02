#!/usr/bin/python
# Classification (U)

"""Program:  sec_2_hr.py

    Description:  Unit testing of sec_2_hr in gen_libs.py.

    Usage:
        test/unit/gen_libs/sec_2_hr.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_sec_2_hr8
        test_sec_2_hr7
        test_sec_2_hr6
        test_sec_2_hr5
        test_sec_2_hr4
        test_sec_2_hr3
        test_sec_2_hr2
        test_sec_2_hr1

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    def test_sec_2_hr8(self):

        """Function:  test_sec_2_hr8

        Description:  Test with -3600 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(-3600), -1.0)

    def test_sec_2_hr7(self):

        """Function:  test_sec_2_hr7

        Description:  Test with 3600 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(3600), 1.0)

    def test_sec_2_hr6(self):

        """Function:  test_sec_2_hr6

        Description:  Test with 3599 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(3599), 0.99)

    def test_sec_2_hr5(self):

        """Function:  test_sec_2_hr5

        Description:  Test with 1800 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(1800), 0.5)

    def test_sec_2_hr4(self):

        """Function:  test_sec_2_hr4

        Description:  Test with 1799 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(1799), 0.49)

    def test_sec_2_hr3(self):

        """Function:  test_sec_2_hr3

        Description:  Test with 36 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(36), 0.01)

    def test_sec_2_hr2(self):

        """Function:  test_sec_2_hr2

        Description:  Test with 35 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(35), 0.0)

    def test_sec_2_hr1(self):

        """Function:  test_sec_2_hr1

        Description:  Test with 0 seconds.

        Arguments:

        """

        self.assertEqual(gen_libs.sec_2_hr(0), 0.0)


if __name__ == "__main__":
    unittest.main()
