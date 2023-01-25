# Classification (U)

"""Program:  is_missing_lists.py

    Description:  Unit testing of is_missing_lists in gen_libs.py.

    Usage:
        test/unit/gen_libs/is_missing_lists.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_some_missing
        test_no_missing

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list1a = ["A", "B", "C"]
        self.list2a = ["A", "B", "C"]
        self.list2b = ["A"]
        self.result1 = []
        self.result2 = ["B", "C"]

    def test_some_missing(self):

        """Function:  test_some_missing

        Description:  Test with some items missing.

        Arguments:

        """

        self.assertEqual(gen_libs.is_missing_lists(self.list1a, self.list2b),
                         self.result2)

    def test_no_missing(self):

        """Function:  test_no_missing

        Description:  Test with no items missing.

        Arguments:

        """

        self.assertEqual(gen_libs.is_missing_lists(self.list1a, self.list2a),
                         self.result1)


if __name__ == "__main__":
    unittest.main()
