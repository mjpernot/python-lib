#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import collections
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
        setUp -> Initialize testing environment.
        test_fetch_install_pkgs -> Test returning installed packages.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_name = "HOSTNAME"
        self.osys = "Linux"
        self.release = "2.6"
        self.distro = ("Centos", "7.5.1804", "Core")
        self.rpmdb = collections.namedtuple('Rpmdb', 'name version arch')

        self.fetch_pkgs = [{"package": "Name", "ver": "1.0", "arch": "Linux"}]

    @mock.patch("platform.linux_distribution")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_fetch_install_pkgs(self, mock_system, mock_release, mock_distro):

        """Function:  test_fetch_install_pkgs

        Description:  Test returning installed packages.

        Arguments:

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        yum = gen_class.Yum(self.host_name)
        yum.rpmdb = [self.rpmdb(name="Name", version="1.0", arch="Linux")]

        self.assertEqual(yum.fetch_install_pkgs(), self.fetch_pkgs)


if __name__ == "__main__":
    unittest.main()
