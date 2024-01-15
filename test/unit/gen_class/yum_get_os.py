# Classification (U)

"""Program:  yum_get_os.py

    Description:  Unit testing of Yum.get_os in gen_class.py.

    Usage:
        test/unit/gen_class/yum_get_os.py

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
        test_get_os

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

    def test_get_os(self):

        """Function:  test_get_os

        Description:  Test get_os method.

        Arguments:

        """

        yum = gen_class.Yum(self.host_name)

        self.assertEqual(yum.get_os(), self.osys)


if __name__ == "__main__":
    unittest.main()
