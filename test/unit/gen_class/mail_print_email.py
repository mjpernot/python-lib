# Classification (U)

"""Program:  mail_print_email.py

    Description:  Unit testing of Mail.print_email in gen_class.py.

    Usage:
        test/unit/gen_class/mail_print_email.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_print_email

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = ["mail_address@domain.name"]
        self.frm = ["mail_address@domain.name"]
        self.subj = "Test subject"
        self.body = "Test mail body"

    def test_print_email(self):

        """Function:  test_print_email

        Description:  Test printing email.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj, frm=self.frm)
        email.create_subject(subj=self.subj)
        email.add_2_msg(txt_ln=self.body)

        self.assertEqual(
            email.print_email(),
            f"To: {self.toaddr}\nFrom: {self.frm}\n{email.create_body()}")


if __name__ == "__main__":
    unittest.main()
