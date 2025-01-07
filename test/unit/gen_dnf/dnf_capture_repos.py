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
        test_repos

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dnf = gen_dnf.Dnf()

    def test_repos(self):

        """Function:  test_repos

        Description:  Test capture_repos method.

        Arguments:

        """

        self.dnf.capture_repos()

        self.assertTrue(self.dnf.base.sack)


if __name__ == "__main__":
    unittest.main()
