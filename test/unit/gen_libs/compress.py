# Classification (U)

"""Program:  compress.py

    Description:  Unit testing of compress in gen_libs.py.

    Usage:
        test/unit/gen_libs/compress.py

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


class SubProcess():                                     # pylint:disable=R0903

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        wait

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the subprocess class.

        Arguments:

        """

    def wait(self):

        """Method:  wait

        Description:  Mock representation of wait method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_compress

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "File_name"

    @mock.patch("gen_libs.subprocess.Popen")
    def test_compress(self, mock_popen):

        """Function:  test_compress

        Description:  Test test_compress function.

        Arguments:

        """

        mock_popen.return_value = SubProcess()

        self.assertFalse(gen_libs.compress(self.fname))


if __name__ == "__main__":
    unittest.main()
