#!/usr/bin/python
# Classification (U)

"""Program:  Mail_create_subject.py

    Description:  Unit testing of Mail.create_subject in gen_class.py.

    Usage:
        test/unit/gen_class/Mail_create_subject.py

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
        test_no_subject -> Test creating body with subject line in place.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.to = ["mail_address@domain.name"]

    def test_no_subject(self):

        """Function:  test_no_subject

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


if __name__ == "__main__":
    unittest.main()
