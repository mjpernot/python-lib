#!/usr/bin/python
# Classification (U)

"""Program:  get_time.py

    Description:  Unit testing of get_time in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_time.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
        test_get_time -> Test get_time function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.intime = "10:11:12"
        self.outtime = "10:11:12"

    @mock.patch("gen_libs.datetime.datetime")
    def test_get_time(self, mock_date):

        """Function:  test_get_time

        Description:  Test get_time function.

        Arguments:

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.intime

        self.assertEqual(gen_libs.get_time(), self.outtime)


if __name__ == "__main__":
    unittest.main()
