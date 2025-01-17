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
        self.result_str = ["this", "is", "another", "test"]
        self.result_file = ["and", "yet", "another", "test"]

    def test_load_empty_file(self):

        """Function:  test_load_empty_file

        Description:  Test loading from an empty file.

        Arguments:

        """

        log = gen_class.LogFile()
        with open(self.input_file2, "r", encoding="UTF-8") as finst:
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
        with open(self.input_file, "r", encoding="UTF-8") as finst:
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
