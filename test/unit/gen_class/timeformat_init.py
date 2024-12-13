# Classification (U)

"""Program:  timeformat_init.py

    Description:  Unit testing of TimeFormat.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/timeformat_init.py

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
        test_delimit
        test_micro
        test_thacks
        test_tformats

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.tform = gen_class.TimeFormat()
        self.delimit = "."
        self.micro = False
        self.thacks = {}
        self.tformats = {
            "ymd": {"format": "%Y%m%d", "del": "", "micro": False},
            "dmy": {"format": "%d%m%Y", "del": "", "micro": False},
            "zulu": {
                "format": "%Y-%m-%dT%H:%M:%SZ", "del": "", "micro": False},
            "dtg": {"format": "%Y%m%d_%H%M%S", "del": "", "micro": False}}

    def test_delimit(self):

        """Function:  test_delimit

        Description:  Test the delimit attribute.

        Arguments:

        """

        self.assertEqual(self.tform.delimit, self.delimit)

    def test_micro(self):

        """Function:  test_micro

        Description:  Test the micro attribute.

        Arguments:

        """

        self.assertEqual(self.tform.micro, self.micro)

    def test_thacks(self):

        """Function:  test_thacks

        Description:  Test the thacks attribute.

        Arguments:

        """

        self.assertEqual(self.tform.thacks, self.thacks)

    def test_tformats(self):

        """Function:  test_tformats

        Description:  Test the tformats attribute.

        Arguments:

        """

        self.assertEqual(self.tform.tformats, self.tformats)


if __name__ == "__main__":
    unittest.main()
