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
import distro
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

        if sys.version_info[0] < 3 or distro.version() < '8':
            print("Python 2 or Linux 7 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.dnf = gen_class.Dnf()
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

        self.assertTrue(isinstance(self.dnf, gen_class.Dnf))

    def test_distro(self):

        """Function:  test_distro

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertEqual(self.dnf.distro, self.distro)


if __name__ == "__main__":
    unittest.main()
