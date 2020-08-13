#!/usr/bin/python
# Classification (U)

"""Program:  mail_read_stdin.py

    Description:  Unit testing of read_stdin in gen_libs.py.

    Usage:
        test/unit/gen_libs/mail_read_stdin.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import io

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

    Methods:
        setUp -> Unit testing initilization.
        test_read_stdin -> Test test_read_stdin function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = "To_Address"

    @mock.patch("gen_class.sys.stdin", io.StringIO(u"Test email line"))
    def test_read_stdin(self):

        """Function:  test_read_stdin

        Description:  Test test_read_stdin function.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)

        email.read_stdin()

        self.assertEqual((email.to, email.msg), (self.toaddr,
                                                 '"Test email line"'))


if __name__ == "__main__":
    unittest.main()
