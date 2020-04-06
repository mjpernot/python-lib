#!/usr/bin/python
# Classification (U)

"""Program:  NotMasterError.py

    Description:  Unit testing of NotMasterError in errors.py.

    Usage:
        test/unit/errors/NotMasterError.py

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
        test_NotMasterError -> Test with no arguments.

    """

    def test_NotMasterError(self):

        """Function:  NotMasterError

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.NotMasterError())


if __name__ == "__main__":
    unittest.main()
