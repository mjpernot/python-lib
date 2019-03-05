#!/usr/bin/python
# Classification (U)

"""Program:  Yum_fetch_install_pkgs.py

    Description:  Unit testing of Yum.fetch_install_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/Yum_fetch_install_pkgs.py

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
import mock

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
        test_get_release -> Test returning OS platform name.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.host_name = "HOSTNAME"
        self.os = "Linux"
        self.release = "2.6"
        self.distro = ("Centos", "7.5.1804", "Core")
        self.rpmdb = [{"Package": "Name", "Ver": "1.0", "Arch": "Linux"}]
        self.fetch_pkgs = [{"Package": "Name", "Ver": "1.0", "Arch": "Linux"}]

    @mock.patch("gen_class.Yum.fetch_install_pkgs")
    @mock.patch("platform.linux_distribution")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_fetch_install_pkgs(self, mock_system, mock_release, mock_distro,
                                mock_fetch):

        """Function:  test_fetch_install_pkgs

        Description:  Test fetch_install_pkgs method.

        Arguments:
            mock_system -> Mock Ref:  platform.system
            mock_release -> Mock Ref:  platform.release
            mock_distro -> Mock Ref:  platform.linux_distribution
            mock_fetch -> Mock Ref:  gen_class.Yum.fetch_install_pkgs

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")
        mock_fetch.return_value = self.rpmdb

        YUM = gen_class.Yum(self.host_name)

        self.assertEqual(YUM.fetch_install_pkgs(), self.fetch_pkgs)


if __name__ == "__main__":
    unittest.main()
