# Classification (U)

"""Program:  month_delta.py

    Description:  Unit testing of month_delta in gen_libs.py.

    Usage:
        test/unit/gen_libs/month_delta.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import datetime
import unittest

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
        test_month_delta
        test_month_delta2
        test_month_delta3
        test_month_delta4
        test_month_delta5
        test_month_delta6
        test_month_delta7
        test_month_delta8

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.date_mask = "%Y-%m-%d"
        self.date = "2017-12-21"
        self.delta = 0

    def test_month_delta(self):

        """Function:  test_month_delta

        Description:  Test month_delta function with a delta of zero.

        Arguments:

        """

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (12, 2017))

    def test_month_delta2(self):

        """Function:  test_month_delta2

        Description:  Test month_delta function for previous month.

        Arguments:

        """

        self.delta = -1

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (11, 2017))

    def test_month_delta3(self):

        """Function:  test_month_delta3

        Description:  Test month_delta function for next month.

        Arguments:

        """

        self.delta = 1

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (1, 2018))

    def test_month_delta4(self):

        """Function:  test_month_delta4

        Description:  Test month_delta function for 11 months past.

        Arguments:

        """

        self.delta = -11

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (1, 2017))

    def test_month_delta5(self):

        """Function:  test_month_delta5

        Description:  Test month_delta function for 12 months past.

        Arguments:

        """

        self.delta = -12

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (12, 2016))

    def test_month_delta6(self):

        """Function:  test_month_delta6

        Description:  Test month_delta function for 11 months future.

        Arguments:

        """

        self.delta = 11

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (11, 2018))

    def test_month_delta7(self):

        """Function:  test_month_delta7

        Description:  Test month_delta function for 12 months future.

        Arguments:

        """

        self.delta = 12

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (12, 2018))

    def test_month_delta8(self):

        """Function:  test_month_delta8

        Description:  Test month_delta function for 13 months future.

        Arguments:

        """

        self.delta = 13

        self.assertEqual(gen_libs.month_delta(datetime.datetime.strptime(
            self.date, self.date_mask), self.delta), (1, 2019))


if __name__ == "__main__":
    unittest.main()
