fetch_install_pkgs# Classification (U)

"""Program:  dnf_fetch_install_pkgs.py

    Description:  Unit testing of Dnf.fetch_install_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_fetch_install_pkgs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import platform
import unittest

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
        test_fetch_install_pkgs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] < 3 or platform.linux_distribution()[1] < '8':
            print("Python 2 or Linux 7 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.dnf = gen_class.Dnf()

    def test_fetch_install_pkgs(self):

        """Function:  test_fetch_install_pkgs

        Description:  Test returning installed packages.

        Arguments:

        """

        data = self.dnf.fetch_install_pkgs()

        self.assertTrue(isinstance(data, list) and isinstance(data[0], dict))


if __name__ == "__main__":
    unittest.main()