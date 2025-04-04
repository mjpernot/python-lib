# Classification (U)

"""Program:  clear_file.py

    Description:  Unit testing of clear_file in gen_libs.py.

    Usage:
        test/unit/gen_libs/clear_file.py

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


def clear_file_check(f_name):

    """Function:  clear_file_check

    Description:  Checks to see if a file was cleared of data.

    Arguments:
        (input) f_name
        (output) True|False

    """

    gen_libs.clear_file(f_name)

    return os.stat(f_name).st_size == 0


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_clear_file
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_libs/tmp/clear_file_test.out")

        gen_libs.write_file(self.f_name, "w", "TEST")

    def test_clear_file(self):

        """Function:  test_clear_file

        Description:  Test with clearing an existing file that has data.

        Arguments:

        """

        self.assertTrue(clear_file_check(self.f_name))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()
