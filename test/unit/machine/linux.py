# Classification (U)

"""Program:  linux.py

    Description:  Unit testing of Linux in machine.py.

    Usage:
        test/unit/machine/linux.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_linux

    """

    def test_linux(self):

        """Function:  test_linux

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(machine.Linux())


if __name__ == "__main__":
    unittest.main()
