# Classification (U)

"""Program:  get_base_dir.py

    Description:  Unit testing of get_base_dir in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_base_dir.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
        test_get_base_dir

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cur_path = os.path.dirname(os.path.realpath(__file__))

    def test_get_base_dir(self):

        """Function:  test_get_base_dir

        Description:  Test get_base_dir function with 0 pattern found.

        Arguments:

        """

        self.assertEqual(gen_libs.get_base_dir(sys.argv[0]), self.cur_path)


if __name__ == "__main__":
    unittest.main()
