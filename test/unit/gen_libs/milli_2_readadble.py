#!/usr/bin/python
# Classification (U)

"""Program:  milli_2_readadble.py

    Description:  Unit testing of milli_2_readadble in gen_libs.py.

    Usage:
        test/unit/gen_libs/milli_2_readadble.py

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
        setUp -> Unit testing initilization.
        test_milli_2_readadble7 -> Test with -1000000000ms.
        test_milli_2_readadble6 -> Test with -1ms.
        test_milli_2_readadble5 -> Test with 1000000000ms.
        test_milli_2_readadble4 -> Test with 1000000ms.
        test_milli_2_readadble3 -> Test with 1000ms.
        test_milli_2_readadble2 -> Test with 1ms.
        test_milli_2_readadble1 -> Test with 0ms.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.answer1 = "0 days 0 hours 0 minutes 0 seconds"
        self.answer2 = "0 days 0 hours 0 minutes 0 seconds"
        self.answer3 = "0 days 0 hours 0 minutes 1 seconds"
        self.answer4 = "0 days 0 hours 16 minutes 40 seconds"
        self.answer5 = "11 days 13 hours 46 minutes 40 seconds"
        self.answer6 = "-1 days 23 hours 59 minutes 59 seconds"
        self.answer7 = "-12 days 10 hours 13 minutes 20 seconds"

    def test_milli_2_readadble7(self):

        """Function:  test_milli_2_readadble7

        Description:  Test with -1000000000ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(-1000000000), self.answer7)

    def test_milli_2_readadble6(self):

        """Function:  test_milli_2_readadble6

        Description:  Test with -1ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(-1), self.answer6)

    def test_milli_2_readadble5(self):

        """Function:  test_milli_2_readadble5

        Description:  Test with 1000000000ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(1000000000), self.answer5)

    def test_milli_2_readadble4(self):

        """Function:  test_milli_2_readadble4

        Description:  Test with 1000000ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(1000000), self.answer4)

    def test_milli_2_readadble3(self):

        """Function:  test_milli_2_readadble3

        Description:  Test with 1000ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(1000), self.answer3)

    def test_milli_2_readadble2(self):

        """Function:  test_milli_2_readadble2

        Description:  Test with 1ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(1), self.answer2)

    def test_milli_2_readadble1(self):

        """Function:  test_milli_2_readadble1

        Description:  Test with 0ms.

        Arguments:

        """

        self.assertEqual(gen_libs.milli_2_readadble(0), self.answer1)


if __name__ == "__main__":
    unittest.main()
