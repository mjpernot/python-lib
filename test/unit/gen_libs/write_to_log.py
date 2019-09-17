#!/usr/bin/python
# Classification (U)

"""Program:  write_to_log.py

    Description:  Unit testing of write_to_log in gen_libs.py.

    Usage:
        test/unit/gen_libs/write_to_log.py

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
        test_write_to_log -> Test write_to_log function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.date = "2019-05-23"
        self.time = "14:46:14"
        self.f_hldr = "File_Handler"
        self.text = "Text_Message"

    @mock.patch("gen_libs.get_date")
    @mock.patch("gen_libs.get_time")
    @mock.patch("gen_libs.write_file2")
    def test_write_to_log(self, mock_write, mock_time, mock_date):

        """Function:  test_write_to_log

        Description:  Test write_to_log function.

        Arguments:

        """

        mock_write.return_value = True
        mock_time.return_value = self.time
        mock_date.return_value = self.date

        self.assertFalse(gen_libs.write_to_log(self.f_hldr, self.text))


if __name__ == "__main__":
    unittest.main()
