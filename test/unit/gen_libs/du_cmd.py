# Classification (U)

"""Program:  du_cmd.py

    Description:  Unit testing of du_cmd in gen_libs.py.

    Usage:
        test/unit/gen_libs/du_cmd.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                                 # pylint:disable=E0401,C0413
import version                                  # pylint:disable=C0413,E0401

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_passed_dir
        test_passed_dir
        test_current_sub_dirs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir = "."
        self.dir2 = "./test"

    def test_no_passed_dir(self):

        """Function:  test_no_passed_dir

        Description:  Test with no directory argument passed.

        Arguments:

        """

        self.assertGreater(gen_libs.du_cmd(), 0)

    def test_passed_dir(self):

        """Function:  test_passed_dir

        Description:  Test with passed directory argument.

        Arguments:

        """

        self.assertGreater(gen_libs.du_cmd(self.dir2), 0)

    def test_current_sub_dirs(self):

        """Function:  test_current_sub_dirs

        Description:  Test with current directory with sub-directories.

        Arguments:

        """

        self.assertGreater(gen_libs.du_cmd(self.dir), 0)


if __name__ == "__main__":
    unittest.main()
