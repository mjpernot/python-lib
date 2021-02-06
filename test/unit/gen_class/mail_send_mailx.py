#!/usr/bin/python
# Classification (U)

"""Program:  mail_send_mailx.py

    Description:  Unit testing of send_mail in gen_libs.py.

    Usage:
        test/unit/gen_libs/mail_send_mailx.py

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


class SubProcess(object):

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__ -> Initialization instance.
        Popen -> Mock representation of subprocess.Popen method.
        wait -> Mock representation of subprocess.wait method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance.

        Arguments:

        """

        self.PIPE = "Pipe Redirect"
        self.stdout = None
        self.stdin = None
        self.cmd = None

    def Popen(self, cmd, stdout=None, stdin=None):

        """Method:  Popen

        Description:  Mock representation of subprocess.Popen method.

        Arguments:

        """

        self.stdout = stdout
        self.stdin = stdin
        self.cmd = cmd

        return "Proc Instance"

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_send_mail -> Test test_send_mail function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.frm = "From_Address"
        self.toaddr = "To_Address"

    @mock.patch("gen_class.Mail.create_body")
    @mock.patch("gen_class.smtplib.SMTP")
    def test_send_mail(self, mock_smtp, mock_body):

        """Function:  test_send_mail

        Description:  Test test_send_mail function.

        Arguments:

        """

        mock_smtp.return_value = Smtplib()
        mock_body.return_value = True
        email = gen_class.Mail(self.toaddr)

        self.assertFalse(email.send_mail())


if __name__ == "__main__":
    unittest.main()
