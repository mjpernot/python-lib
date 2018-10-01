#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      Yum_init.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_class       => 2.4.0 or higher
#
###############################################################################

"""Program:  Yum_init.py

    Description:  Unit testing of Yum.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/Yum_init.py

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

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_hostname -> Test with hostname argument.
        test_no_hostname -> Test with no hostname argument.

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

    @mock.patch("platform.linux_distribution")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_hostname(self, mock_system, mock_release, mock_distro):

        """Function:  test_hostname

        Description:  Test __init__ method with hostname argument.

        Arguments:
            mock_system -> Mock Ref:  platform.system
            mock_release -> Mock Ref:  platform.release
            mock_distro -> Mock Ref:  platform.linux_distribution

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        YUM = gen_class.Yum(self.host_name)

        self.assertEqual((YUM.host_name, YUM.os, YUM.release, YUM.distro),
                         (self.host_name, self.os, self.release, self.distro))

    @mock.patch("platform.linux_distribution")
    @mock.patch("socket.gethostname")
    @mock.patch("platform.release")
    @mock.patch("platform.system")
    def test_no_hostname(self, mock_system, mock_release, mock_socket,
                         mock_distro):

        """Function:  test_no_hostname

        Description:  Test __init__ method with hostname argument.

        Arguments:
            mock_system -> Mock Ref:  platform.system
            mock_release -> Mock Ref:  platform.release
            mock_socket -> Mock Ref:  socket.gethostname
            mock_distro -> Mock Ref:  platform.linux_distribution

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_socket.return_value = "HOSTNAME"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        YUM = gen_class.Yum()

        self.assertEqual((YUM.host_name, YUM.os, YUM.release, YUM.distro),
                         (self.host_name, self.os, self.release, self.distro))


if __name__ == "__main__":
    unittest.main()
