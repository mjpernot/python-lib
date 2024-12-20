# Classification (U)

"""Program:  file_search_cnt.py

    Description:  Unit testing of file_search_cnt in gen_libs.py.

    Usage:
        test/unit/gen_libs/file_search_cnt.py

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
        test_file_search_cnt
        test_file_search_cnt2
        test_file_search_cnt3
        test_file_search_cnt4
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = "test/unit/gen_libs/tmp/file_search_cnt_test.txt"
        self.f_name2 = "test/unit/gen_libs/tmp/file_search_cnt_test2.txt"
        self.pattern = "quack"
        with open(self.f_name, "w", encoding="UTF-8") as f_hdlr:
            print("This is a test file", file=f_hdlr)
            print("This is a quick brown fox file", file=f_hdlr)
        open(                                           # pylint:disable=R1732
            self.f_name2, "w", encoding="UTF-8").close()

    def test_file_search_cnt(self):

        """Function:  test_file_search_cnt

        Description:  Test file_search_cnt function with 0 pattern found.

        Arguments:

        """

        self.assertEqual(
            gen_libs.file_search_cnt(self.f_name, self.pattern), 0)

    def test_file_search_cnt2(self):

        """Function:  test_file_search_cnt2

        Description:  Test file_search_cnt function with 1 pattern found.

        Arguments:

        """

        self.pattern = "test"
        self.assertEqual(
            gen_libs.file_search_cnt(self.f_name, self.pattern), 1)

    def test_file_search_cnt3(self):

        """Function:  test_file_search_cnt3

        Description:  Test file_search_cnt function with 2 pattern found.

        Arguments:

        """

        self.pattern = "file"
        self.assertEqual(
            gen_libs.file_search_cnt(self.f_name, self.pattern), 2)

    def test_file_search_cnt4(self):

        """Function:  test_file_search_cnt4

        Description:  Test file_search_cnt function with an empty file.

        Arguments:

        """

        self.assertEqual(
            gen_libs.file_search_cnt(self.f_name2, self.pattern), 0)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)
        os.remove(self.f_name2)


if __name__ == "__main__":
    unittest.main()
