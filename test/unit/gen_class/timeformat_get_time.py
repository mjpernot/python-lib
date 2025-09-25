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
import time
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
        test_current_new_timeform3
        test_current_new_timeform2
        test_current_new_timeform
        test_current_timeform3
        test_current_timeform2
        test_current_timeform
        test_no_create_time
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
        self.tform2 = gen_class.TimeFormat()
        self.newform = "%Y%m%d_%H%M"
        self.newform2 = "%Y%m%d:%H%M%S"

    def test_current_new_timeform3(self):

        """Function:  test_current_new_timeform3

        Description:  Test with current time option for current time option.

        Arguments:

        """

        dtg = gen_class.TimeFormat()
        dtg.create_time()
        time.sleep(1)
        data = self.tform.get_time(newform=self.newform2)

        self.assertNotEqual(
            self.tform.get_time(newform=self.newform2, current=True), data)

    def test_current_new_timeform2(self):

        """Function:  test_current_new_timeform2

        Description:  Test with new time format for current time option.

        Arguments:

        """

        self.assertEqual(
            len(self.tform.get_time(
                newform=self.newform2, micro=True, current=True)), 20)

    def test_current_new_timeform(self):

        """Function:  test_current_new_timeform

        Description:  Test with new time format for current time option.

        Arguments:

        """

        self.assertEqual(
            len(self.tform.get_time(newform=self.newform2, current=True)), 15)

    def test_current_timeform3(self):

        """Function:  test_current_timeform3

        Description:  Test with current time option.

        Arguments:

        """

        dtg = gen_class.TimeFormat()
        dtg.create_time()
        time.sleep(1)

        self.assertNotEqual(
            self.tform.get_time("dtg", current=True), dtg.get_time("dtg"))

    def test_current_timeform2(self):

        """Function:  test_current_timeform2

        Description:  Test with existing current time option with microseconds.

        Arguments:

        """

        self.assertEqual(
            len(self.tform.get_time("ymd", micro=True, current=True)), 13)

    def test_current_timeform(self):

        """Function:  test_current_timeform

        Description:  Test with current time option.

        Arguments:

        """

        self.assertEqual(len(self.tform.get_time("ymd", current=True)), 8)

    def test_no_create_time(self):

        """Function:  test_no_create_time

        Description:  Test with no time in rdtg attribute (no previous call to
            create_time).

        Arguments:

        """

        self.assertIsNone(self.tform2.get_time("dtg"))

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
