#!/usr/bin/python
# Classification (U)

"""Program:  yum_get_hostname.py

    Description:  Unit testing of Yum.get_hostname in gen_class.py.

    Usage:
        test/unit/gen_class/yum_get_hostname.py

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

        self.host_name = "HOSTNAME"
        self.osys = "Linux"
        self.release = "2.6"
        self.distro = ("Centos", "7.5.1804", "Core")

    @mock.patch("platform.linux_distribution")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_get_hostname(self, mock_system, mock_release, mock_distro):

        """Function:  test_get_hostname

        Description:  Test get_hostname method.

        Arguments:

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(yum.get_hostname(), self.host_name)


if __name__ == "__main__":
    unittest.main()
