# Classification (U)

"""Program:  dnf_get_updates.py

    Description:  Unit testing of Dnf.get_updates in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_updates.py

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
        test_get_packages

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dnf = gen_class.Dnf()

    def test_get_packages(self):

        """Function:  test_get_packages

        Description:  Test get_updates method.

        Arguments:

        """

        self.assertTrue(isinstance(self.dnf.get_updates(), list))


if __name__ == "__main__":
    unittest.main()
