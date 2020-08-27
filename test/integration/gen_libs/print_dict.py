#!/usr/bin/python
# Classification (U)

"""Program:  print_dict.py

    Description:  Unit testing of print_dict in gen_libs.py.

    Usage:
        test/integration/gen_libs/print_dict.py

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
import filecmp

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
        test_non_dict -> Test with non-dictionary object.
        test_ofile_json -> Test with ofile and json_fmt arguments.
        test_set_no_std -> Test with no_std argument.
        test_set_json -> Test with json_fmt argument.
        test_set_ofile -> Test with ofile argument.
        test_set_default -> Test with default settings.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {"key1": "value1", "key2": {"key3": "value2"}}
        self.ofile = "test/integration/gen_libs/tmp/test_print_dict.txt"
        self.basefile = "test/integration/gen_libs/basefiles/print_dict.txt"

    def test_non_dict(self):

        """Function:  test_non_dict

        Description:  Test with non-dictionary object.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict([1, 2, 3]),
                         (True, "Error: [1, 2, 3] -> Is not a dictionary"))

    def test_ofile_json(self):

        """Function:  test_ofile_json

        Description:  Test with ofile and json_fmt arguments.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict(self.data, ofile=self.ofile,
                                             json_fmt=True, no_std=True),
                         (False, None))

        self.assertTrue(filecmp.cmp(self.basefile, self.ofile))

    def test_set_no_std(self):

        """Function:  test_set_no_std

        Description:  Test with no_std argument.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict(self.data, no_std=True),
                         (False, None))

    def test_set_json(self):

        """Function:  test_set_json

        Description:  Test with json_fmt argument.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict(self.data, ofile=self.ofile,
                                             json_fmt=True, no_std=True),
                         (False, None))

        self.assertTrue(filecmp.cmp(self.basefile, self.ofile))

    def test_set_ofile(self):

        """Function:  test_set_ofile

        Description:  Test with ofile argument.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict(self.data, ofile=self.ofile,
                                             no_std=True), (False, None))

        self.assertTrue(os.path.isfile(self.ofile))

    def test_set_default(self):

        """Function:  test_set_default

        Description:  Test with default settings.

        Arguments:

        """

        self.assertEqual(gen_libs.print_dict(self.data, no_std=True),
                         (False, None))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
