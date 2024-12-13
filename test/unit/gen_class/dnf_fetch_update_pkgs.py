# Classification (U)

"""Program:  dnf_fetch_update_pkgs.py

    Description:  Unit testing of Dnf.fetch_update_pkgs in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_fetch_update_pkgs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_fetch_install_pkgs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dnf = gen_class.Dnf()

    def test_fetch_install_pkgs(self):

        """Function:  test_fetch_install_pkgs

        Description:  Test returning installed packages.

        Arguments:

        """

        data = self.dnf.fetch_update_pkgs()

        self.assertTrue(
            isinstance(data, list) and
            ((len(data) > 0 and isinstance(data[0], dict)) or len(data) == 0))


if __name__ == "__main__":
    unittest.main()
