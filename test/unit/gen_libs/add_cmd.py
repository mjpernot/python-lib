#!/usr/bin/python
# Classification (U)

"""Program:  add_cmd.py

    Description:  Unit testing of add_cmd in gen_libs.py.

    Usage:
        test/unit/gen_libs/add_cmd.py

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
        setUp
        test_cmd_value
        test_cmd_only

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cmd = []
        self.arg = "--optionsetting="
        self.val = "valuesetting"
        self.base1 = ["--optionsetting="]
        self.base2 = ["--optionsetting=valuesetting"]

    def test_cmd_value(self):

        """Function:  test_cmd_value

        Description:  Test with command and value.

        Arguments:

        """

        self.assertEqual(gen_libs.add_cmd(self.cmd, arg=self.arg,
                                          val=self.val), self.base2)

    def test_cmd_only(self):

        """Function:  test_cmd_only

        Description:  Test with command only.

        Arguments:

        """

        self.assertEqual(gen_libs.add_cmd(self.cmd, arg=self.arg), self.base1)


if __name__ == "__main__":
    unittest.main()
