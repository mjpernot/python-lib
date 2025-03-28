# Classification (U)

"""Program:  no_std_out.py

    Description:  Unit testing of no_std_out in gen_libs.py.

    Usage:
        test/unit/gen_libs/no_std_out.py

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


def test_no_print_out():

    """Function:  test_no_print_out

    Description:  Used as stub test function for test_no_std_out function..

    Arguments:

    """

    print("This line should not print if successful")
    return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_get_base_dir

    """

    def test_no_std_out(self):

        """Function:  test_no_std_out

        Description:  Test no_std_out function.

        Arguments:

        """

        with gen_libs.no_std_out():
            status = test_no_print_out()

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
