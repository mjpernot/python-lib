# Classification (U)

"""Program:  dnf_get_hostname.py

    Description:  Unit testing of Dnf.get_hostname in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_hostname.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import socket
import unittest

# Local
sys.path.append(os.getcwd())
import gen_dnf                      # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_hostname

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_name = socket.gethostname()

    def test_get_hostname(self):

        """Function:  test_get_hostname

        Description:  Test get_hostname method.

        Arguments:

        """

        dnf = gen_dnf.Dnf()

        self.assertEqual(dnf.get_hostname(), self.host_name)


if __name__ == "__main__":
    unittest.main()
