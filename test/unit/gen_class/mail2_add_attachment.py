# Classification (U)

"""Program:  mail2_add_attachment.py

    Description:  Unit testing of Mail2.add_attachment in gen_class.py.

    Usage:
        test/unit/gen_class/mail2_add_attachment.py

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
        test_no_ftype
        test_json_ftype

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = "mail_address@domain.name"
        self.subj = "Test_Subj"
        self.frm = "mail_address@domain.name"
        self.fname = "testfilename.txt"
        self.ftype = "json"
        self.data = {"tar": "x-tar", "sh": "x-sh"}

    def test_no_ftype(self):

        """Function:  test_no_ftype

        Description:  Test with None passed for ftype.

        Arguments:

        """

        email = gen_class.Mail2(self.subj, self.toaddr, fromaddr=self.frm)
        email.add_attachment(self.fname, None, self.data)

        self.assertFalse(self.fname in email.msg.as_string())

    def test_json_ftype(self):

        """Function:  test_json_ftype

        Description:  Test with json passed for ftype.

        Arguments:

        """

        email = gen_class.Mail2(self.subj, self.toaddr, fromaddr=self.frm)
        email.add_attachment(self.fname, self.ftype, self.data)

        self.assertTrue(self.fname in email.msg.as_string())


if __name__ == "__main__":
    unittest.main()
