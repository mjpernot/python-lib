# Classification (U)

"""Program:  in_list.py

    Description:  Unit testing of in_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/in_list.py

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
        test_not_in_list
        test_in_list
        test_empty_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list = []
        self.list2 = [1, 2, 3]

        self.name1 = 2
        self.name2 = 4

        self.out1 = []
        self.out2 = [2]

    def test_not_in_list(self):

        """Function:  test_not_in_list

        Description:  Test with item not in list.

        Arguments:

        """

        self.assertEqual(gen_libs.in_list(self.name2, self.list2), self.out1)

    def test_in_list(self):

        """Function:  test_in_list

        Description:  Test with item in list.

        Arguments:

        """

        self.assertEqual(gen_libs.in_list(self.name1, self.list2), self.out2)

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test with empty list.

        Arguments:

        """

        self.assertEqual(gen_libs.in_list(self.name1, self.list), self.out1)


if __name__ == "__main__":
    unittest.main()
