#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class SubProcess(object):

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

        pass

    def wait(self):

        """Method:  wait

        Description:  Mock representation of wait method.

        Arguments:

        """

        pass


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
