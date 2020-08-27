#!/usr/bin/python
# Classification (U)

"""Program:  and_is_true.py

    Description:  Unit testing of and_is_true in gen_libs.py.

    Usage:
        test/unit/gen_libs/and_is_true.py

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
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_yes_yes -> Test with yes and yes values.
        test_no_no -> Test with no and no values.
        test_no_yes -> Test with no and yes values.
        test_yes_no -> Test with yes and no values.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.yes = "Yes"
        self.nos = "No"

    def test_yes_yes(self):

        """Function:  test_yes_yes

        Description:  Test with data of yes and yes.

        Arguments:

        """

        self.assertTrue(gen_libs.and_is_true(self.yes, self.yes))

    def test_no_no(self):

        """Function:  test_no_no

        Description:  Test with data of no and no.

        Arguments:

        """

        self.assertFalse(gen_libs.and_is_true(self.nos, self.nos))

    def test_no_yes(self):

        """Function:  test_no_yes

        Description:  Test with data of no and yes.

        Arguments:

        """

        self.assertFalse(gen_libs.and_is_true(self.nos, self.yes))

    def test_yes_no(self):

        """Function:  test_yes_no

        Description:  Test with data of yes and no.

        Arguments:

        """

        self.assertFalse(gen_libs.and_is_true(self.yes, self.nos))


if __name__ == "__main__":
    unittest.main()
