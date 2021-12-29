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

    def test_dictionary_newline2(self):

        """Function:  test_dictionary_newline2

        Description:  Test with a dictionary argument with newline option and
            with no pre-existing data in email.

        Arguments:

        """

        msg2 = {1: "Test ", 2: "email ", 3: "line2"}
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(msg2, new_line=True)

        self.assertEqual((email.to, email.msg), (
            self.toaddr, '{"1": "Test ", "2": "email ", "3": "line2"}'))

    def test_dictionary_newline(self):

        """Function:  test_dictionary_newline

        Description:  Test with a dictionary argument with newline option.

        Arguments:

        """

        msg2 = {1: "Test ", 2: "email ", 3: "line2"}
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg, new_line=True)
        email.add_2_msg(msg2, new_line=True)

        self.assertEqual((email.to, email.msg), (
            self.toaddr,
            self.msg + "\n" + '{"1": "Test ", "2": "email ", "3": "line2"}'))

    def test_non_string_newline2(self):

        """Function:  test_non_string_newline2

        Description:  Test with a list argument with newline option and with
            no pre-existing data in email.

        Arguments:

        """

        msg2 = ["Test ", "email ", "line2"]
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(msg2, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, '["Test ", "email ", "line2"]'))

    def test_non_string_newline(self):

        """Function:  test_non_string_newline

        Description:  Test with a list argument with newline option.

        Arguments:

        """

        msg2 = ["Test ", "email ", "line2"]
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg, new_line=True)
        email.add_2_msg(msg2, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr,
                          self.msg + "\n" + '["Test ", "email ", "line2"]'))

    def test_add_newline2(self):

        """Function:  test_add_newline2

        Description:  Test with adding newline option with no pre-existing data
            in the email.

        Arguments:

        """

        msg2 = "Test email line2"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(msg2, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, msg2))

    def test_add_newline(self):

        """Function:  test_add_newline

        Description:  Test with adding newline option.

        Arguments:

        """

        msg2 = "Test email line2"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(msg2, new_line=True)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + "\n" + msg2))

    def test_default_newline2(self):

        """Function:  test_default_newline2

        Description:  Test with using default newline option with no
            pre-existing data in the email.

        Arguments:

        """

        msg2 = "Test email line2"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(msg2)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, msg2))

    def test_default_newline(self):

        """Function:  test_default_newline

        Description:  Test with using default newline option.

        Arguments:

        """

        msg2 = "Test email line2"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(msg2)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + msg2))

    def test_non_string2(self):

        """Function:  test_non_string2

        Description:  Test with a dictionary argument.

        Arguments:

        """

        msg2 = {1: "Test ", 2: "email ", 3: "line2"}
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(msg2)

        self.assertEqual((email.to, email.msg), (
            self.toaddr,
            self.msg + '{"1": "Test ", "2": "email ", "3": "line2"}'))

    def test_non_string(self):

        """Function:  test_non_string

        Description:  Test with a list argument.

        Arguments:

        """

        msg2 = ["Test ", "email ", "line2"]
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(msg2)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr,
                          self.msg + '["Test ", "email ", "line2"]'))

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

        msg2 = "Test email line2"
        email = gen_class.Mail(self.toaddr)
        email.add_2_msg(self.msg)
        email.add_2_msg(msg2)

        self.assertEqual((email.to, email.msg),
                         (self.toaddr, self.msg + msg2))

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
