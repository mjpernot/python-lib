#!/usr/bin/python
# Classification (U)

"""Program:  get_data.py

    Description:  Unit testing of get_data in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_data.py

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


def compare_list_check(f_name):

    """Function Stub:  compare_list_check

    Description:  .

    Arguments:
        (input) f_name
        (output) True|False

    """

    with open(f_name, "r") as f_hdlr:
        base_list = [x.strip() for x in f_hdlr]

    f_hdlr = open(f_name, "r")
    test_list = gen_libs.get_data(f_hdlr)

    return base_list == test_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_compare_lists

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_libs/baseline/get_data_baseline.out")

    def test_compare_lists(self):

        """Function:  test_compare_lists

        Description:  Test with comparing baseline list with test list.

        Arguments:

        """

        self.assertTrue(compare_list_check(self.f_name))


if __name__ == "__main__":
    unittest.main()
