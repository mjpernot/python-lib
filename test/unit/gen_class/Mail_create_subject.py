#!/usr/bin/python
# Classification (U)

"""Program:  Mail_create_subject.py

    Description:  Unit testing of Mail.create_subject in gen_class.py.

    Usage:
        test/unit/gen_class/Mail_create_subject.py

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
        test_subj_overwrite -> Test overwriting existing subject.
        test_subject_none -> Test with no subject passed.
        test_no_subject -> Test creating subject.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.to = ["mail_address@domain.name"]

    def test_subj_overwrite(self):

        """Function:  test_subj_overwrite

        Description:  Test overwriting existing subject.

        Arguments:

        """

        subj = "Test subject"
        subj2 = "Test subject2"

        email = gen_class.Mail(self.to, subj=subj)

        email.create_subject(subj=subj2)

        self.assertEqual(email.subj, subj2)

    def test_subject_none(self):

        """Function:  test_subject_none

        Description:  Test with no subject passed.

        Arguments:

        """

        subj = "Test subject"

        email = gen_class.Mail(self.to, subj=subj)

        email.create_subject(subj=None)

        self.assertEqual(email.subj, subj)

    def test_no_subject(self):

        """Function:  test_no_subject

        Description:  Test creating subject.

        Arguments:

        """

        subj = "Test subject"

        email = gen_class.Mail(self.to)

        email.create_subject(subj=subj)

        self.assertEqual(email.subj, subj)


if __name__ == "__main__":
    unittest.main()
