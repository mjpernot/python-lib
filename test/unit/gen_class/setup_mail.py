# Classification (U)

"""Program:  setup_mail.py

    Description:  Unit testing of setup_mail in gen_class.py.

    Usage:
        test/unit/gen_class/setup_mail.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import socket
import getpass
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_with_subj_list
        test_with_from_line
        test_no_from_line

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.to_line = "email_address"
        self.subj = "subject_line"
        self.frm_line = "from_email_address"

    def test_with_subj_list(self):

        """Function:  test_with_subj_list

        Description:  Test with subject line being a list.

        Arguments:

        """

        mail = gen_class.setup_mail([self.to_line], [self.subj], self.frm_line)

        self.assertEqual((mail.toaddr, mail.subj, mail.frm),
                         ([self.to_line], self.subj, self.frm_line))

    def test_with_from_line(self):

        """Function:  test_with_from_line

        Description:  Test with from line passed.

        Arguments:

        """

        mail = gen_class.setup_mail([self.to_line], [self.subj], self.frm_line)

        self.assertEqual((mail.toaddr, mail.subj, mail.frm),
                         ([self.to_line], self.subj, self.frm_line))

    def test_no_from_line(self):

        """Function:  test_no_from_line

        Description:  Test with no from line passed.

        Arguments:

        """

        mail = gen_class.setup_mail([self.to_line])
        from_line = getpass.getuser() + "@" + socket.gethostname()

        self.assertEqual((mail.toaddr, mail.subj, mail.frm),
                         ([self.to_line], None, from_line))


if __name__ == "__main__":
    unittest.main()
