# Classification (U)

"""Program:  mail2_init.py

    Description:  Unit testing of Mail2.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/mail2_init.py

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
        test_to_string
        test_to_list2
        test_to_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        toaddr = "mail_address@domain.name"
        self.toaddr = [toaddr]
        self.toaddr2 = toaddr
        self.toaddr3 = [toaddr, toaddr]
        self.toaddr3a = toaddr + "," + toaddr
        self.subj = None
        self.subj2 = "Test_Subj"
        self.subj3 = "This is a test"
        self.subj4 = ["This", "is", "a", "test"]
        self.subj4a = "This is a test"
        self.frm = None
        self.frm2 = toaddr

    def test_no_from_addr(self):

        """Function:  test_no_from_addr

        Description:  Test with no from address is passed.

        Arguments:

        """

        email = gen_class.Mail2(self.subj4, self.toaddr, fromaddr=self.frm2)

        self.assertTrue(email.msg["From"])

    def test_from_addr(self):

        """Function:  test_from_addr

        Description:  Test with from address is passed.

        Arguments:

        """

        email = gen_class.Mail2(self.subj4, self.toaddr, fromaddr=self.frm2)

        self.assertEqual(email.msg["From"], self.frm2)

    def test_subj_list(self):

        """Function:  test_subj_string

        Description:  Test subject line as a string.

        Arguments:

        """

        email = gen_class.Mail2(self.subj4, self.toaddr, fromaddr=self.frm2)

        self.assertEqual(
            (email.msg["Subject"], email.msg["To"], email.msg["From"]),
            (self.subj4a, self.toaddr2, self.frm2))

    def test_subj_string(self):

        """Function:  test_subj_string

        Description:  Test subject line as a string.

        Arguments:

        """

        email = gen_class.Mail2(self.subj3, self.toaddr, fromaddr=self.frm2)

        self.assertEqual(
            (email.msg["Subject"], email.msg["To"], email.msg["From"]),
            (self.subj3, self.toaddr2, self.frm2))

    def test_to_string(self):

        """Function:  test_to_string

        Description:  Test to line with a string.

        Arguments:

        """

        email = gen_class.Mail2(self.subj3, self.toaddr2)

        self.assertEqual(
            (email.msg["Subject"], email.msg["To"]),
            (self.subj3, self.toaddr2))

    def test_to_list2(self):

        """Function:  test_to_list2

        Description:  Test to line with a list.

        Arguments:

        """

        email = gen_class.Mail2(self.subj4, self.toaddr3)

        self.assertEqual(
            (email.msg["Subject"], email.msg["To"]),
            (self.subj4a, self.toaddr3a))

    def test_to_list(self):

        """Function:  test_to_list

        Description:  Test to line with a list.

        Arguments:

        """

        email = gen_class.Mail2(self.subj4, self.toaddr)

        self.assertEqual(
            (email.msg["Subject"], email.msg["To"]),
            (self.subj4a, self.toaddr2))


if __name__ == "__main__":
    unittest.main()
