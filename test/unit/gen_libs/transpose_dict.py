# Classification (U)

"""Program:  transpose_dict.py

    Description:  Unit testing of transpose_dict in gen_libs.py.

    Usage:
        test/unit/gen_libs/transpose_dict.py

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
        test_int_bool_list
        test_multiple_bool_list
        test_bool_list
        test_multiple_lists
        test_single_list
        test_no_matches2
        test_no_matches
        test_empty_data
        test_multiple_bools2
        test_multiple_bools
        test_multiple_ints
        test_multiple_nones
        test_single_bool_no_key
        test_single_bool2
        test_single_bool
        test_single_int_no_key
        test_single_int
        test_single_str_no_key
        test_single_empty
        test_single_none

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        p_list = '["item1", "item2"]'

        self.data = [{}]
        self.data2 = [{"a": "None"}]
        self.data3 = [{"a": ""}]
        self.data4 = [{"a": "1"}]
        self.data5 = [{"a": "True"}]
        self.data5a = [{"a": "False"}]
        self.data6 = [{"a": "None"}, {"a": ""}]
        self.data7 = [{"a": "1"}, {"a": "1"}]
        self.data8 = [{"a": "True"}, {"a": "True"}]
        self.data8a = [{"a": "False"}, {"a": "False"}]
        self.data9 = [{"a": p_list}]
        self.data10 = [{"a": p_list}, {"a": '["item3", "item4"]'}]
        self.data11 = [{"a": "True", "b": p_list}]
        self.data12 = [{"a": "True", "b": p_list},
                       {"a": "False", "b": '["item3", "item4"]'}]
        self.data13 = [{"a": "True", "b": p_list, "c": "12"}]

        self.data_key = {}
        self.data_key2 = {"a": "None"}
        self.data_key3 = {"a": "int"}
        self.data_key4 = {"a": "bool"}
        self.data_key5 = {"b": "None"}
        self.data_key6 = {"a": "list"}
        self.data_key7 = {"a": "bool", "b": "list"}
        self.data_key8 = {"a": "bool", "b": "list", "c": "int"}

        self.results = [{"a": "None"}]
        self.results2 = [{"a": None}]
        self.results3 = [{"a": 1}]
        self.results4 = [{"a": "1"}]
        self.results5 = [{"a": True}]
        self.results5a = [{"a": False}]
        self.results6 = [{"a": "True"}]
        self.results7 = [{"a": None}, {"a": None}]
        self.results8 = [{"a": 1}, {"a": 1}]
        self.results9 = [{"a": True}, {"a": True}]
        self.results9a = [{"a": False}, {"a": False}]
        self.results10 = [{"a": ["item1", "item2"]}]
        self.results11 = [{"a": ["item1", "item2"]}, {"a": ["item3", "item4"]}]
        self.results12 = [{"a": True, "b": ["item1", "item2"]}]
        self.results13 = [{"a": True, "b": ["item1", "item2"]},
                          {"a": False, "b": ["item3", "item4"]}]
        self.results14 = [{"a": True, "b": ["item1", "item2"], "c": 12}]

    def test_int_bool_list(self):

        """Function:  test_int_bool_list

        Description:  Test with a boolean and list entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data13, self.data_key8), self.results14)

    def test_multiple_bool_list(self):

        """Function:  test_multiple_bool_list

        Description:  Test with multiple boolean and list entries.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data12, self.data_key7), self.results13)

    def test_bool_list(self):

        """Function:  test_bool_list

        Description:  Test with a boolean and list entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data11, self.data_key7), self.results12)

    def test_multiple_lists(self):

        """Function:  test_multiple_lists

        Description:  Test with a multiple list entries.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data10, self.data_key6), self.results11)

    def test_single_list(self):

        """Function:  test_single_list

        Description:  Test with a single list entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data9, self.data_key6), self.results10)

    def test_no_matches2(self):

        """Function:  test_no_matches2

        Description:  Test with no intersect matches.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data7, self.data_key5), self.data7)

    def test_no_matches(self):

        """Function:  test_no_matches

        Description:  Test with no intersect matches.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data2, self.data_key5), self.results)

    def test_empty_data(self):

        """Function:  test_empty_data

        Description:  Test with an empty data list.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data, self.data_key2), self.data)

    def test_multiple_bools2(self):

        """Function:  test_multiple_bools2

        Description:  Test with a multiple boolean entries.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data8a, self.data_key4), self.results9a)

    def test_multiple_bools(self):

        """Function:  test_multiple_bools

        Description:  Test with a multiple boolean entries.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data8, self.data_key4), self.results9)

    def test_multiple_ints(self):

        """Function:  test_multiple_ints

        Description:  Test with a multiple integer entries.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data7, self.data_key3), self.results8)

    def test_multiple_nones(self):

        """Function:  test_multiple_nones

        Description:  Test with a multiple none entries.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data6, self.data_key2), self.results7)

    def test_single_bool_no_key(self):

        """Function:  test_single_bool_no_key

        Description:  Test with an empty data key for boolean.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data5, self.data_key), self.results6)

    def test_single_bool2(self):

        """Function:  test_single_bool2

        Description:  Test with a single boolean entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data5a, self.data_key4), self.results5a)

    def test_single_bool(self):

        """Function:  test_single_bool

        Description:  Test with a single boolean entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data5, self.data_key4), self.results5)

    def test_single_int_no_key(self):

        """Function:  test_single_int_no_key

        Description:  Test with an empty data key for integer.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data4, self.data_key), self.results4)

    def test_single_int(self):

        """Function:  test_single_int

        Description:  Test with a single integer entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data4, self.data_key3), self.results3)

    def test_single_str_no_key(self):

        """Function:  test_single_str_no_key

        Description:  Test with an empty data key for string.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data2, self.data_key), self.results)

    def test_single_empty(self):

        """Function:  test_single_empty

        Description:  Test with a single empty entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data3, self.data_key2), self.results2)

    def test_single_none(self):

        """Function:  test_single_none

        Description:  Test with a single none entry.

        Arguments:

        """

        self.assertEqual(
            gen_libs.transpose_dict(
                self.data2, self.data_key2), self.results2)


if __name__ == "__main__":
    unittest.main()
