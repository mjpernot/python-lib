#!/usr/bin/python
# Classification (U)

"""Program:  logfile_load_ignore.py

    Description:  Unit testing of LogFile.load_ignore in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_load_ignore.py

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
        test_load_empty_file
        test_load_empty_str
        test_load_empty_list
        test_load_file
        test_load_str
        test_load_list

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
        self.result_str = ["this is another test"]
        self.result_file = ["and", "yet", "another", "test"]

    def test_load_empty_file(self):

        """Function:  test_load_empty_file

        Description:  Test loading ignore from an empty file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file2)
        log.load_ignore(finst)

        self.assertEqual(log.ignore, [])

    def test_load_empty_str(self):

        """Function:  test_load_empty_str

        Description:  Test loading ignore from an empty sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_ignore("")

        self.assertEqual(log.ignore, [""])

    def test_load_empty_list(self):

        """Function:  test_load_empty_list

        Description:  Test loading ignore from an empty list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_ignore([])

        self.assertEqual(log.ignore, [])

    def test_load_file(self):

        """Function:  test_load_file

        Description:  Test loading ignore from a file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file)
        log.load_ignore(finst)

        self.assertEqual(log.ignore, self.result_file)

    def test_load_str(self):

        """Function:  test_load_str

        Description:  Test loading ignore from a sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_ignore(self.input_str)

        self.assertEqual(log.ignore, self.result_str)

    def test_load_list(self):

        """Function:  test_load_list

        Description:  Test loading ignore from a list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_ignore(self.input_list)

        self.assertEqual(log.ignore, self.result_list)


if __name__ == "__main__":
    unittest.main()
