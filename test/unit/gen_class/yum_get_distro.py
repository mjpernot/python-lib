# Classification (U)

"""Program:  yum_get_distro.py

    Description:  Unit testing of Yum.get_distro in gen_class.py.

    Usage:
        test/unit/gen_class/yum_get_distro.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import socket
import unittest
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
        test_get_distro

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

    def test_get_distro(self):

        """Function:  test_get_distro

        Description:  Test get_distro method.

        Arguments:

        """

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(yum.get_distro(), self.distro)


if __name__ == "__main__":
    unittest.main()
