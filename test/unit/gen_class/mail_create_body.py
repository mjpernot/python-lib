#!/usr/bin/python
# Classification (U)

"""Program:  mail_create_body.py

    Description:  Unit testing of Mail.create_body in gen_class.py.

    Usage:
        test/unit/gen_class/mail_create_body.py

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

    Methods:
        setUp
        test_long_subject
        test_with_subject
        test_create_body

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = ["mail_address@domain.name"]
        self.subj_mask = "Subject: %s\n\n%s"

    def test_long_subject(self):

        """Function:  test_long_subject

        Description:  Test with subject line to maximum.

        Arguments:

        """

        msg = "Test email line with a line greater than thirty characters"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(msg)
        email.create_body()

        self.assertEqual(email.create_body(),
                         (self.subj_mask % (msg[:30], msg)))

    def test_with_subject(self):

        """Function:  test_with_subject

        Description:  Test creating body with subject line in place.

        Arguments:

        """

        msg = "Test email line"
        subj = "Test subject"
        email = gen_class.Mail(self.toaddr, subj=subj)
        email.add_2_msg(msg)
        email.create_body()

        self.assertEqual(email.create_body(), (self.subj_mask % (subj, msg)))

    def test_create_body(self):

        """Function:  test_create_body

        Description:  Test creating body.

        Arguments:

        """

        msg = "Test email line"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(msg)
        email.create_body()

        self.assertEqual(email.create_body(), (self.subj_mask % (msg, msg)))


if __name__ == "__main__":
    unittest.main()
