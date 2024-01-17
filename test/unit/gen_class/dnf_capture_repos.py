# Classification (U)

"""Program:  dnf_capture_repos.py

    Description:  Unit testing of Dnf.capture_repos in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_capture_repos.py

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
        test_repos

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

    def test_repos(self):

        """Function:  test_repos

        Description:  Test capture_repos method.

        Arguments:

        """

        self.dnf.capture_repos()

        self.assertTrue(self.dnf.base.sack)


if __name__ == "__main__":
    unittest.main()
