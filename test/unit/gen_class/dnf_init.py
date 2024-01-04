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
import platform
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
        test_base
        test_packages

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] < 3 and platform.linux_distribution()[1] < '8':
            print("Python 2 or Linux 8 platforms do not support dnf, skipping")
            self.skipTest("Pre-conditions not met.")

        self.dnf = gen_class.Dnf()

    def test_base(self):

        """Function:  test_base

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertTrue(isinstance(self.dnf, gen_class.Dnf))

    def test_packages(self):

        """Function:  test_packages

        Description:  Test __init__ method.

        Arguments:

        """

        self.assertEqual(self.dnf.packages, None)


if __name__ == "__main__":
    unittest.main()
