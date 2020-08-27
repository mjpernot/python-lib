#!/usr/bin/python
# Classification (U)

"""Program:  logfile_load_marker.py

    Description:  Unit testing of LogFile.load_marker in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_load_marker.py

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
        setUp -> Initialize testing environment.
        test_load_empty_file -> Test loading from an empty file.
        test_load_empty_str -> Test loading from an empty sting.
        test_load_file -> Test loading from a file.
        test_load_str_single -> Test loading from a single sting.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.input_str = "This is a test marker"
        self.input_str2 = "This is a test marker\n"
        self.input_file = "test/unit/gen_class/testfiles/load_marker_file.txt"
        self.input_file2 = "test/unit/gen_class/testfiles/empty_file.txt"
        self.input_file3 = \
            "test/unit/gen_class/testfiles/load_marker_file2.txt"

        self.result_str = "This is a test marker"

    def test_load_empty_file(self):

        """Function:  test_load_empty_file

        Description:  Test loading from an empty file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file2)
        log.load_marker(finst)

        self.assertEqual(log.marker, "")

    def test_load_empty_str(self):

        """Function:  test_load_empty_str

        Description:  Test loading from an empty sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_marker("")

        self.assertEqual(log.marker, "")

    def test_load_file(self):

        """Function:  test_load_file

        Description:  Test loading from a file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file)
        log.load_marker(finst)

        self.assertEqual(log.marker, self.result_str)

    def test_load_str_single(self):

        """Function:  test_load_str_single

        Description:  Test loading from a single sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_marker(self.input_str)

        self.assertEqual(log.marker, self.result_str)


if __name__ == "__main__":
    unittest.main()
