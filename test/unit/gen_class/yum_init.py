#!/usr/bin/python
# Classification (U)

"""Program:  yum_init.py

    Description:  Unit testing of Yum.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/yum_init.py

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
        test_hostname
        test_no_hostname

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
    def test_hostname(self, mock_system, mock_release, mock_distro):

        """Function:  test_hostname

        Description:  Test __init__ method with hostname argument.

        Arguments:

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(
            (yum.host_name, yum.os, yum.release, yum.distro),
            (self.host_name, self.osys, self.release, self.distro))

    @mock.patch("platform.linux_distribution")
    @mock.patch("socket.gethostname")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_no_hostname(self, mock_system, mock_release, mock_socket,
                         mock_distro):

        """Function:  test_no_hostname

        Description:  Test __init__ method with hostname argument.

        Arguments:

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_socket.return_value = "HOSTNAME"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        yum = gen_class.Yum()

        self.assertEqual(
            (yum.host_name, yum.os, yum.release, yum.distro),
            (self.host_name, self.osys, self.release, self.distro))


if __name__ == "__main__":
    unittest.main()
