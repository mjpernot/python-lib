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
import dnf

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
