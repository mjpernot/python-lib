# Classification (U)

"""Program:  create_cfg_array.py

    Description:  Unit testing of create_cfg_array in gen_libs.py.

    Usage:
        test/unit/gen_libs/create_cfg_array.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_multiple_entries
        test_single_entry
        test_no_data
        test_empty_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg_file1 = "create_cfg_array_config_file1"
        self.cfg_file2 = "create_cfg_array_config_file2"
        self.cfg_file3 = "create_cfg_array_config_file3"
        self.cfg_file4 = "create_cfg_array_config_file4"
        self.cfg_file5 = \
            "./test/unit/gen_libs/testfiles/create_cfg_array_config_file3"
        self.cfg_path = "./test/unit/gen_libs/testfiles"

        self.base = [{}]
        self.base2 = [{'host': 'SERVER_IP', 'port': '3306', 'user': 'root'}]
        self.base3 = [{'host': 'SERVER_IP', 'port': '3306', 'user': 'root'},
                      {'host': 'SERVER_IP2', 'port': '3307', 'user': 'root'}]

    def test_single_entry2(self):

        """Function:  test_single_entry

        Description:  Test with single user entry.

        Arguments:

        """

        self.assertEqual(gen_libs.create_cfg_array(self.cfg_file5,
                                                   cfg_path=self.cfg_path),
                         self.base2)

    def test_multiple_entries(self):

        """Function:  test_multiple_entries

        Description:  Test with multiple user entries.

        Arguments:

        """

        self.assertEqual(gen_libs.create_cfg_array(self.cfg_file4,
                                                   cfg_path=self.cfg_path),
                         self.base3)

    def test_single_entry(self):

        """Function:  test_single_entry

        Description:  Test with single user entry.

        Arguments:

        """

        self.assertEqual(gen_libs.create_cfg_array(self.cfg_file3,
                                                   cfg_path=self.cfg_path),
                         self.base2)

    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data in file, only comments.

        Arguments:

        """

        self.assertEqual(gen_libs.create_cfg_array(self.cfg_file2,
                                                   cfg_path=self.cfg_path),
                         self.base)

    def test_empty_file(self):

        """Function:  test_empty_file

        Description:  Test with empty file.

        Arguments:

        """

        self.assertEqual(gen_libs.create_cfg_array(self.cfg_file1,
                                                   cfg_path=self.cfg_path),
                         self.base)


if __name__ == "__main__":
    unittest.main()
