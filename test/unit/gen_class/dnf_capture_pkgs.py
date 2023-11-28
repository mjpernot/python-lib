# Classification (U)

"""Program:  dnf_capture_pkgs.py

    Description:  Unit testing of Dnf.capture_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_capture_pkgs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
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
        test_packages

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dnf = gen_class.Dnf()

    def test_packages(self):

        """Function:  test_packages

        Description:  Test capture_pkgs method.

        Arguments:

        """

        self.dnf.capture_pkgs()

        self.assertTrue(self.dnf.packages)


if __name__ == "__main__":
    unittest.main()
