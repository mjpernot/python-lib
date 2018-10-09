#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      clear_file.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_libs        => v1.32.0 or higher
#
###############################################################################

"""Program:  clear_file.py

    Description:  Unit testing of clear_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/clear_file.py

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

# Version Information
__version__ = version.__version__


def clear_file_check(f_name):

    """Function:  clear_file_check

    Description:  Checks to see if a file was cleared of data.

    Arguments:
        (input) f_name -> Test file name to check.
        (output) True|False -> Comparsion results of file check.

    """

    gen_libs.clear_file(f_name)

    if os.stat(f_name).st_size == 0:
        return True

    else:
        return False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_clear_file -> Test with clearing an existing file that has data.
        tearDown -> Cleanup of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_libs/tmp/clear_file_test.out")

        gen_libs.write_file(self.f_name, "w", "TEST")

    def test_clear_file(self):

        """Function:  test_clear_file

        Description:  Test with clearing an existing file that has data.

        Arguments:
            None

        """

        self.assertTrue(clear_file_check(self.f_name))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:
            None

        """

        os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()