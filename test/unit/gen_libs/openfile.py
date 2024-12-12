# Classification (U)

"""Program:  openfile.py

    Description:  Unit testing of openfile in gen_libs.py.

    Usage:
        test/unit/gen_libs/openfile.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import subprocess

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_openfile
        test_openfile_gzip
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = "test/unit/gen_libs/tmp/openfile_test"
        self.f_name2 = "test/unit/gen_libs/tmp/openfile_test2"

        with open(self.f_name, "w", encoding="UTF-8") as f_hdlr:
            print("This is a test file", file=f_hdlr)

        with open(self.f_name2, "w", encoding="UTF-8") as f_hdlr2:
            print("This is a test file", file=f_hdlr2)

        proc1 = subprocess.Popen(["gzip", self.f_name2]) # pylint:disable=R1732
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
