#!/usr/bin/python
# Classification (U)

"""Program:  rm_newline_list.py

    Description:  Unit testing of rm_newline_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/rm_newline_list.py

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
        test_with_no_newlines
        test_with_some_newlines
        test_with_all_newlines

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.line = "And the last"
        self.list1 = ["This is test\n", "And another\n", self.line]
        self.list2 = ["This is test\n", "And another\n", "And the last\n"]
        self.list3 = ["This is test", "And another", self.line]
        self.list = ["This is test", "And another", self.line]

    def test_with_no_newlines(self):

        """Function:  test_with_no_newlines

        Description:  Test with no newlines in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_newline_list(self.list3), self.list)

    def test_with_some_newlines(self):

        """Function:  test_with_some_newlines

        Description:  Test with some newlines in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_newline_list(self.list1), self.list)

    def test_with_all_newlines(self):

        """Function:  test_with_all_newlines

        Description:  Test with all newlines in list.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_newline_list(self.list2), self.list)


if __name__ == "__main__":
    unittest.main()
