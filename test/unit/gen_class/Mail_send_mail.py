#!/usr/bin/python
# Classification (U)

"""Program:  Mail_send_mail.py

    Description:  Unit testing of send_mail in gen_libs.py.

    Usage:
        test/unit/gen_libs/Mail_send_mail.py

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

    Super-Class:  object

    Sub-Classes:

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

        pass

    def sendmail(self, frm, to, func):

        """Method:  sendmail

        Description:  Mock representation of sendmail method.

        Arguments:
            frm -> Mock for from address.
            to -> Mock for to address.
            func -> Mock for function call.

        """

        pass

    def quit(self):

        """Method:  quit

        Description:  Mock representation of quit method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

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
        self.to = "To_Address"

    @mock.patch("gen_class.Mail.create_body")
    @mock.patch("gen_class.smtplib.SMTP")
    def test_send_mail(self, mock_smtp, mock_body):

        """Function:  test_send_mail

        Description:  Test test_send_mail function.

        Arguments:

        """

        mock_smtp.return_value = Smtplib()
        mock_body.return_value = True
        email = gen_class.Mail(self.to)

        self.assertFalse(email.send_mail())


if __name__ == "__main__":
    unittest.main()
