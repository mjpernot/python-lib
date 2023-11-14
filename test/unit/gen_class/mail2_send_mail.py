# Classification (U)

"""Program:  mail2_send_mail.py

    Description:  Unit testing of Mail2.send_mail in gen_libs.py.

    Usage:
        test/unit/gen_libs/mail2_send_mail.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
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
        __init__
        sendmail
        quit

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
            frm
            toaddr
            func

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
        setUp
        test_send_mail

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.frm = "mail_address@domain.name"
        self.toaddr = "mail_address@domain.name"
        self.subj = "SubjectLine"

    @mock.patch("gen_class.smtplib.SMTP")
    def test_send_mail(self, mock_smtp):

        """Function:  test_send_mail

        Description:  Test test_send_mail function.

        Arguments:

        """

        mock_smtp.return_value = Smtplib()
        mail = gen_class.Mail2(self.subj, self.toaddr, fromaddr=self.frm)

        self.assertFalse(mail.send_email())


if __name__ == "__main__":
    unittest.main()
