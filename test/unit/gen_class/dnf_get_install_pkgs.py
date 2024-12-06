# Classification (U)

"""Program:  dnf_get_install_pkgs.py

    Description:  Unit testing of Dnf.get_install_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_install_pkgs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import dnf
import distro

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
        test_get_install_pkgs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base2 = gen_class.Dnf()

    def test_get_install_pkgs(self):

        """Function:  test_get_install_pkgs

        Description:  Test returning installed packages.

        Arguments:

        """

        base = dnf.Base()
        base.fill_sack()
        pkgs = base.sack.query()
        pkgs2 = pkgs.installed()

        self.assertTrue(self.base2.get_install_pkgs()[0], pkgs2[0])


if __name__ == "__main__":
    unittest.main()
