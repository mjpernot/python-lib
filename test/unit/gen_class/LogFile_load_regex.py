#!/usr/bin/python
# Classification (U)

"""Program:  LogFile_load_regex.py

    Description:  Unit testing of LogFile.load_regex in gen_class.py.

    Usage:
        test/unit/gen_class/LogFile_load_regex.py

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
        test_load_file_multiple -> Test loading from a file multiple lines.
        test_load_empty_file -> Test loading from an empty file.
        test_load_empty_str -> Test loading from an empty sting.
        test_load_file -> Test loading from a file.
        test_load_str_multiple -> Test loading from a multiple line string.
        test_load_str_single -> Test loading from a single sting.
        test_load_empty_list -> Test loading from an empty list.
        test_load_list_multiple -> Test loading from a multiple item list.
        test_load_list -> Test loading from a list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.regex = "\d{4}\-\d{2}\-\d{2}"
        self.input_list = [self.regex]
        self.input_list2 = [self.regex, "d{2}:\d{2}:\d{2}"]
        self.input_str = self.regex
        self.input_str2 = "\d{4}\-\d{2}\-\d{2}\nd{2}:\d{2}:\d{2}\n"
        self.input_file = "test/unit/gen_class/testfiles/load_regex_file.txt"
        self.input_file2 = "test/unit/gen_class/testfiles/empty_file.txt"
        self.input_file3 = "test/unit/gen_class/testfiles/load_regex_file2.txt"

        self.result_str = self.regex
        self.result_str2 = "\d{4}\-\d{2}\-\d{2}|d{2}:\d{2}:\d{2}"

    def test_load_file_multiple(self):

        """Function:  test_load_file

        Description:  Test loading from a file multiple lines.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file3)
        log.load_regex(finst)

        self.assertEqual(log.regex, self.result_str2)

    def test_load_empty_file(self):

        """Function:  test_load_empty_file

        Description:  Test loading from an empty file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file2)
        log.load_regex(finst)

        self.assertEqual(log.regex, "")

    def test_load_empty_str(self):

        """Function:  test_load_empty_str

        Description:  Test loading from an empty sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_regex("")

        self.assertEqual(log.regex, "")

    def test_load_file(self):

        """Function:  test_load_file

        Description:  Test loading from a file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file)
        log.load_regex(finst)

        self.assertEqual(log.regex, self.result_str)

    def test_load_str_multiple(self):

        """Function:  test_load_str_multiple

        Description:  Test loading from a multiple line sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_regex(self.input_str2)

        self.assertEqual(log.regex, self.result_str2)

    def test_load_str_single(self):

        """Function:  test_load_str_single

        Description:  Test loading from a single sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_regex(self.input_str)

        self.assertEqual(log.regex, self.result_str)

    def test_load_empty_list(self):

        """Function:  test_load_empty_list

        Description:  Test loading from an empty list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_regex([])

        self.assertEqual(log.regex, "")

    def test_load_list_multiple(self):

        """Function:  test_load_list_multiple

        Description:  Test loading from a list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_regex(self.input_list2)

        self.assertEqual(log.regex, self.result_str2)

    def test_load_list(self):

        """Function:  test_load_list

        Description:  Test loading from a list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_regex(self.input_list)

        self.assertEqual(log.regex, self.result_str)


if __name__ == "__main__":
    unittest.main()
