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
        test_load_empty_file
        test_load_empty_str
        test_load_file
        test_load_str_single

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
        with open(self.input_file2, "r", encoding="UTF-8") as finst:
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
        with open(self.input_file, "r", encoding="UTF-8") as finst:
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
