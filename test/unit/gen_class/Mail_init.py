#!/usr/bin/python
# Classification (U)

"""Program:  Mail_init.py

    Description:  Unit testing of Mail.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/Mail_init.py

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

# Local
sys.path.append(os.getcwd())
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_subj_list -> Test subject line as a list.
        test_subj_string -> Test subject line as a string.
        test_with_data -> Test other attributes with data.
        test_to_string -> Test to line with a string.
        test_to_list -> Test to line with a list.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.to = ["mail_address@domain.name"]
        self.subj = None
        self.subj2 = "Test_Subj"
        self.subj3 = "This is a test"
        self.subj4 = ["This", "is", "a", "test"]
        self.subj4a = "Thisisatest"
        self.frm = None
        self.frm2 = "mail_address@domain.name"
        self.host_name = None
        self.host = None

    def test_subj_list(self):

        """Function:  test_subj_string

        Description:  Test subject line as a string.

        Arguments:

        """

        email = gen_class.Mail(self.to, subj=self.subj4, frm=self.frm2)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (email.to, self.subj4a, self.frm2, None,
                                        None))

    def test_subj_string(self):

        """Function:  test_subj_string

        Description:  Test subject line as a string.

        Arguments:

        """

        email = gen_class.Mail(self.to, subj=self.subj3, frm=self.frm2)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (email.to, self.subj3, self.frm2, None,
                                        None))

    def test_with_data(self):

        """Function:  test_with_data

        Description:  Test other attributes with data.

        Arguments:

        """

        email = gen_class.Mail(self.to, subj=self.subj2, frm=self.frm2)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (email.to, self.subj2, self.frm2, None,
                                        None))

    def test_to_string(self):

        """Function:  test_to_string

        Description:  Test to line with a string.

        Arguments:

        """

        email = gen_class.Mail(self.to)

        self.assertEqual(("mail_address@domain.name", email.subj, email.frm,
                          email.host_name, email.host),
                         ("mail_address@domain.name", None, None, None, None))

    def test_to_list(self):

        """Function:  test_to_list

        Description:  Test to line with a list.

        Arguments:

        """

        email = gen_class.Mail(self.to)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (self.to, None, None, None, None))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        email = gen_class.Mail(self.to)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (self.to, None, None, None, None))


if __name__ == "__main__":
    unittest.main()
