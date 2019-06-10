#!/usr/bin/python
# Classification (U)

"""Program:  list_files.py

    Description:  Unit testing of list_files in gen_libs.py.

    Usage:
        test/unit/gen_libs/list_files.py

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
import mock

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_list_files -> Test list_files function.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir_path = "test/unit/gen_libs/tmp"

        self.fname1 = os.path.join(self.dir_path, "file.py")
        self.fname2 = os.path.join(self.dir_path, "file.txt")
        self.dname = os.path.join(self.dir_path, "dir1")

        with open(self.fname1, "a"):
            os.utime(self.fname1, None)

        with open(self.fname2, "a"):
            os.utime(self.fname2, None)

        os.makedirs(self.dname)

        self.results1 = ["file.txt", "file.py"]
        self.results2 = ["file.py", "file.txt"]

    def test_list_files(self):

        """Function:  test_list_files

        Description:  Test list_files function.

        Arguments:

        """

        file_list = gen_libs.list_files(self.dir_path)

        if file_list == self.results1 or file_list == self.results2:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.fname1)
        os.remove(self.fname2)
        os.rmdir(self.dname)


if __name__ == "__main__":
    unittest.main()
