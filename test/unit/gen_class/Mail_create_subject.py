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

    Methods:
        setUp -> Initialize testing environment.
        test_subj_list -> Test subject as a list.
        test_subj_string -> Test subject as a string.
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
        self.subj = "Test subject"
        self.subj2 = "Test subject2"
        self.subj3 = "This is a string"
        self.subj4 = ["This", "is", "a", "list"]
        self.subj4a = "This is a list"

    def test_subj_list(self):

        """Function:  test_subj_list

        Description:  Test subject as a list.

        Arguments:

        """

        email = gen_class.Mail(self.to)
        email.create_subject(subj=self.subj4)

        self.assertEqual(email.subj, self.subj4a)

    def test_subj_string(self):

        """Function:  test_subj_string

        Description:  Test subject as a string.

        Arguments:

        """

        email = gen_class.Mail(self.to)
        email.create_subject(subj=self.subj3)

        self.assertEqual(email.subj, self.subj3)

    def test_subj_overwrite(self):

        """Function:  test_subj_overwrite

        Description:  Test overwriting existing subject.

        Arguments:

        """

        email = gen_class.Mail(self.to, subj=self.subj)
        email.create_subject(subj=self.subj2)

        self.assertEqual(email.subj, self.subj2)

    def test_subject_none(self):

        """Function:  test_subject_none

        Description:  Test with no subject passed.

        Arguments:

        """

        email = gen_class.Mail(self.to, subj=self.subj)
        email.create_subject(subj=None)

        self.assertEqual(email.subj, self.subj)

    def test_no_subject(self):

        """Function:  test_no_subject

        Description:  Test creating subject.

        Arguments:

        """

        email = gen_class.Mail(self.to)
        email.create_subject(subj=self.subj)

        self.assertEqual(email.subj, self.subj)


if __name__ == "__main__":
    unittest.main()
