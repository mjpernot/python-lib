#!/usr/bin/python
# Classification (U)

"""Program:  write_file.py

    Description:  Unit testing of write_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/write_file.py

    Arguments:
        None

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

# Version
__version__ = version.__version__


def create_file(f_name, mode):

    """Function:  create_file

    Description:  Used as stub test function for test_create_file function..

    Arguments:
        (input) f_name -> Name of file
        (input) mode w|a -> Write or append to file.
        (output) True|False -> Creation of file was successful.

    """

    gen_libs.write_file(f_name, mode, "TEST")

    if os.path.isfile(f_name):
        return True

    else:
        return False


def write_file(f_name, mode):

    """Function:  write_file

    Description:  Used as stub test function for test_write_file function..

    Arguments:
        (input) f_name -> Name of file
        (input) mode w|a -> Write or append to file.
        (output) True|False -> Writing to a file was successful.

    """

    gen_libs.write_file(f_name, mode, "TEST")

    if os.path.isfile(f_name):

        if "TEST" in open(f_name).read():
            return True

        else:
            return False

    else:
        return False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_create_file -> Test creating file.
        test_write_file -> Test writing to file.
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.f_path = os.path.join(os.getcwd(),
                                   "test/unit/gen_libs/tmp/w_file.txt")

    def test_create_file(self):

        """Function:  test_create_file

        Description:  Test creating file.

        Arguments:
            None

        """

        self.assertTrue(create_file(self.f_path, "w"))

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test writing to a file.

        Arguments:
            None

        """

        self.assertTrue(write_file(self.f_path, "w"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:
            None

        """

        os.remove(self.f_path)


if __name__ == "__main__":
    unittest.main()
