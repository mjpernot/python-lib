#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      no_std_out.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_libs        => v1.31.0 or higher
#
###############################################################################

"""Program:  no_std_out.py

    Description:  Unit testing of no_std_out in gen_libs.py.

    Usage:
        test/unit/gen_libs/no_std_out.py

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


def test_no_print_out():

    """Function:  test_no_print_out

    Description:  Used as stub test function for test_no_std_out function..

    Arguments:
        None

    """

    print("This line should not print if successful")
    return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        test_get_base_dir -> Test no_std_out function.

    """

    def test_no_std_out(self):

        """Function:  test_no_std_out

        Description:  Test no_std_out function.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            status = test_no_print_out()

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
