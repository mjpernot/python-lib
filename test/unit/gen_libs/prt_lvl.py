# Classification (U)

"""Program:  prt_lvl.py

    Description:  Unit testing of prt_lvl in gen_libs.py.

    Usage:
        test/unit/gen_libs/prt_lvl.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_set_lvl
        test_default_lvl
        test_zero_lvl

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.lvl0 = 0
        self.lvl2 = 2

    def test_set_lvl(self):

        """Function:  test_set_lvl

        Description:  Test with set level.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_lvl(self.lvl2))

    def test_default_lvl(self):

        """Function:  test_default_lvl

        Description:  Test with default level.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_lvl())

    def test_zero_lvl(self):

        """Function:  test_prt_lvl

        Description:  Test with zero level.

        Arguments:

        """

        self.assertFalse(gen_libs.prt_lvl(self.lvl0))


if __name__ == "__main__":
    unittest.main()
