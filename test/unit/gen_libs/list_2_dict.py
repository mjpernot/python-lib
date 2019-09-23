#!/usr/bin/python
# Classification (U)

"""Program:  list_2_dict.py

    Description:  Unit testing of list_2_dict in gen_libs.py.

    Usage:
        test/unit/gen_libs/list_2_dict.py

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
        test_field_del -> Test with different field delimiter.
        test_multi_keys -> Test with multiple items for same key.
        test_multi_item -> Test with multiple items in list.
        test_one_item -> Test with one item in list.
        test_empty_list -> Test with empty list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.list0 = []
        self.list1 = ["a.1"]
        self.list2 = ["a.1", "b.2"]
        self.list3 = ["a.1", "b.2", "a.3"]
        self.list4 = ["a:1"]
        self.dict0 = {}
        self.dict1 = {"a": ["1"]}
        self.dict2 = {"a": ["1"], "b": ["2"]}
        self.dict3 = {"a": ["1", "3"], "b": ["2"]}

    def test_field_del(self):

        """Function:  test_field_del

        Description:  Test with different field delimiter.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_dict(self.list4, ":"), self.dict1)

    def test_multi_keys(self):

        """Function:  test_multi_keys

        Description:  Test with multiple items for same key.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_dict(self.list3), self.dict3)

    def test_multi_item(self):

        """Function:  test_multi_item

        Description:  Test with multiple items in list.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_dict(self.list2), self.dict2)

    def test_one_item(self):

        """Function:  test_one_item

        Description:  Test with one item in list.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_dict(self.list1), self.dict1)

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test with empty list.

        Arguments:

        """

        self.assertEqual(gen_libs.list_2_dict(self.list0), self.dict0)


if __name__ == "__main__":
    unittest.main()
