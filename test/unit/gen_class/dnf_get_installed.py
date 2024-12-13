# Classification (U)

"""Program:  dnf_get_installed.py

    Description:  Unit testing of Dnf.get_installed in gen_class.py.

    Usage:
        test/unit/gen_class/dnf_get_installed.py

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

        Description:  Test get_installed method.

        Arguments:

        """

        self.assertIsInstance(self.dnf.get_installed(), list)


if __name__ == "__main__":
    unittest.main()
