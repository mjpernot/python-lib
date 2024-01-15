# Classification (U)

"""Program:  yum_fetch_install_pkgs.py

    Description:  Unit testing of Yum.fetch_install_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/yum_fetch_install_pkgs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import socket
import distro
import unittest
import collections

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

        if sys.version_info > (2, 8):
            print("Error: Python 3 does not support yum==3.4.3, skipping test")
            self.skipTest("Pre-conditions not met.")

        self.host_name = socket.gethostname()
        self.osys = distro.name()
        self.release = distro.version()
        self.distro = (distro.name(), distro.version(), distro.codename())
        self.rpmdb = collections.namedtuple('Rpmdb', 'name version arch')

        self.fetch_pkgs = [{"package": "Name", "ver": "1.0", "arch": "Linux"}]

    def test_fetch_install_pkgs(self):

        """Function:  test_fetch_install_pkgs

        Description:  Test returning installed packages.

        Arguments:

        """

        yum = gen_class.Yum(self.host_name)
        yum.rpmdb = [self.rpmdb(name="Name", version="1.0", arch="Linux")]

        self.assertEqual(yum.fetch_install_pkgs(), self.fetch_pkgs)


if __name__ == "__main__":
    unittest.main()
