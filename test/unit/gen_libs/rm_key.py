#!/usr/bin/python
# Classification (U)

"""Program:  rm_key.py

    Description:  Unit testing of rm_key in gen_libs.py.

    Usage:
        test/unit/gen_libs/rm_key.py

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
        test_one_entry
        test_empty_dict
        test_rm_miss_key
        test_rm_no_key
        test_rm_key

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {}
        self.data2 = {"data_key1": "val1"}
        self.data3 = {"data_key1": "val1", "data_key2": "val2"}
        self.key = ""
        self.key2 = "data_key2"
        self.key3 = "data_key3"
        self.key4 = "data_key1"
        self.results = {}
        self.results2 = {"data_key1": "val1"}
        self.results3 = {"data_key1": "val1", "data_key2": "val2"}

    def test_one_entry(self):

        """Function:  test_one_entry

        Description:  Test with one entry in dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_key(self.data2, self.key4),
                         self.results)

    def test_empty_dict(self):

        """Function:  test_empty_dict

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_key(self.data, self.key2),
                         self.results)

    def test_rm_miss_key(self):

        """Function:  test_rm_miss_key

        Description:  Test with missing data_key to remove.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_key(self.data3, self.key3),
                         self.results3)

    def test_rm_no_key(self):

        """Function:  test_rm_no_key

        Description:  Test with no key to remove.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_key(self.data3, self.key),
                         self.results3)

    def test_rm_key(self):

        """Function:  test_rm_key

        Description:  Test removing one data_key.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_key(self.data3, self.key2),
                         self.results2)


if __name__ == "__main__":
    unittest.main()
