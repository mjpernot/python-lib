#!/usr/bin/python
# Classification (U)

"""Program:  logfile_load_loglist.py

    Description:  Unit testing of LogFile.load_loglist in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_load_loglist.py

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
        test_load_multiple_files
        test_load_dict_no_key
        test_load_dict_list
        test_load_empty_file
        test_load_empty_str
        test_load_empty_list
        test_load_file
        test_load_str_multiple
        test_load_str_single
        test_load_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.line1 = "This is line 1"
        self.line2 = "This is line 2"
        self.line3 = "This is line 3"
        self.line4 = "This is line 4"
        self.input_dict = {"lines": ["This is line 1 ", self.line2,
                                     "This is line 3  ", self.line4]}
        self.input_dict2 = {"lines":
                            "This is line 1\nThis is line 2\nThis is line 3\n"}
        self.input_list = ["This is line 1 ", self.line2,
                           "This is line 3  ", self.line4]
        self.input_str = "This is another test"
        self.input_str2 = "This is line 1\nThis is line 2\nThis is line 3\n"
        self.input_file = "test/unit/gen_class/testfiles/load_loglist_file.txt"
        self.input_file2 = "test/unit/gen_class/testfiles/empty_file.txt"
        self.input_file3 = \
            "test/unit/gen_class/testfiles/load_loglist_file2.txt"

        self.result_dict = [self.line1, self.line2, self.line3, self.line4]
        self.result_dict2 = [self.line1, self.line2, self.line3]
        self.result_list = [self.line1, self.line2, self.line3, self.line4]
        self.result_str = ["This is another test"]
        self.result_str2 = [self.line1, self.line2, self.line3]
        self.result_file = ["This is test 1", "This is test 2",
                            "This is test 3"]
        self.result_file2 = ["This is test 1", "This is test 2",
                             "This is test 3", "This is test 4",
                             "This is test 5", "This is test 6"]

    def test_load_multiple_files(self):

        """Function:  test_load_multiple_files

        Description:  Test loading from multiple files.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file)
        finst2 = open(self.input_file3)
        log.load_loglist(finst)
        log.load_loglist(finst2)

        self.assertEqual((log.loglist, log.lastline), (self.result_file2,
                                                       self.result_file2[-1]))

    def test_load_dict_no_key(self):

        """Function:  test_load_empty_dict

        Description:  Test loading from a dictionary with no key passed.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist(self.input_dict)

        self.assertEqual((log.loglist, log.lastline), ([], None))

    def test_load_empty_dict(self):

        """Function:  test_load_empty_dict

        Description:  Test loading from an empty dictionary.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist({}, dictkey="lines")

        self.assertEqual((log.loglist, log.lastline), ([], None))

    def test_load_dict_str(self):

        """Function:  test_load_dict_str

        Description:  Test loading from a dictionary with a string.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist(self.input_dict2, dictkey="lines")

        self.assertEqual((log.loglist, log.lastline), (self.result_dict2,
                                                       self.result_dict2[-1]))

    def test_load_dict_list(self):

        """Function:  test_load_dict_list

        Description:  Test loading from a dictionary with a list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist(self.input_dict, dictkey="lines")

        self.assertEqual((log.loglist, log.lastline), (self.result_dict,
                                                       self.result_dict[-1]))

    def test_load_empty_file(self):

        """Function:  test_load_empty_file

        Description:  Test loading from an empty file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file2)
        log.load_loglist(finst)

        self.assertEqual((log.loglist, log.lastline), ([], None))

    def test_load_empty_str(self):

        """Function:  test_load_empty_str

        Description:  Test loading from an empty sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist("")

        self.assertEqual((log.loglist, log.lastline), ([""], ""))

    def test_load_empty_list(self):

        """Function:  test_load_empty_list

        Description:  Test loading from an empty list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist([])

        self.assertEqual((log.loglist, log.lastline), ([], None))

    def test_load_file(self):

        """Function:  test_load_file

        Description:  Test loading from a file.

        Arguments:

        """

        log = gen_class.LogFile()
        finst = open(self.input_file)
        log.load_loglist(finst)

        self.assertEqual((log.loglist, log.lastline), (self.result_file,
                                                       self.result_file[-1]))

    def test_load_str_multiple(self):

        """Function:  test_load_str_multiple

        Description:  Test loading from a multiple line sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist(self.input_str2)

        self.assertEqual((log.loglist, log.lastline), (self.result_str2,
                                                       self.result_str2[-1]))

    def test_load_str_single(self):

        """Function:  test_load_str_single

        Description:  Test loading from a single sting.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist(self.input_str)

        self.assertEqual((log.loglist, log.lastline), (self.result_str,
                                                       self.result_str[-1]))

    def test_load_list(self):

        """Function:  test_load_list

        Description:  Test loading from a list.

        Arguments:

        """

        log = gen_class.LogFile()
        log.load_loglist(self.input_list)

        self.assertEqual((log.loglist, log.lastline), (self.result_list,
                                                       self.result_list[-1]))


if __name__ == "__main__":
    unittest.main()
