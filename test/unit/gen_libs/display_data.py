# Classification (U)

"""Program:  display_data.py

    Description:  Unit testing of display_data in gen_libs.py.

    Usage:
        test/unit/gen_libs/display_data.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import filecmp
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


def display_data_check(b_name, f_name, data, level=0):

    """Function Stub:  display_data_check

    Description:  Front-end function to gen_libs.display_data to create and
        check test data files to baseline data files.

    Arguments:
        (input) b_name
        (input) f_name
        (input) data
        (input) level
        (output) True|False

    """

    with open(f_name, "w", encoding="UTF-8") as f_hdlr:
        gen_libs.display_data(data, level, f_hdlr)

    return filecmp.cmp(b_name, f_name)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_non_dict
        test_only_list
        test_empty_list
        test_only_dict
        test_dict_list
        test_dict_dict
        test_level_is_one
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        #######################################################################
        # WARNING:  If any of the self.data{N} data structures are changed,
        #   then a new associated data baseline file needs to be created for
        #   the new data structure.
        self.data1 = "Test String"
        self.b_name1 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base1.out")

        self.data2 = [1]
        self.b_name2 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base2.out")

        self.data3 = []
        self.b_name3 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base3.out")

        self.data4 = {"A": 1}
        self.b_name4 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base4.out")

        self.data5 = {"A": 1, "B": ["a", "b"], "C": 3}
        self.b_name5 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base5.out")
        self.b_name5_3 = os.path.join(
            os.getcwd(),
            "test/unit/gen_libs/baseline/display_data_base5_3.out")

        self.data6 = {
            "A": 1, "B": ["a", "b"], "C": 3, "D": {"a": "i", "b": "ii"}}
        self.b_name6 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base6.out")
        self.b_name6_3 = os.path.join(
            os.getcwd(),
            "test/unit/gen_libs/baseline/display_data_base6_3.out")

        self.data7 = {
            "A": 1, "B": ["a", "b"], "C": 3, "D": {"a": "i", "b": "ii"}}
        self.b_name7 = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/display_data_base7.out")
        self.b_name7_3 = os.path.join(
            os.getcwd(),
            "test/unit/gen_libs/baseline/display_data_base7_3.out")

        #######################################################################

        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_libs/tmp/test_display_data.txt")

    def test_non_dict(self):

        """Function:  test_non_dict

        Description:  Test with non-dictionary structure.

        Arguments:

        """

        self.assertTrue(
            display_data_check(self.b_name1, self.f_name, self.data1, level=0))

    def test_only_list(self):

        """Function:  test_only_list

        Description:  Test with only a list structure.

        Arguments:


        """

        self.assertTrue(
            display_data_check(self.b_name2, self.f_name, self.data2, level=0))

    def test_empty_list(self):

        """Function:  test_empty_list

        Description:  Test with an empty list structure.

        Arguments:

        """

        self.assertTrue(
            display_data_check(self.b_name3, self.f_name, self.data3, level=0))

    def test_only_dict(self):

        """Function:  test_only_list

        Description:  Test with only a dictionary structure.

        Arguments:

        """

        self.assertTrue(
            display_data_check(self.b_name4, self.f_name, self.data4, level=0))

    def test_dict_list(self):

        """Function:  test_dict_list

        Description:  Test with a list within a dictionary structure.

        Arguments:

        """

        if sys.version_info < (3, 0):
            b_name = self.b_name5

        else:
            b_name = self.b_name5_3

        self.assertTrue(
            display_data_check(b_name, self.f_name, self.data5, level=0))

    def test_dict_dict(self):

        """Function:  test_dict_dict

        Description:  Test with a dictionary within a dictionary structure.

        Arguments:

        """

        if sys.version_info < (3, 0):
            b_name = self.b_name6

        else:
            b_name = self.b_name6_3

        self.assertTrue(
            display_data_check(b_name, self.f_name, self.data6, level=0))

    def test_level_is_one(self):

        """Function:  test_level_is_one

        Description:  Test with a level setting of one.

        Arguments:

        """

        if sys.version_info < (3, 0):
            b_name = self.b_name7

        else:
            b_name = self.b_name7_3

        self.assertTrue(
            display_data_check(b_name, self.f_name, self.data7, level=1))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()
