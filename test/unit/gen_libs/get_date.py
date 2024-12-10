# Classification (U)

"""Program:  get_date.py

    Description:  Unit testing of get_date in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_date.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
        test_get_date

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.indate = "2019/12/16"
        self.outdate = "2019/12/16"

    @mock.patch("gen_libs.datetime.datetime")
    def test_get_date(self, mock_date):

        """Function:  test_get_date

        Description:  Test get_date function.

        Arguments:

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.indate

        self.assertEqual(gen_libs.get_date(), self.outdate)


if __name__ == "__main__":
    unittest.main()
