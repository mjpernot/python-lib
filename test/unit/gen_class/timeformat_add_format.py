#!/usr/bin/python
# Classification (U)

"""Program:  timeformat_add_format.py

    Description:  Unit testing of TimeFormat.add_format in gen_class.py.

    Usage:
        test/unit/gen_class/timeformat_add_format.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import datetime

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
        test_tformat2
        test_tformat

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

        self.tform.add_format(self.name, self.texpr, micro=True)

        self.assertEqual(self.tform.tformats[self.name]["micro"], True)

    def test_micro_default(self):

        """Function:  test_micro_default

        Description:  Test with default micro attribute.

        Arguments:

        """

        self.tform.add_format(self.name, self.texpr)

        self.assertEqual(self.tform.tformats[self.name]["micro"], False)

    def test_delimit(self):

        """Function:  test_delimit

        Description:  Test with delimiter attribute.

        Arguments:

        """

        self.tform.add_format(self.name, self.texpr, delimit=self.delimit2)

        self.assertEqual(self.tform.tformats[self.name]["del"], self.delimit2)

    def test_delimit_default(self):

        """Function:  test_delimit_default

        Description:  Test with default delimiter attribute.

        Arguments:

        """

        self.tform.add_format(self.name, self.texpr)

        self.assertEqual(self.tform.tformats[self.name]["del"], self.delimit)

    def test_tformat2(self):

        """Function:  test_tformat2

        Description:  Test adding time format.

        Arguments:

        """

        self.tform.add_format(self.name, self.texpr)

        self.assertEqual(self.tform.tformats[self.name]["format"], self.texpr)

    def test_tformat(self):

        """Function:  test_tformat

        Description:  Test adding time format.

        Arguments:

        """

        self.tform.add_format(self.name, self.texpr)

        self.assertTrue(self.name in self.tform.tformats)


if __name__ == "__main__":
    unittest.main()
