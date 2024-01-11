# Classification (U)

"""Program:  dnf_get_distro.py

    Description:  Unit testing of Dnf.get_distro in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_distro.py

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
        test_get_distro

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] < 3 or distro.version() < '8':
            print("Python 2 or Linux 7 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.distro = distro.linux_distribution()

    def test_get_distro(self):

        """Function:  test_get_distro

        Description:  Test get_distro method.

        Arguments:

        """

        dnf = gen_class.Dnf()

        self.assertEqual(dnf.get_distro(), self.distro)


if __name__ == "__main__":
    unittest.main()
