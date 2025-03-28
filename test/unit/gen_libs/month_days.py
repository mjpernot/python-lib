# Classification (U)

"""Program:  month_days.py

    Description:  Unit testing of month_days in gen_libs.py.

    Usage:
        test/unit/gen_libs/month_days.py

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
        test_month_days

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = datetime.datetime.strptime("20200301", "%Y%m%d")
        self.results = 31

    def test_month_days(self):

        """Function:  test_month_days

        Description:  Test months_days function.

        Arguments:

        """

        self.assertEqual(gen_libs.month_days(self.dtg), self.results)


if __name__ == "__main__":
    unittest.main()
