#!/usr/bin/python
# Classification (U)

"""Program:  and_is_true.py

    Description:  Unit testing of and_is_true in gen_libs.py.

    Usage:
        test/unit/gen_libs/and_is_true.py

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
import gen_libs
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_no_yes -> Test with no and yes value.
        test_yes_no -> Test with yes and no value.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.yes = "Yes"
        self.no = "No"

    def test_no_yes(self):

        """Function:  test_no_yes

        Description:  Test with data of no and yes.

        Arguments:
            None

        """

        self.assertFalse(gen_libs.and_is_true(self.no, self.yes))

    def test_yes_no(self):

        """Function:  test_yes_no

        Description:  Test with data of yes and no.

        Arguments:
            None

        """

        self.assertFalse(gen_libs.and_is_true(self.yes, self.no))


if __name__ == "__main__":
    unittest.main()
