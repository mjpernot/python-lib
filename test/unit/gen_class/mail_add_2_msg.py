#!/usr/bin/python
# Classification (U)

"""Program:  mail_add_2_msg.py

    Description:  Unit testing of Mail.add_2_msg in gen_class.py.

    Usage:
        test/unit/gen_class/mail_add_2_msg.py

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
        test_dictionary_newline2
        test_dictionary_newline
        test_non_string_newline2
        test_non_string_newline
        test_add_newline2
        test_add_newline
        test_default_newline
        test_non_string2
        test_non_string
        test_empty_test
        test_add_exist
        test_initial_add

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.toaddr = ["mail_address@domain.name"]
        self.msg = "Test email line"
        self.msg2 = {1: "Test ", 2: "email ", 3: "line2"}
        self.msg3 = ["Test ", "email ", "line2"]
        self.msg4 = "Test email line2"
        self.results = '{"1": "Test ", "2": "email ", "3": "line2"}'
        self.results2 = '["Test ", "email ", "line2"]'

    def test_dictionary_newline2(self):

        """Function:  test_dictionary_newline2

        Description:  Test with a dictionary argument with newline option and
            with no pre-existing data in email.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg2, new_line=True)

        self.assertEqual((email.to, email.msg), (self.toaddr, self.results))

    def test_dictionary_newline(self):

        """Function:  test_dictionary_newline

        Description:  Test with a dictionary argument with newline option.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg, new_line=True)
        email.add_2_msg(self.msg2, new_line=True)

        self.assertEqual((email.to, email.msg), (
            self.toaddr, self.msg + "\n" + self.results))

    def test_non_string_newline2(self):

        """Function:  test_non_string_newline2

        Description:  Test with a list argument with newline option and with
            no pre-existing data in email.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg3, new_line=True)

        self.assertEqual((email.to, email.msg), (self.toaddr, self.results2))

    def test_non_string_newline(self):

        """Function:  test_non_string_newline

        Description:  Test with a list argument with newline option.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg, new_line=True)
        email.add_2_msg(self.msg3, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + "\n" + self.results2))

    def test_add_newline2(self):

        """Function:  test_add_newline2

        Description:  Test with adding newline option with no pre-existing data
            in the email.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg4, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg4))

    def test_add_newline(self):

        """Function:  test_add_newline

        Description:  Test with adding newline option.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(self.msg4, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + "\n" + self.msg4))

    def test_default_newline2(self):

        """Function:  test_default_newline2

        Description:  Test with using default newline option with no
            pre-existing data in the email.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg4)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg4))

    def test_default_newline(self):

        """Function:  test_default_newline

        Description:  Test with using default newline option.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(self.msg4)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + self.msg4))

    def test_non_string2(self):

        """Function:  test_non_string2

        Description:  Test with a dictionary argument.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(self.msg2)

        self.assertEqual((email.to, email.msg), (
            self.toaddr, self.msg + self.results))

    def test_non_string(self):

        """Function:  test_non_string

        Description:  Test with a list argument.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(self.msg3)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + self.results2))

    def test_empty_test(self):

        """Function:  test_empty_test

        Description:  Test with empty text line.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg()

        self.assertEqual((email.to, email.msg), (self.toaddr, self.msg))

    def test_add_exist(self):

        """Function:  test_add_exist

        Description:  Test with adding data to existing message.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(self.msg4)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + self.msg4))

    def test_initial_add(self):

        """Function:  test_initial_add

        Description:  Test with adding data to empty message.

        Arguments:

        """

        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)

        self.assertEqual((email.to, email.msg), (self.toaddr, self.msg))


if __name__ == "__main__":
    unittest.main()
