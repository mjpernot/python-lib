#!/usr/bin/python
# Classification (U)

"""Program:  notmastererror.py

    Description:  Unit testing of NotMasterError in errors.py.

    Usage:
        test/unit/errors/notmastererror.py

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
        test_notmastererror

    """

    def test_notmastererror(self):

        """Function:  test_notmastererror

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(errors.NotMasterError())


if __name__ == "__main__":
    unittest.main()
