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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_read_stdin

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = "To_Address"
        self.msg = '"Test email line"'
        self.msg3 = "Test email line"

    @mock.patch("gen_class.sys.stdin", io.StringIO("Test email line"))
    def test_read_stdin(self):

        """Function:  test_read_stdin

        Description:  Test test_read_stdin function.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)

        email.read_stdin()

        if sys.version_info < (3, 0):
            msg = self.msg

        else:
            msg = self.msg3

        self.assertEqual(
            (email.toaddr, email.msg), (self.toaddr, msg))


if __name__ == "__main__":
    unittest.main()
