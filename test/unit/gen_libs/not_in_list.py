#!/usr/bin/python
# Classification (U)

"""Program:  not_in_list.py

    Description:  Unit testing of not_in_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/not_in_list.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_in_list -> Test item in the list.
        test_not_in_list -> Test item not in the list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "A"
        self.name2 = "D"
        self.base = ["D"]
        self.array_list = ["A", "B", "C"]

    def test_in_list(self):

        """Function:  test_in_list

        Description:  Test item in the list.

        Arguments:

        """

        self.assertEqual(gen_libs.not_in_list(self.name, self.array_list), [])

    def test_not_in_list(self):

        """Function:  test_not_in_list

        Description:  Test item not in the list.

        Arguments:

        """

        self.assertEqual(gen_libs.not_in_list(self.name2, self.array_list),
                         self.base)


if __name__ == "__main__":
    unittest.main()
