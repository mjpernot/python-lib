# Classification (U)

"""Program:  nooptionerror.py

    Description:  Unit testing of NoOptionError in errors.py.

    Usage:
        test/unit/errors/nooptionerror.py

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
        test_nooptionerror

    """

    def test_nooptionerror(self):

        """Function:  test_nooptionerror

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.NoOptionError())


if __name__ == "__main__":
    unittest.main()
