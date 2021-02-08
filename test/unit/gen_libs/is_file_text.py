#!/usr/bin/python
# Classification (U)

"""Program:  is_file_text.py

    Description:  Unit testing of is_file_text in gen_libs.py.

    Usage:
        test/unit/gen_libs/is_file_text.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
        test_null_file -> Test with null byte in file.
        test_binary_file -> Test with binary in file.
        test_empty_file -> Test with empty file.
        test_text_file -> Test with text in file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        base_path = "test/unit/gen_libs/testfiles"
        self.file = os.path.join(os.getcwd(), base_path, "is_file_text")
        self.file2 = os.path.join(os.getcwd(), base_path, "is_file_text2")
        self.file3 = os.path.join(os.getcwd(), base_path, "is_file_text3")
        self.file4 = os.path.join(os.getcwd(), base_path, "is_file_text4")

    def test_null_file(self):

        """Function:  test_null_file

        Description:  Test with null byte in file.

        Arguments:

        """

        self.assertFalse(gen_libs.is_file_text(self.file4))

    def test_binary_file(self):

        """Function:  test_binary_file

        Description:  Test with binary in file.

        Arguments:

        """

        self.assertFalse(gen_libs.is_file_text(self.file2))

    def test_empty_file(self):

        """Function:  test_empty_file

        Description:  Test with empty file.

        Arguments:

        """

        self.assertTrue(gen_libs.is_file_text(self.file3))

    def test_text_file(self):

        """Function:  test_text_file

        Description:  Test with text in file.

        Arguments:

        """

        self.assertTrue(gen_libs.is_file_text(self.file))


if __name__ == "__main__":
    unittest.main()
