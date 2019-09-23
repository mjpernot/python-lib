#!/usr/bin/python
# Classification (U)

"""Program:  del_not_and_list.py

    Description:  Unit testing of del_not_and_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/del_not_and_list.py

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
        test_with_all_present -> Test with all items present.
        test_with_two_items -> Test with two items removed.
        test_with_one_item -> Test with one item removed.
        test_with_list2_empty -> Test with list2 empty.
        test_with_list1_empty -> Test with list1 empty.
        test_with_empty_lists -> Test with both lists empty.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list10 = []
        self.list11 = [1, 2, 3, 4]
        self.list20 = []
        self.list21 = [1, 2, 3, 4]
        self.list22 = [2]
        self.list23 = [2, 4]
        self.result0 = []
        self.result1 = [1, 3, 4]
        self.result2 = [1, 3]
        self.result3 = [1, 2, 3, 4]

    def test_with_all_present(self):

        """Function:  test_with_all_present

        Description:  Test with all items present.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_and_list(self.list11, self.list21),
                         self.result0)

    def test_with_two_items(self):

        """Function:  test_with_two_items

        Description:  Test with two items removed.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_and_list(self.list11, self.list23),
                         self.result2)

    def test_with_one_item(self):

        """Function:  test_with_one_item

        Description:  Test with one item removed.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_and_list(self.list11, self.list22),
                         self.result1)

    def test_with_list2_empty(self):

        """Function:  test_with_list2_empty

        Description:  Test with list2 empty.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_and_list(self.list11, self.list20),
                         self.result3)

    def test_with_list1_empty(self):

        """Function:  test_with_list1_empty

        Description:  Test with list1 empty.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_and_list(self.list10, self.list21),
                         self.result0)

    def test_with_empty_lists(self):

        """Function:  test_with_empty_lists

        Description:  Test with both lists empty.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_and_list(self.list10, self.list20),
                         self.result0)


if __name__ == "__main__":
    unittest.main()
