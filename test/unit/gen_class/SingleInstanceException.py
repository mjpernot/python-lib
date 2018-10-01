#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      SingleInstanceException.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_class       => 1.33.0 or higher
#
###############################################################################

"""Program:  SingleInstanceException.py

    Description:  Unit testing of SingleInstanceException in gen_class.py.

    Usage:
        test/unit/gen_class/SingleInstanceException.py

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
import gen_class
import version

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        test_SingleInstanceException -> Test with no arguments.

    """

    def test_SingleInstanceException(self):

        """Function:  test_SingleInstanceException

        Description:  Test with no arguments.

        Arguments:
            None

        """

        self.assertTrue(gen_class.SingleInstanceException())


if __name__ == "__main__":
    unittest.main()
