# Classification (U)

"""Program:  dnf_get_os.py

    Description:  Unit testing of Dnf.get_os in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_os.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import distro

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
        test_get_os

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_name = "HOSTNAME"
        self.osys = distro.name()

    def test_get_os(self):

        """Function:  test_get_os

        Description:  Test get_os method.

        Arguments:

        """

        dnf = gen_dnf.Dnf()

        self.assertEqual(dnf.get_os(), self.osys)


if __name__ == "__main__":
    unittest.main()
