# Classification (U)

"""Program:  singleinstanceexception.py

    Description:  Unit testing of SingleInstanceException in gen_class.py.

    Usage:
        test/unit/gen_class/singleinstanceexception.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_singleinstanceexception

    """

    def test_singleinstanceexception(self):

        """Function:  test_singleinstanceexception

        Description:  Test with no arguments.

        Arguments:

        """

        self.assertTrue(gen_class.SingleInstanceException())


if __name__ == "__main__":
    unittest.main()
