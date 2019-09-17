#!/usr/bin/python
# Classification (U)

"""Program:  dict_2_list.py

    Description:  Unit testing of dict_2_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/dict_2_list.py

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
        test_key_not_in_list -> Test with key value not in dictionary.
        test_key_in_list -> Test with key value in dictionary.
        test_empty_dict -> Test with empty dictionary.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dict_list = {}
        self.dict_list2 = [{"a": 1, "b": 2}, {"d": 1, "a": 2}]
        self.key_val1 = "a"
        self.key_val2 = "c"
        self.list = []
        self.list2 = [1, 2]

    @unittest.skip("Known bug: see #591")
    def test_key_not_in_list(self):

        """Function:  test_key_not_in_list

        Description:  Test with key value not in dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.dict_2_list(self.dict_list2, self.key_val2),
                         self.list)

    def test_key_in_list(self):

        """Function:  test_key_in_list

        Description:  Test with key value in dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.dict_2_list(self.dict_list2, self.key_val1),
                         self.list2)

    def test_empty_dict(self):

        """Function:  test_empty_dict

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.dict_2_list(self.dict_list, self.key_val1),
                         self.list)


if __name__ == "__main__":
    unittest.main()
