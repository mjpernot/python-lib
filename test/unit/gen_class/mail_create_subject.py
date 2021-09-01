#!/usr/bin/python
# Classification (U)

"""Program:  mail_create_subject.py

    Description:  Unit testing of Mail.create_subject in gen_class.py.

    Usage:
        test/unit/gen_class/mail_create_subject.py

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
        test_subj_list_delimiter
        test_subj_list
        test_subj_string
        test_subj_overwrite
        test_subject_none
        test_no_subject

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = ["mail_address@domain.name"]
        self.subj = "Test subject"
        self.subj2 = "Test subject2"
        self.subj3 = "This is a string"
        self.subj4 = ["This", "is", "a", "list"]
        self.subj4a = "This is a list"
        self.subj4b = "This_is_a_list"
        self.subj4c = "Thisisalist"

    def test_subj_list_delimiter2(self):

        """Function:  test_subj_list_delimiter2

        Description:  Test with delimiter passed.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.create_subject(subj=self.subj4, delimiter="")

        self.assertEqual(email.subj, self.subj4c)

    def test_subj_list_delimiter(self):

        """Function:  test_subj_list_delimiter

        Description:  Test with delimiter passed.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.create_subject(subj=self.subj4, delimiter="_")

        self.assertEqual(email.subj, self.subj4b)

    def test_subj_list(self):

        """Function:  test_subj_list

        Description:  Test subject as a list.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.create_subject(subj=self.subj4)

        self.assertEqual(email.subj, self.subj4a)

    def test_subj_string(self):

        """Function:  test_subj_string

        Description:  Test subject as a string.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.create_subject(subj=self.subj3)

        self.assertEqual(email.subj, self.subj3)

    def test_subj_overwrite(self):

        """Function:  test_subj_overwrite

        Description:  Test overwriting existing subject.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj)
        email.create_subject(subj=self.subj2)

        self.assertEqual(email.subj, self.subj2)

    def test_subject_none(self):

        """Function:  test_subject_none

        Description:  Test with no subject passed.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr, subj=self.subj)
        email.create_subject(subj=None)

        self.assertEqual(email.subj, self.subj)

    def test_no_subject(self):

        """Function:  test_no_subject

        Description:  Test creating subject.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.create_subject(subj=self.subj)

        self.assertEqual(email.subj, self.subj)


if __name__ == "__main__":
    unittest.main()
