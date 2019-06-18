#!/usr/bin/python
# Classification (U)

"""Program:  Mail_read_stdin.py

    Description:  Unit testing of read_stdin in gen_libs.py.

    Usage:
        test/unit/gen_libs/Mail_read_stdin.py

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
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_read_stdin -> Test test_read_stdin function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.to = "To_Address"

    @mock.patch("gen_class.Mail.read_stdin")
    @mock.patch("gen_class.sys")
    def test_read_stdin(self, mock_sys, mock_read):

        """Function:  test_read_stdin

        Description:  Test test_read_stdin function.

        Arguments:

        """

        mock_sys.stdin.return_value = ["This", "is", "a", "test"]
        mock_read.return_value = True
        email = gen_class.Mail(self.to)

        self.assertTrue(email.read_stdin())


if __name__ == "__main__":
    unittest.main()
