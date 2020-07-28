#!/usr/bin/python
# Classification (U)

"""Program:  load_module.py

    Description:  Unit testing of load_module in gen_libs.py.

    Usage:
        test/unit/gen_libs/load_module.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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
        test_load_module -> Test load_module function.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mod_name = "test_load_module"
        self.mod_path = "test/unit/gen_libs/tmp"
        self.fname = os.path.join(self.mod_path, self.mod_name + ".py")
        self.fname2 = os.path.join(self.mod_path, self.mod_name + ".pyc")
        data = "entry=True"

        with open(self.fname, "w") as f_hdlr:
            print(data, file=f_hdlr)

    def test_load_module(self):

        """Function:  test_load_module

        Description:  Test load_module function.

        Arguments:

        """

        cfg = gen_libs.load_module(self.mod_name, self.mod_path)

        self.assertEqual(cfg.entry, True)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.fname):
            os.remove(self.fname)

        if os.path.isfile(self.fname2):
            os.remove(self.fname2)


if __name__ == "__main__":
    unittest.main()
