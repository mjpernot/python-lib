#!/usr/bin/python
# Classification (U)

"""Program:  Yum_get_os.py

    Description:  Unit testing of Yum.get_os in gen_class.py.

    Usage:
        test/unit/gen_class/Yum_get_os.py

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
        test_get_os -> Test returning OS platform name.

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
    def test_get_os(self, mock_system, mock_release, mock_distro):

        """Function:  test_get_os

        Description:  Test get_os method.

        Arguments:
            mock_system -> Mock Ref:  platform.system
            mock_release -> Mock Ref:  platform.release
            mock_distro -> Mock Ref:  platform.linux_distribution

        """

        mock_system.return_value = "Linux"
        mock_release.return_value = "2.6"
        mock_distro.return_value = ("Centos", "7.5.1804", "Core")

        YUM = gen_class.Yum(self.host_name)

        self.assertEqual(YUM.get_os(), self.os)


if __name__ == "__main__":
    unittest.main()
