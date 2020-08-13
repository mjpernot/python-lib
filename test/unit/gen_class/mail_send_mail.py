#!/usr/bin/python
# Classification (U)

"""Program:  mail_send_mail.py

    Description:  Unit testing of send_mail in gen_libs.py.

    Usage:
        test/unit/gen_libs/mail_send_mail.py

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


class Smtplib(object):

    """Class:  SubProcess

    Description:  Class which is a representation of the smtplib class.

    Methods:
        __init__ -> Initialize configuration environment.
        sendmail -> Mock representation of sendmail method.
        quit -> Mock representation of quit method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the subprocess class.

        Arguments:

        """

        self.frm = None
        self.toaddr = None
        self.func = None

    def sendmail(self, frm, toaddr, func):

        """Method:  sendmail

        Description:  Mock representation of sendmail method.

        Arguments:
            frm -> Mock for from address.
            toaddr -> Mock for to address.
            func -> Mock for function call.

        """

        self.frm = frm
        self.toaddr = toaddr
        self.func = func

    def quit(self):

        """Method:  quit

        Description:  Mock representation of quit method.

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
