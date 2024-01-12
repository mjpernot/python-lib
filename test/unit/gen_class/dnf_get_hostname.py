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
import distro
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

        if sys.version_info[0] < 3 or distro.version() < '8':
            print("Python 2 or Linux 7 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.host_name = socket.gethostname()

    def test_get_hostname(self):

        """Function:  test_get_hostname

        Description:  Test get_hostname method.

        Arguments:

        """

        dnf = gen_class.Dnf()

        self.assertEqual(dnf.get_hostname(), self.host_name)


if __name__ == "__main__":
    unittest.main()
