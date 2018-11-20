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
        test_create_body -> Test creating body.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.to = ["mail_address@domain.name"]

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
