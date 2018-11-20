#!/usr/bin/python
# Classification (U)

"""Program:  Mail_add_2_msg.py

    Description:  Unit testing of Mail.add_2_msg in gen_class.py.

    Usage:
        test/unit/gen_class/Mail_add_2_msg.py

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
        test_empty_test -> Test with empty text line.
        test_add_exist -> Test with adding data to existing message.
        test_initial_add -> Test with adding data to empty message.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.to = ["mail_address@domain.name"]

    def test_empty_test(self):

        """Function:  test_empty_test

        Description:  Test with empty text line.

        Arguments:
            None

        """

        msg = "Test email line"

        email = gen_class.Mail(self.to)

        email.add_2_msg(msg)
        email.add_2_msg()

        self.assertEqual((email.to, email.msg), (self.to, msg))

    def test_add_exist(self):

        """Function:  test_add_exist

        Description:  Test with adding data to existing message.

        Arguments:
            None

        """

        msg = "Test email line"
        msg2 = "Test email line2"

        email = gen_class.Mail(self.to)

        email.add_2_msg(msg)
        email.add_2_msg(msg2)

        self.assertEqual((email.to, email.msg), (self.to, msg + msg2))

    def test_initial_add(self):

        """Function:  test_initial_add

        Description:  Test with adding data to empty message.

        Arguments:
            None

        """

        msg = "Test email line"

        email = gen_class.Mail(self.to)

        email.add_2_msg(msg)

        self.assertEqual((email.to, email.msg), (self.to, msg))


if __name__ == "__main__":
    unittest.main()
