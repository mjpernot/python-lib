#!/usr/bin/python
# Classification (U)

"""Program:  solaris.py

    Description:  Unit testing of Solaris in machine.py.

    Usage:
        test/unit/machine/solaris.py

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
import machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_solaris

    """

    def test_solaris(self):

        """Function:  test_solaris

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(machine.Solaris())


if __name__ == "__main__":
    unittest.main()
