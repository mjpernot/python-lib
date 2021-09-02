#!/usr/bin/python
# Classification (U)

"""Program:  rm_dup_list.py

    Description:  Unit testing of rm_dup_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/rm_dup_list.py

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
        test_with_multi_dups
        test_with_one_dup2
        test_with_one_dup
        test_with_multi_item
        test_with_one_item
        test_with_empty_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list = []
        self.base = [1, 2, 3, 4]
        self.base2 = [1]
        self.list2 = [1]
        self.list3 = [1, 1]
        self.list4 = [1, 2, 3, 4]
        self.list5 = [1, 2, 3, 4, 1]
        self.list6 = [1, 1, 2, 3, 4, 2]

    def test_with_multi_dups(self):

        """Function:  test_with_multi_dups

        Description:  Test with multiple dupes in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_dup_list(self.list6), self.base)

    def test_with_one_dup2(self):

        """Function:  test_with_one_dup2

        Description:  Test with one dupe in multiple item list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_dup_list(self.list5), self.base)

    def test_with_one_dup(self):

        """Function:  test_with_one_dup

        Description:  Test with one dupe in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_dup_list(self.list3), self.base2)

    def test_with_multi_item(self):

        """Function:  test_with_multi_item

        Description:  Test with multiple items in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_dup_list(self.list4), self.base)

    def test_with_one_item(self):

        """Function:  test_with_one_item

        Description:  Test with single item in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_dup_list(self.list2), self.base2)

    def test_with_empty_list(self):

        """Function:  test_with_empty_list

        Description:  Test with empty list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_dup_list(self.list), [])


if __name__ == "__main__":
    unittest.main()
