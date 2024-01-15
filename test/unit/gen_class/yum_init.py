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
import distro
import socket
import unittest

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

        if sys.version_info > (2, 8):
            print("Error: Python 3 does not support yum==3.4.3, skipping test")
            self.skipTest("Pre-conditions not met.")

        self.host_name = socket.gethostname()
        self.osys = distro.name()
        self.release = distro.version()
        self.distro = (distro.name(), distro.version(), distro.codename())

    def test_hostname(self):

        """Function:  test_hostname

        Description:  Test __init__ method with hostname argument.

        Arguments:

        """

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(
            (yum.host_name, yum.os_name, yum.release, yum.distro),
            (self.host_name, self.osys, self.release, self.distro))

    def test_no_hostname(self):

        """Function:  test_no_hostname

        Description:  Test __init__ method with hostname argument.

        Arguments:

        """

        yum = gen_class.Yum()

        self.assertEqual(
            (yum.host_name, yum.os_name, yum.release, yum.distro),
            (self.host_name, self.osys, self.release, self.distro))


if __name__ == "__main__":
    unittest.main()
