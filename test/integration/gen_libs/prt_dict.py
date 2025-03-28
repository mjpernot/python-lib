# Classification (U)

"""Program:  prt_dict.py

    Description:  Integration testing of prt_dict in gen_libs.py.

    Usage:
        test/integration/gen_libs/prt_dict.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import filecmp

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
        test_indent_multi_lvl
        test_indent_multi_dict
        test_indent2
        test_indent
        test_multi_lvl
        test_multi_dict
        test_one_item
        test_empty_dict
        tearDown

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
        self.indent = 0
        self.indent2 = 4
        self.ofile = "test/integration/gen_libs/tmp/test_prt_dict.txt"
        self.basefile = "test/integration/gen_libs/basefiles/prt_dict.txt"
        self.basefile2 = "test/integration/gen_libs/basefiles/prt_dict2.txt"
        self.basefile23 = "test/integration/gen_libs/basefiles/prt_dict2-3.txt"
        self.basefile3 = "test/integration/gen_libs/basefiles/prt_dict3.txt"
        self.basefile4 = "test/integration/gen_libs/basefiles/prt_dict4.txt"
        self.basefile5 = "test/integration/gen_libs/basefiles/prt_dict5.txt"
        self.basefile53 = "test/integration/gen_libs/basefiles/prt_dict5-3.txt"
        self.basefile6 = "test/integration/gen_libs/basefiles/prt_dict6.txt"
        self.fname = open(                          # pylint:disable=R1732
            self.ofile, "w", encoding="UTF-8")

    def test_indent_multi_lvl(self):

        """Function:  test_indent_multi_lvl

        Description:  Test multi level with indentation.

        Arguments:

        """

        gen_libs.prt_dict(self.data4, self.fname, indent=self.indent2)
        self.fname.close()

        self.assertTrue(filecmp.cmp(self.basefile6, self.ofile))

    def test_indent_multi_dict(self):

        """Function:  test_indent_multi_dict

        Description:  Test multi dict with indentation.

        Arguments:

        """

        gen_libs.prt_dict(self.data3, self.fname, indent=self.indent2)
        self.fname.close()

        if sys.version_info < (3, 0):
            self.assertTrue(filecmp.cmp(self.basefile5, self.ofile))

        else:
            self.assertTrue(filecmp.cmp(self.basefile53, self.ofile))

    def test_indent2(self):

        """Function:  test_indent2

        Description:  Test with passing indentation setting.

        Arguments:

        """

        gen_libs.prt_dict(self.data2, self.fname, indent=self.indent2)
        self.fname.close()

        self.assertTrue(filecmp.cmp(self.basefile4, self.ofile))

    def test_indent(self):

        """Function:  test_indent

        Description:  Test with passing indentation setting.

        Arguments:

        """

        gen_libs.prt_dict(self.data2, self.fname, indent=self.indent)
        self.fname.close()

        self.assertTrue(filecmp.cmp(self.basefile, self.ofile))

    def test_multi_lvl(self):

        """Function:  test_multi_lvl

        Description:  Test with multiple level dictionary.

        Arguments:

        """

        gen_libs.prt_dict(self.data4, self.fname)
        self.fname.close()

        self.assertTrue(filecmp.cmp(self.basefile3, self.ofile))

    def test_multi_dict(self):

        """Function:  test_multi_dict

        Description:  Test with multiple items in dictionary.

        Arguments:

        """

        gen_libs.prt_dict(self.data3, self.fname)
        self.fname.close()

        if sys.version_info < (3, 0):
            self.assertTrue(filecmp.cmp(self.basefile2, self.ofile))

        else:
            self.assertTrue(filecmp.cmp(self.basefile23, self.ofile))

    def test_one_item(self):

        """Function:  test_one_item

        Description:  Test with one item in dictionary.

        Arguments:

        """

        self.assertFalse(gen_libs.prt_dict(self.data2, self.fname))
        self.fname.close()

        self.assertTrue(filecmp.cmp(self.basefile, self.ofile))

    def test_empty_dict(self):

        """Function:  test_empty_dict

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.fname.close()

        self.assertFalse(gen_libs.prt_dict(self.data))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
