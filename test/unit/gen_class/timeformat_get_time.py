# Classification (U)

"""Program:  timeformat_get_time.py

    Description:  Unit testing of TimeFormat.get_time in gen_class.py.

    Usage:
        test/unit/gen_class/timeformat_get_time.py

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
        test_new_timeform2
        test_new_timeform
        test_exist_timeform2
        test_exist_timeform

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.tform = gen_class.TimeFormat()
        self.tform.create_time()
        self.newform = "%Y%m%d_%H%M"

    def test_no_timeform(self):

        """Function:  test_no_timeform

        Description:  Test with no time format passed.

        Arguments:

        """

        self.assertIsNone(self.tform.get_time())

    def test_new_timeform2(self):

        """Function:  test_new_timeform2

        Description:  Test with new time format.

        Arguments:

        """

        self.assertEqual(
            len(self.tform.get_time(newform=self.newform, micro=True)), 18)

    def test_new_timeform(self):

        """Function:  test_new_timeform

        Description:  Test with new time format.

        Arguments:

        """

        self.assertEqual(len(self.tform.get_time(newform=self.newform)), 13)

    def test_exist_timeform2(self):

        """Function:  test_exist_timeform2

        Description:  Test with existing time format with microseconds.

        Arguments:

        """

        self.assertEqual(len(self.tform.get_time("ymd", micro=True)), 13)

    def test_exist_timeform(self):

        """Function:  test_exist_timeform

        Description:  Test with existing time format.

        Arguments:

        """

        self.assertEqual(len(self.tform.get_time("ymd")), 8)


if __name__ == "__main__":
    unittest.main()
