#!/usr/bin/python
# Classification (U)

"""Program:  del_not_in_list.py

    Description:  Unit testing of del_not_in_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/del_not_in_list.py

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
        setUp
        test_with_all_present
        test_with_two_items
        test_with_one_item
        test_with_list2_empty
        test_with_list1_empty
        test_with_empty_lists

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    def test_with_all_present(self):

        """Function:  test_with_all_present

        Description:  Test with all items present.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_in_list([1, 2, 3], [1, 2, 3, 4]),
                         [1, 2, 3])

    def test_with_two_items(self):

        """Function:  test_with_two_items

        Description:  Test with two items removed.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_in_list([1, 2, 3], [2, 4]), [2])

    def test_with_one_item(self):

        """Function:  test_with_one_item

        Description:  Test with one item removed.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_in_list([1, 2, 3], [1, 3, 4]),
                         [1, 3])

    def test_with_list2_empty(self):

        """Function:  test_with_list2_empty

        Description:  Test with list2 empty.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_in_list([1, 2, 3], []), [])

    def test_with_list1_empty(self):

        """Function:  test_with_list1_empty

        Description:  Test with list1 empty.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_in_list([], [1]), [])

    def test_with_empty_lists(self):

        """Function:  test_with_empty_lists

        Description:  Test with both lists empty.

        Arguments:

        """

        self.assertEqual(gen_libs.del_not_in_list([], []), [])


if __name__ == "__main__":
    unittest.main()
