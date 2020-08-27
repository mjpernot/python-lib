#!/usr/bin/python
# Classification (U)

"""Program:  rm_file.py

    Description:  Unit testing of rm_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/rm_file.py

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
        test_with_rm_file -> Test with removing file.
        test_with_raise_exception -> Test raising exception.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = "test/unit/gen_libs/tmp/test_rm_file.txt"
        self.err_msg = "Error: test/unit/gen_libs/tmp/test_rm_file.txt" \
                       + " - No such file or directory"

    def test_with_rm_file(self):

        """Function:  test_with_rm_file

        Description:  Test with removing file.

        Arguments:

        """

        with open(self.f_name, "a"):
            os.utime(self.f_name, None)

        self.assertEqual(gen_libs.rm_file(self.f_name), (False, None))

    def test_with_raise_exception(self):

        """Function:  test_with_raise_exception

        Description:  Test raising exception.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_file(self.f_name), (True, self.err_msg))


if __name__ == "__main__":
    unittest.main()
