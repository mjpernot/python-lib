# Classification (U)

"""Program:  dnf_get_all_repos.py

    Description:  Unit testing of Dnf.get_all_repos in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_all_repos.py

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
        test_repos_url
        test_repos

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] < 3 or distro.version() < '8':
            print("Python 2 or Linux 8 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.dnf = gen_class.Dnf()

    def test_repos_url(self):

        """Function:  test_repos_url

        Description:  Test with url being included.

        Arguments:

        """

        self.assertTrue(isinstance(self.dnf.get_all_repos(url=True)[0], tuple))

    def test_repos(self):

        """Function:  test_repos

        Description:  Test get_all_repos method.

        Arguments:

        """

        self.assertTrue(isinstance(self.dnf.get_all_repos(), list))


if __name__ == "__main__":
    unittest.main()
