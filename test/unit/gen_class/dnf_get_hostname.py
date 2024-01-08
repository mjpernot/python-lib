# Classification (U)

"""Program:  dnf_get_hostname.py

    Description:  Unit testing of Dnf.get_hostname in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_hostname.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import platform
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
        test_get_hostname

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] < 3 or platform.linux_distribution()[1] < '8':
            print("Python 2 or Linux 7 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.host_name = "HOSTNAME"
        self.osys = "Linux"
        self.release = "4.18.0"
        self.distro = ("Red Hat Enterprise Linux", "8.7", "Ootpa")

    @mock.patch("platform.linux_distribution")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_get_hostname(self, mock_system, mock_release, mock_distro):

        """Function:  test_get_hostname

        Description:  Test get_hostname method.

        Arguments:

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "4.18.0"
        self.distro = ("Red Hat Enterprise Linux", "8.7", "Ootpa")

        dnf = gen_class.Dnf(self.host_name)

        self.assertEqual(dnf.get_hostname(), self.host_name)


if __name__ == "__main__":
    unittest.main()
