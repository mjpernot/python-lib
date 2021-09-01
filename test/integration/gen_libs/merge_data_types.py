#!/usr/bin/python
# Classification (U)

"""Program:  merge_data_types.py

    Description:  Unit testing of merge_data_types in gen_libs.py.

    Usage:
        test/integration/gen_libs/merge_data_types.py

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
        test_data1_notequal_data2
        test_data1_equal_data2
        test_merge_string
        test_merge_list
        test_merge_tuple
        test_merge_dict
        test_non_merge

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data_1_i = 1
        self.data_2_i = 2
        self.data_1_s = "Good "
        self.data_2_s = "test"
        self.data_1_d = {"a": 1, "b": 2}
        self.data_2_d = {"c": 3, "d": 4}
        self.data_1_t = (1, 2, 3)
        self.data_2_t = (4, 5, 6)
        self.data_1_l = [1, 2, 3]
        self.data_2_l = [4, 5, 6]

        self.status_f = False
        self.status_t = True
        self.err_msg_1 = "Not string, dictionary, list, or tuple data type"
        self.err_msg_2 = "Inconsistent data types"
        self.err_msg_n = ""

        self.data_s = "Good test"
        self.data_t = (1, 2, 3, 4, 5, 6)
        self.data_l = [1, 2, 3, 4, 5, 6]
        self.data_d = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.data_n = None

    def test_data1_notequal_data2(self):

        """Function:  test_data1_notequal_data2

        Description:  Test with data types not equal.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_i,
                                                   self.data_2_s),
                         (self.data_n, self.status_f, self.err_msg_2))

    def test_data1_equal_data2(self):

        """Function:  test_data1_equal_data2

        Description:  Test with data types equal.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_s,
                                                   self.data_2_s),
                         (self.data_s, self.status_t, self.err_msg_n))

    def test_merge_string(self):

        """Function:  test_merge_string

        Description:  Test with merge of two strings.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_s,
                                                   self.data_2_s),
                         (self.data_s, self.status_t, self.err_msg_n))

    def test_merge_list(self):

        """Function:  test_merge_list

        Description:  Test with merge of two lists.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_l,
                                                   self.data_2_l),
                         (self.data_l, self.status_t, self.err_msg_n))

    def test_merge_tuple(self):

        """Function:  test_merge_tuple

        Description:  Test with merge of two tuples.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_t,
                                                   self.data_2_t),
                         (self.data_t, self.status_t, self.err_msg_n))

    def test_merge_dict(self):

        """Function:  test_merge_dict

        Description:  Test with merge of two dictionaries.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_d,
                                                   self.data_2_d),
                         (self.data_d, self.status_t, self.err_msg_n))

    def test_non_merge(self):

        """Function:  test_non_merge

        Description:  Test with non-mergable data types.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_data_types(self.data_1_i,
                                                   self.data_2_i),
                         (self.data_n, self.status_f, self.err_msg_1))


if __name__ == "__main__":
    unittest.main()
