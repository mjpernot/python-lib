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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class SubProcess():

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        Popen
        wait

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance.

        Arguments:

        """

        self.stdout = None
        self.stdin = None
        self.cmd = None

    def Popen(self, cmd, stdout=None, stdin=None):      # pylint:disable=C0103

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_to_list2
        test_to_list
        test_to_str
        test_subj_spaces2
        test_subj_spaces
        test_subj_str
        test_send_mailx2
        test_send_mailx

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.frm = "From_Address"
        self.toaddr = "To_Address"
        self.toaddr2 = ["To_Address"]
        self.toaddr3 = ["To_Address", "To_Address2"]
        self.toaddr3a = "To_Address To_Address2"
        self.subj = "SubjectLine"
        self.subj2 = ["SubjectLine2"]
        self.subj2a = "SubjectLine2"
        self.subj3 = ["Subject", "Line3"]
        self.subj3a = "SubjectLine3"
        self.subp = SubProcess()
        self.subp2 = SubProcess()

    @mock.patch("gen_class.subprocess")
    def test_to_list2(self, mock_subp):

        """Function:  test_to_list2

        Description:  Test to address as a list.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr3, subj=self.subj, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj, self.toaddr3a))

    @mock.patch("gen_class.subprocess")
    def test_to_list(self, mock_subp):

        """Function:  test_to_list

        Description:  Test to address as a list.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr2, subj=self.subj, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj, self.toaddr))

    @mock.patch("gen_class.subprocess")
    def test_to_str(self, mock_subp):

        """Function:  test_to_str

        Description:  Test to address as a string.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr, subj=self.subj, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj, self.toaddr))

    @mock.patch("gen_class.subprocess")
    def test_subj_spaces2(self, mock_subp):

        """Function:  test_subj_spaces2

        Description:  Test subject line with white spaces.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr, subj=self.subj3, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj3a, self.toaddr))

    @mock.patch("gen_class.subprocess")
    def test_subj_spaces(self, mock_subp):

        """Function:  test_subj_spaces

        Description:  Test subject line with white spaces.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr, subj=self.subj2, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj2a, self.toaddr))

    @mock.patch("gen_class.subprocess")
    def test_subj_str(self, mock_subp):

        """Function:  test_subj_str

        Description:  Test subject line as a string.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr, subj=self.subj, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj, self.toaddr))

    @mock.patch("gen_class.subprocess")
    def test_send_mailx2(self, mock_subp):

        """Function:  test_send_mailx2

        Description:  Test send_mailx function.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr, subj=self.subj, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        mail.send_mailx()

        self.assertEqual((mail.subj, mail.toaddr), (self.subj, self.toaddr))

    @mock.patch("gen_class.subprocess")
    def test_send_mailx(self, mock_subp):

        """Function:  test_send_mailx

        Description:  Test send_mailx function.

        Arguments:

        """

        mail = gen_class.Mail(self.toaddr, subj=self.subj, frm=self.frm)
        mock_subp.side_effect = [self.subp, self.subp2]

        self.assertFalse(mail.send_mailx())


if __name__ == "__main__":
    unittest.main()
