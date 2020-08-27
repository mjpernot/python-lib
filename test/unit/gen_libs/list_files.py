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
        test_list_files -> Test list_files function.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.filep = "file.py"
        self.filet = "file.txt"
        self.dir_path = "test/unit/gen_libs/tmp/tmp"
        os.makedirs(self.dir_path)
        self.fname1 = os.path.join(self.dir_path, self.filep)
        self.fname2 = os.path.join(self.dir_path, self.filet)
        self.dname = os.path.join(self.dir_path, "dir1")

        with open(self.fname1, "a"):
            os.utime(self.fname1, None)

        with open(self.fname2, "a"):
            os.utime(self.fname2, None)

        os.makedirs(self.dname)

        self.results1 = [self.filet, self.filep]
        self.results2 = [self.filep, self.filet]

    def test_list_files(self):

        """Function:  test_list_files

        Description:  Test list_files function.

        Arguments:

        """

        file_list = gen_libs.list_files(self.dir_path)

        self.assertTrue(
            file_list == self.results1 or file_list == self.results2)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.fname1)
        os.remove(self.fname2)
        os.rmdir(self.dname)
        os.rmdir(self.dir_path)


if __name__ == "__main__":
    unittest.main()
