# Classification (U)

"""Program:  rm_file.py

    Description:  Unit testing of rm_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/rm_file.py

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
        test_with_rm_file
        test_with_raise_exception

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = "test/unit/gen_libs/tmp/test_rm_file.txt"
        self.err_msg = "Error: test/unit/gen_libs/tmp/test_rm_file.txt" \
                       + " - No such file or directory"

    def test_with_rm_file(self):

        """Function:  test_with_rm_file

        Description:  Test with removing file.

        Arguments:

        """

        with open(self.f_name, "a", encoding="UTF-8"):
            os.utime(self.f_name, None)

        self.assertEqual(gen_libs.rm_file(self.f_name), (False, None))

    def test_with_raise_exception(self):

        """Function:  test_with_raise_exception

        Description:  Test raising exception.

        Arguments:

        """

        self.assertEqual(gen_libs.rm_file(self.f_name), (True, self.err_msg))


if __name__ == "__main__":
    unittest.main()
