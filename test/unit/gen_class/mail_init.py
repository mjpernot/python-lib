# Classification (U)

"""Program:  mail_init.py

    Description:  Unit testing of Mail.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/mail_init.py

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
        test_no_from_addr
        test_from_addr
        test_subj_list
        test_subj_string
        test_with_data
        test_to_string
        test_to_list
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mailaddr = "mail_address@domain.name"
        self.toaddr = [self.mailaddr]
        self.subj = None
        self.subj2 = "Test_Subj"
        self.subj3 = "This is a test"
        self.subj4 = ["This", "is", "a", "test"]
        self.subj4a = "This is a test"
        self.frm = None
        self.frm2 = self.mailaddr
        self.host_name = None
        self.host = None

    def test_no_from_addr(self):

        """Function:  test_no_from_addr

        Description:  Test with no from address is passed.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj4, frm=self.frm2)

        self.assertTrue(email.frm)

    def test_from_addr(self):

        """Function:  test_from_addr

        Description:  Test with from address is passed.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj4, frm=self.frm2)

        self.assertEqual(email.frm, self.frm2)

    def test_subj_list(self):

        """Function:  test_subj_string

        Description:  Test subject line as a string.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj4, frm=self.frm2)

        self.assertEqual(
            (email.toaddr, email.subj, email.frm, email.host_name, email.host),
            (email.toaddr, self.subj4a, self.frm2, None, None))

    def test_subj_string(self):

        """Function:  test_subj_string

        Description:  Test subject line as a string.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj3, frm=self.frm2)

        self.assertEqual(
            (email.toaddr, email.subj, email.frm, email.host_name, email.host),
            (email.toaddr, self.subj3, self.frm2, None, None))

    def test_with_data(self):

        """Function:  test_with_data

        Description:  Test other attributes with data.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj2, frm=self.frm2)

        self.assertEqual(
            (email.toaddr, email.subj, email.frm, email.host_name, email.host),
            (email.toaddr, self.subj2, self.frm2, None, None))

    def test_to_string(self):

        """Function:  test_to_string

        Description:  Test to line with a string.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)

        self.assertEqual(
            (self.mailaddr, email.subj, email.host_name, email.host),
            (self.mailaddr, None, None, None))

    def test_to_list(self):

        """Function:  test_to_list

        Description:  Test to line with a list.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)

        self.assertEqual(
            (email.toaddr, email.subj, email.host_name, email.host),
            (self.toaddr, None, None, None))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)

        self.assertEqual(
            (email.toaddr, email.subj, email.host_name, email.host),
            (self.toaddr, None, None, None))


if __name__ == "__main__":
    unittest.main()
