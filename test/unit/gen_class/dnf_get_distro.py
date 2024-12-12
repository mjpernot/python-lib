# Classification (U)

"""Program:  dnf_get_distro.py

    Description:  Unit testing of Dnf.get_distro in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_distro.py

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
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

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

        self.distro = (distro.name(), distro.version(), distro.codename())

    def test_get_distro(self):

        """Function:  test_get_distro

        Description:  Test get_distro method.

        Arguments:

        """

        dnf = gen_class.Dnf()

        self.assertEqual(dnf.get_distro(), self.distro)


if __name__ == "__main__":
    unittest.main()
