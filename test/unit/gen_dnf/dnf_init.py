# Classification (U)

"""Program:  dnf_init.py

    Description:  Unit testing of Dnf.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_init.py

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
import gen_dnf                      # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_osname
        test_release
        test_base
        test_distro

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dnf = gen_dnf.Dnf()
        self.distro = (distro.name(), distro.version(), distro.codename())
        self.release = distro.version()
        self.os_name = distro.name()

    def test_osname(self):

        """Function:  test_osname

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertEqual(self.dnf.os_name, self.os_name)

    def test_release(self):

        """Function:  test_release

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertEqual(self.dnf.release, self.release)

    def test_base(self):

        """Function:  test_base

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertIsInstance(self.dnf, gen_dnf.Dnf)

    def test_distro(self):

        """Function:  test_distro

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertEqual(self.dnf.distro, self.distro)


if __name__ == "__main__":
    unittest.main()
