# Classification (U)

"""Program:  notyetimplementederror.py

    Description:  Unit testing of NotYetImplementedError in errors.py.

    Usage:
        test/unit/errors/notyetimplementederror.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import errors
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_notyetimplementederror

    """

    def test_notyetimplementederror(self):

        """Function:  test_notyetimplementederror

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.NotYetImplementedError())


if __name__ == "__main__":
    unittest.main()
