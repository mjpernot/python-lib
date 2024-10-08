# Classification (U)

"""Program:  mail2_add_text.py

    Description:  Unit testing of Mail2.add_text in gen_class.py.

    Usage:
        test/unit/gen_class/mail2_add_text.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_add_text

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = "mail_address@domain.name"
        self.subj = "Test_Subj"
        self.frm = "mail_address@domain.name"
        self.data = "This is a test line for an email"

    def test_add_text(self):

        """Function:  test_add_text

        Description:  Test with adding text to the email.

        Arguments:

        """

        email = gen_class.Mail2(self.subj, self.toaddr, fromaddr=self.frm)
        email.add_text(self.data)

        self.assertTrue(self.data in email.msg.as_string())


if __name__ == "__main__":
    unittest.main()
