#!/usr/bin/python
# Classification (U)

"""Program:  Mail_create_body.py

    Description:  Unit testing of Mail.create_body in gen_class.py.

    Usage:
        test/unit/gen_class/Mail_create_body.py

    Arguments:
        None

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

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_long_subject -> Test with subject line to maximum.
        test_with_subject -> Test creating body with subject line in place.
        test_create_body -> Test creating body.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.to = ["mail_address@domain.name"]

    def test_long_subject(self):

        """Function:  test_long_subject

        Description:  Test with subject line to maximum.

        Arguments:
            None

        """

        msg = "Test email line with a line greater than thirty characters"

        email = gen_class.Mail(self.to)
        email.add_2_msg(msg)

        email.create_body()

        self.assertEqual(email.create_body(),
                         ("Subject: %s\n\n%s" % (msg[:30], msg)))

    def test_with_subject(self):

        """Function:  test_with_subject

        Description:  Test creating body with subject line in place.

        Arguments:
            None

        """

        msg = "Test email line"
        subj = "Test subject"

        email = gen_class.Mail(self.to, subj=subj)
        email.add_2_msg(msg)

        email.create_body()

        self.assertEqual(email.create_body(),
                         ("Subject: %s\n\n%s" % (subj, msg)))

    def test_create_body(self):

        """Function:  test_create_body

        Description:  Test creating body.

        Arguments:
            None

        """

        msg = "Test email line"

        email = gen_class.Mail(self.to)
        email.add_2_msg(msg)

        email.create_body()

        self.assertEqual(email.create_body(),
                         ("Subject: %s\n\n%s" % (msg, msg)))


if __name__ == "__main__":
    unittest.main()
