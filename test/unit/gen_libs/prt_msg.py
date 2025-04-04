# Classification (U)

"""Program:  prt_msg.py

    Description:  Unit testing of prt_msg in gen_libs.py.

    Usage:
        test/unit/gen_libs/prt_msg.py

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
        test_prt_msg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.hdr = "Print_Header"
        self.msg = "Print_Message"
        self.lvl = 0

    @mock.patch("gen_libs.prt_lvl")
    def test_prt_msg(self, mock_lvl):

        """Function:  test_prt_msg

        Description:  Test prt_msg function.

        Arguments:

        """

        mock_lvl.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.prt_msg(self.hdr, self.msg, self.lvl))


if __name__ == "__main__":
    unittest.main()
