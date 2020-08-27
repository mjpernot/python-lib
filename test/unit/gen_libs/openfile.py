#!/usr/bin/python
# Classification (U)

"""Program:  openfile.py

    Description:  Unit testing of openfile in gen_libs.py.

    Usage:
        test/unit/gen_libs/openfile.py

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
import subprocess

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
        test_openfile -> Test with normal flat file.
        test_openfile_gzip -> Test with compressed file.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = "test/unit/gen_libs/tmp/openfile_test"
        self.f_name2 = "test/unit/gen_libs/tmp/openfile_test2"

        f_hdlr = open(self.f_name, "w")
        print("This is a test file", file=f_hdlr)
        f_hdlr.close()

        f_hdlr2 = open(self.f_name2, "w")
        print("This is a test file", file=f_hdlr2)
        f_hdlr2.close()

        cmd = gen_libs.get_inst(subprocess)
        proc1 = cmd.Popen(["gzip", self.f_name2])
        proc1.wait()

        self.f_name2 = self.f_name2 + ".gz"

    def test_openfile(self):

        """Function:  test_openfile

        Description:  Test with normal flat file.

        Arguments:

        """

        f_hdlr = gen_libs.openfile(self.f_name)
        status = f_hdlr.closed
        f_hdlr.close()

        self.assertFalse(status)

    def test_openfile_gzip(self):

        """Function:  test_openfile_gzip

        Description:  Test with compressed file.

        Arguments:

        """

        f_hdlr = gen_libs.openfile(self.f_name2)
        status = f_hdlr.closed
        f_hdlr.close()

        self.assertFalse(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)
        os.remove(self.f_name2)


if __name__ == "__main__":
    unittest.main()
