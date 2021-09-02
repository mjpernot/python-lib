#!/usr/bin/python
# Classification (U)

"""Program:  prt_dict.py

    Description:  Unit testing of prt_dict in gen_libs.py.

    Usage:
        test/unit/gen_libs/prt_dict.py

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
        test_indent_multi_lvl
        test_indent_multi_dict
        test_indent2
        test_indent
        test_multi_lvl
        test_multi_dict
        test_one_item
        test_empty_dict

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {}
        self.data2 = {"key1": "value1"}
        self.data3 = {"key1": "value1", "key2": "value2"}
        self.data4 = {"key1": {"key2": "value2"}}
        self.f_hldr = open("/dev/null", "w")
        self.indent = 0
        self.indent2 = 1

    def test_indent_multi_lvl(self):

        """Function:  test_indent_multi_lvl

        Description:  Test multi level with indentation.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data4, self.f_hldr,
                                               indent=self.indent2))

    def test_indent_multi_dict(self):

        """Function:  test_indent_multi_dict

        Description:  Test multi dict with indentation.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data3, self.f_hldr,
                                               indent=self.indent2))

    def test_indent2(self):

        """Function:  test_indent2

        Description:  Test with passing indentation setting.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data2, self.f_hldr,
                                               indent=self.indent2))

    def test_indent(self):

        """Function:  test_indent

        Description:  Test with passing indentation setting.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data2, self.f_hldr,
                                               indent=self.indent))

    def test_multi_lvl(self):

        """Function:  test_multi_lvl

        Description:  Test with multiple level dictionary.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data4, self.f_hldr))

    def test_multi_dict(self):

        """Function:  test_multi_dict

        Description:  Test with multiple items in dictionary.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data3, self.f_hldr))

    def test_one_item(self):

        """Function:  test_one_item

        Description:  Test with one item in dictionary.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_dict(self.data2, self.f_hldr))

    def test_empty_dict(self):

        """Function:  test_empty_dict

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.assertFalse(gen_libs.prt_dict(self.data))


if __name__ == "__main__":
    unittest.main()
