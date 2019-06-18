#!/usr/bin/python
# Classification (U)

"""Program:  crt_file_time.py

    Description:  Unit testing of crt_file_time in gen_libs.py.

    Usage:
        test/unit/gen_libs/crt_file_time.py

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_crt_file_time -> Test crt_file_time function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.indate = "20190610_0415"
        self.fname = "File_name"
        self.path = "/dir/path/"
        self.ext = ".txt"
        self.result = "/dir/path/File_name.20190610_0415.txt"

    @mock.patch("gen_libs.time")
    def test_crt_file_time(self, mock_date):

        """Function:  test_crt_file_time

        Description:  Test crt_file_time function.

        Arguments:

        """

        mock_date.strftime.return_value = self.indate

        self.assertEqual(gen_libs.crt_file_time(self.fname, self.path,
                                                self.ext), self.result)


if __name__ == "__main__":
    unittest.main()
