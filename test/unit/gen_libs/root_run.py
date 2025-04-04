# Classification (U)

"""Program:  root_run.py

    Description:  Unit testing of root_run in gen_libs.py.

    Usage:
        test/unit/gen_libs/root_run.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

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
        test_with_nonroot
        test_with_root

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    @mock.patch("gen_libs.os.geteuid")
    def test_with_nonroot(self, mock_root):

        """Function:  test_with_nonroot

        Description:  Test with non-root user.

        Arguments:

        """

        mock_root.return_value = 1

        self.assertFalse(gen_libs.root_run())

    @mock.patch("gen_libs.os.geteuid")
    def test_with_root(self, mock_root):

        """Function:  test_with_root

        Description:  Test with root user.

        Arguments:

        """

        mock_root.return_value = 0

        self.assertTrue(gen_libs.root_run())


if __name__ == "__main__":
    unittest.main()
