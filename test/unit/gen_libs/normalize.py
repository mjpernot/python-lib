# Classification (U)

"""Program:  normalize.py

    Description:  Unit testing of normalize in gen_libs.py.

    Usage:
        test/unit/gen_libs/normalize.py

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
        test_rng3
        test_rng2
        test_rng1

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.rng = [(12, 15), (1, 10)]
        self.rng2 = [(1, 12), (12, 15)]
        self.rng3 = [(1, 22), (12, 15)]
        self.rng4 = [[(1, 22)]]
        self.result = [(1, 10), (12, 15)]
        self.result2 = [(1, 15)]
        self.result3 = [(1, 22)]
        self.result4 = [((1, 22), (1, 22))]

    def test_rng4(self):

        """Function:  test_rng4

        Description:  Test with one range encompassing all ranges.

        Arguments:

        """

        self.assertEqual(gen_libs.normalize(self.rng4), self.result4)

    def test_rng3(self):

        """Function:  test_rng3

        Description:  Test with one range encompassing all ranges.

        Arguments:

        """

        self.assertEqual(gen_libs.normalize(self.rng3), self.result3)

    def test_rng2(self):

        """Function:  test_rng2

        Description:  Test with two consective sets of ranges.

        Arguments:

        """

        self.assertEqual(gen_libs.normalize(self.rng2), self.result2)

    def test_rng1(self):

        """Function:  test_rng1

        Description:  Test with two sets of ranges.

        Arguments:

        """

        self.assertEqual(gen_libs.normalize(self.rng), self.result)


if __name__ == "__main__":
    unittest.main()
