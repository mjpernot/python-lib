#!/usr/bin/python
# Classification (U)

"""Program:  Mail_init.py

    Description:  Unit testing of Mail.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/Mail_init.py

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
        test_to_list -> Test to line with a list.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.to = ["mail_address@domain.name"]
        self.subj = None
        self.frm = None
        self.host_name = None
        self.host = None

    def test_to_list(self):

        """Function:  test_to_list

        Description:  Test to line with a list.

        Arguments:
            None

        """

        email = gen_class.Mail(self.to)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (self.to, None, None, None, None))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:
            None

        """

        email = gen_class.Mail(self.to)

        self.assertEqual((email.to, email.subj, email.frm, email.host_name,
                          email.host), (self.to, None, None, None, None))


if __name__ == "__main__":
    unittest.main()
