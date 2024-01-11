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
import distro
import unittest
import mock

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
        test_get_os

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] < 3 or distro.version() < '8':
            print("Python 2 or Linux 7 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.host_name = "HOSTNAME"
        self.osys = distro.linux_distribution()[0]

    def test_get_os(self):

        """Function:  test_get_os

        Description:  Test get_os method.

        Arguments:

        """

        dnf = gen_class.Dnf(self.host_name)

        self.assertEqual(dnf.get_os(), self.osys)


if __name__ == "__main__":
    unittest.main()
