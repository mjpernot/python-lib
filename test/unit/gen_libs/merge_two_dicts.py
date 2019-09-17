#!/usr/bin/python
# Classification (U)

"""Program:  merge_two_dicts.py

    Description:  Unit testing of merge_two_dicts in gen_libs.py.

    Usage:
        test/unit/gen_libs/merge_two_dicts.py

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
        test_instance_nondict -> Test with instance is non-dictionary.
        test_instance_dict -> Test with instance is dictionary.
        test_data1_nondict_data2_nondict -> Test with data1 is non-dictionary
            and data2 is non-dictionary.
        test_data1_dict_data2_nondict -> Test with data1 is dictionary and
            data2 is non-dictionary.
        test_data1_nondict_data2_dict -> Test with data1 is non-dictionary and
            data2 is dictionary.
        test_data1_dict_data2_dict -> Test with data1 is dictionary and data2
            is dictionary.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data_1 = {"a": 1, "b": 2}
        self.data_2 = {"c": 3, "d": 4}
        self.data_1n = "String"
        self.data_2n = [1, 2]
        self.status_f = False
        self.status_t = True
        self.err_msg = "One item isn't a dictionary or inconsistent data types"
        self.err_msg_n = ""
        self.data_r = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.data_n = None

    def test_instance_nondict(self):

        """Function:  test_instance_nondict

        Description:  Test merge_two_dicts function with instance is
            non-dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_two_dicts(self.data_1n, self.data_2n),
                         (self.data_n, self.status_f, self.err_msg))

    def test_instance_dict(self):

        """Function:  test_instance_dict

        Description:  Test merge_two_dicts function with instance is
            dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_two_dicts(self.data_1, self.data_2n),
                         (self.data_n, self.status_f, self.err_msg))

    def test_data1_nondict_data2_nondict(self):

        """Function:  test_data1_nondict_data2_nondict

        Description:  Test merge_two_dicts function with data1 is
            non-dictionary and data2 is non-dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_two_dicts(self.data_1n, self.data_2n),
                         (self.data_n, self.status_f, self.err_msg))

    def test_data1_dict_data2_nondict(self):

        """Function:  test_data1_dict_data2_nondict

        Description:  Test merge_two_dicts function with data1 is dictionary
            and data2 is non-dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_two_dicts(self.data_1, self.data_2n),
                         (self.data_n, self.status_f, self.err_msg))

    def test_data1_nondict_data2_dict(self):

        """Function:  test_data1_nondict_data2_dict

        Description:  Test merge_two_dicts function with data1 is
            non-dictionary and data2 is dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_two_dicts(self.data_1n, self.data_2),
                         (self.data_n, self.status_f, self.err_msg))

    def test_data1_dict_data2_dict(self):

        """Function:  test_data1_dict_data2_dict

        Description:  Test merge_two_dicts function with data1 is dictionary
            and data2 is dictionary.

        Arguments:

        """

        self.assertEqual(gen_libs.merge_two_dicts(self.data_1, self.data_2),
                         (self.data_r, self.status_t, self.err_msg_n))


if __name__ == "__main__":
    unittest.main()
