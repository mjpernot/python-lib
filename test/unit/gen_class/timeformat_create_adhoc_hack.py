#!/usr/bin/python
# Classification (U)

"""Program:  timeformat_create_adhoc_hack.py

    Description:  Unit testing of TimeFormat.create_adhoc_hack in gen_class.py.

    Usage:
        test/unit/gen_class/timeformat_create_adhoc_hack.py

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
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_micro
        test_micro_default
        test_delimit
        test_delimit_default
        test_adhoc

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.tform = gen_class.TimeFormat()
        self.delimit = "."
        self.delimit2 = "_"
        self.name = "ymd_hm"
        self.texpr = "%Y%m%d_%H%M"

    def test_micro(self):

        """Function:  test_micro

        Description:  Test with micro attribute.

        Arguments:

        """

        self.tform.create_adhoc_hack(self.name, self.texpr, micro=True)

        self.assertTrue(self.tform.thacks[self.name].split(".")[1])

    def test_delimit(self):

        """Function:  test_delimit

        Description:  Test with delimiter attribute.

        Arguments:

        """

        self.tform.create_adhoc_hack(
            self.name, self.texpr, delimit=self.delimit2, micro=True)

        self.assertEqual(self.tform.thacks[self.name][13], self.delimit2)

    def test_micro_default(self):

        """Function:  test_micro_default

        Description:  Test with default micro value.

        Arguments:

        """

        self.tform.create_adhoc_hack(self.name, self.texpr)

        self.assertEqual(len(self.tform.thacks[self.name]), 13)

    def test_adhoc(self):

        """Function:  test_adhoc

        Description:  Test with creating adhoc time hack.

        Arguments:

        """

        self.tform.create_adhoc_hack(self.name, self.texpr)

        self.assertTrue(self.name in self.tform.thacks)


if __name__ == "__main__":
    unittest.main()
