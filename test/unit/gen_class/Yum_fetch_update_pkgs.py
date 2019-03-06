#!/usr/bin/python
# Classification (U)

"""Program:  Yum_fetch_update_pkgs.py

    Description:  Unit testing of Yum.fetch_update_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/Yum_fetch_update_pkgs.py

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
import collections

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
        test_fetch_update_pkgs -> Test returning update packages.

    """

    def mock_get_update(self, pkgnarrow, patterns, ignore_case):
        rpmdb1 = collections.namedtuple('Rpmdb', 'name version arch repo')
        return [rpmdb1(name="Name", version="1.0", arch="Linux",
                       repo="RepoName")]

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
        self.update_pkgs = [{"package": "Name", "ver": "1.0", "arch": "Linux",
                             "repo": "RepoName"}]

    @mock.patch("gen_class.Yum.doPackageLists", mock_get_update)
    @mock.patch("platform.linux_distribution")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_fetch_update_pkgs(self, mock_system, mock_release, mock_distro):

        """Function:  test_fetch_update_pkgs

        Description:  Test returning update packages.

        Arguments:
            mock_system -> Mock Ref:  platform.system
            mock_release -> Mock Ref:  platform.release
            mock_distro -> Mock Ref:  platform.linux_distribution

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(yum.fetch_update_pkgs(), self.update_pkgs)


if __name__ == "__main__":
    unittest.main()
