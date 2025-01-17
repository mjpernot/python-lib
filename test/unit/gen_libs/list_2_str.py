# Classification (U)

"""Program:  list_2_str.py

    Description:  Unit testing of list_2_str in gen_libs.py.

    Usage:
        test/unit/gen_libs/list_2_str.py

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
        test_mixed_items
        test_field_del
        test_multi_item
        test_one_item
        test_empty_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list0 = []
        self.list1 = ["This"]
        self.list2 = ["This", "is", "a", "test"]
        self.list3 = ["This", "is", 2, "a", "test"]
        self.res0 = ""
        self.res1 = "This"
        self.res2 = "Thisisatest"
        self.res3 = "This is a test"
        self.res4 = "Thisis2atest"

    def test_mixed_items(self):

        """Function:  test_mixed_items

        Description:  Test with mixture of strings and integers.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_str(self.list3), self.res4)

    def test_field_del(self):

        """Function:  test_field_del

        Description:  Test with different field delimiter.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_str(self.list2, " "), self.res3)

    def test_multi_item(self):

        """Function:  test_multi_item

        Description:  Test with multiple items in list.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_str(self.list2), self.res2)

    def test_one_item(self):

        """Function:  test_one_item

        Description:  Test with one item in list.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_str(self.list1), self.res1)

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test with empty list.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_str(self.list0), self.res0)


if __name__ == "__main__":
    unittest.main()
