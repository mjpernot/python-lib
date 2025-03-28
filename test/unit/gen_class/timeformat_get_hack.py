# Classification (U)

"""Program:  timeformat_get_hack.py

    Description:  Unit testing of TimeFormat.get_hack in gen_class.py.

    Usage:
        test/unit/gen_class/timeformat_get_hack.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_time_not_exists
        test_time_exists

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.tform = gen_class.TimeFormat()
        self.name = "ymd"
        self.name2 = "ymda"

    def test_time_not_exists(self):

        """Function:  test_time_not_exists

        Description:  Test with creating time hack with no existing format.

        Arguments:

        """

        self.tform.create_hack(self.name)

        self.assertFalse(self.tform.get_hack(self.name2))

    def test_time_exists2(self):

        """Function:  test_time_exists2

        Description:  Test with creating time hack with existing time format.

        Arguments:

        """

        self.tform.create_hack(self.name)
        time_hack = self.tform.thacks[self.name]

        self.assertEqual(self.tform.get_hack(self.name), time_hack)

    def test_time_exists(self):

        """Function:  test_time_exists

        Description:  Test with creating time hack with existing time format.

        Arguments:

        """

        self.tform.create_hack(self.name)

        self.assertTrue(self.tform.get_hack(self.name))


if __name__ == "__main__":
    unittest.main()
