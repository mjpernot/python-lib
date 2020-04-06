#!/usr/bin/python
# Classification (U)

"""Program:  NotYetImplementedError.py

    Description:  Unit testing of NotYetImplementedError in errors.py.

    Usage:
        test/unit/errors/NotYetImplementedError.py

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
import errors
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_NotYetImplementedError -> Test with no arguments.

    """

    def test_NotYetImplementedError(self):

        """Function:  test_Error

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.NotYetImplementedError())


if __name__ == "__main__":
    unittest.main()
