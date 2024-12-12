# Classification (U)

"""Program:  notslaveerror.py

    Description:  Unit testing of NotSlaveError in errors.py.

    Usage:
        test/unit/errors/notslaveerror.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import errors                       # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_notslaveerror

    """

    def test_notslaveerror(self):

        """Function:  test_notslaveerror

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.NotSlaveError())


if __name__ == "__main__":
    unittest.main()
