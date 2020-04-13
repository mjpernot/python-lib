#!/usr/bin/python
# Classification (U)

"""Program:  SlaveNotRunningError.py

    Description:  Unit testing of SlaveNotRunningError in errors.py.

    Usage:
        test/unit/errors/SlaveNotRunningError.py

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
        test_SlaveNotRunningError -> Test with no arguments.

    """

    def test_SlaveNotRunningError(self):

        """Function:  SlaveNotRunningError

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.SlaveNotRunningError())


if __name__ == "__main__":
    unittest.main()