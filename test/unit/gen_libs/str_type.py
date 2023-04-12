# Classification (U)

"""Program:  str_type.py

    Description:  Unit testing of str_type in gen_libs.py.

    Usage:
        test/unit/gen_libs/str_type.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_str_type

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        if sys.version_info[0] == 3:
            self.str_type = str

        else:
            self.str_type = basestring

    def test_str_type(self):

        """Function:  test_str_type

        Description:  Test to see if correct string type comes back.

        Arguments:

        """

        self.assertEqual(gen_libs.str_type(), self.str_type)


if __name__ == "__main__":
    unittest.main()
