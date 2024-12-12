# Classification (U)

"""Program:  amachine.py

    Description:  Unit testing of Machine in machine.py.

    Note: The file is called amachine.py instead of machine.py, this is due to
        the fact if it is called machine.py then the other unit test files
        try use this file as the import.

    Usage:
        test/unit/machine/amachine.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import machine                      # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_machine

    """

    def test_machine(self):

        """Function:  test_machine

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(machine.Machine())


if __name__ == "__main__":
    unittest.main()
