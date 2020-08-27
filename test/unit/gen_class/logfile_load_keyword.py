#!/usr/bin/python
# Classification (U)

"""Program:  logfile_load_keyword.py

    Description:  Unit testing of LogFile.load_keyword in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_load_keyword.py

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
        test_load_empty_list -> Test loading from an empty list.
        test_load_file -> Test loading from a file.
        test_load_str -> Test loading from a sting.
        test_load_list -> Test loading from a list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.input_list = ["This", "is", "a", "test"]
        self.input_str = "This is another test"
        self.input_file = "test/unit/gen_class/testfiles/load_ignore_file.txt"
        self.input_file2 = "test/unit/gen_class/testfiles/empty_file.txt"
        self.result_list = ["this", "is", "a", "test"]
        self.result_str = ["this", "is", "another", "test"]
        self.result_file = ["and", "yet", "another", "test"]

    def test_load_empty_file(self):

        """Function:  test_load_empty_file

        Description:  Test loading from an empty file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file2)
        log.load_keyword(finst)

        self.assertEqual(log.keyword, [])

    def test_load_empty_str(self):

        """Function:  test_load_empty_str

        Description:  Test loading from an empty sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_keyword("")

        self.assertEqual(log.keyword, [""])

    def test_load_empty_list(self):

        """Function:  test_load_empty_list

        Description:  Test loading from an empty list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_keyword([])

        self.assertEqual(log.keyword, [])

    def test_load_file(self):

        """Function:  test_load_file

        Description:  Test loading from a file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file)
        log.load_keyword(finst)

        self.assertEqual(log.keyword, self.result_file)

    def test_load_str(self):

        """Function:  test_load_str

        Description:  Test loading from a sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_keyword(self.input_str)

        self.assertEqual(log.keyword, self.result_str)

    def test_load_list(self):

        """Function:  test_load_list

        Description:  Test loading from a list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_keyword(self.input_list)

        self.assertEqual(log.keyword, self.result_list)


if __name__ == "__main__":
    unittest.main()
