# Classification (U)

"""Program:  dnf_get_release.py

    Description:  Unit testing of Dnf.get_release in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_release.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
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
        test_get_release

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_name = "HOSTNAME"
        self.release = distro.version()

    def test_get_release(self):

        """Function:  test_get_release

        Description:  Test get_release method.

        Arguments:

        """

        dnf = gen_class.Dnf()

        self.assertEqual(dnf.get_release(), self.release)


if __name__ == "__main__":
    unittest.main()
