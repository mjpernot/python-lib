# Classification (U)

"""Program:  yum_fetch_update_pkgs.py

    Description:  Unit testing of Yum.fetch_update_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/yum_fetch_update_pkgs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import socket
import unittest
import collections
import mock
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
        test_fetch_update_pkgs

    """

    def mock_get_update(self, pkgnarrow, patterns, ignore_case):

        """Function:  mock_get_update

        Description:  Mock function.

        Arguments:

        """

        rpmdb1 = collections.namedtuple('Rpmdb', 'name version arch repo')

        if pkgnarrow and patterns and ignore_case and not rpmdb1:
            rpmdb1 = collections.namedtuple('Rpmdb', 'name version arch repo')

        return [rpmdb1(name="Name", version="1.0", arch="Linux",
                       repo="RepoName")]

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
        self.update_pkgs = [{"package": "Name", "ver": "1.0", "arch": "Linux",
                             "repo": "RepoName"}]

    @mock.patch("gen_class.Yum.doPackageLists", mock_get_update)
    def test_fetch_update_pkgs(self):

        """Function:  test_fetch_update_pkgs

        Description:  Test returning update packages.

        Arguments:

        """

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(yum.fetch_update_pkgs(), self.update_pkgs)


if __name__ == "__main__":
    unittest.main()
