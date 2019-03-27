#!/usr/bin/python
# Classification (U)

"""Program:  arg_file_chk.py

    Description:  Unit testing of arg_file_chk in arg_parser.py.

    Usage:
        test/unit/arg_parser/arg_file_chk.py

    Arguments:
        None

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
import mock

# Local
sys.path.append(os.getcwd())
import arg_parser
import version

# Version
__version__ = version.__version__

class FileOpen(object):

    """Class:  FileOpen

    Description:  Class stub holder for file open class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        close -> Stub holder for close function.

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:
            None

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_no_match_between_lists -> Test with no match between lists passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.file_chk_list = ["-f"]
        self.args_array = {"-f": "test/file1", "-m": "Marker"}
        self.open = Open()

    @mock.patch("arg_parser.open")
    def test_no_match_between_lists(self, mock_open):

        """Function:  test_no_match_between_lists

        Description:  Test with no match between lists passed.

        Arguments:
            mock_open -> Mock Ref:  arg_parser.open

        """

        mock_open.return_value = self.open

        self.assertFalse(arg_parser.arg_file_chk(self.args_array,
                                                 self.file_chk_list))


if __name__ == "__main__":
    unittest.main()
