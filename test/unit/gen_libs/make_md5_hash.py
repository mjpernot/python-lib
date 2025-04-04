# Classification (U)

"""Program:  make_md5_hash.py

    Description:  Unit testing of make_md5_hash in gen_libs.py.

    Usage:
        test/unit/gen_libs/make_md5_hash.py

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


class SubProcess3():                                    # pylint:disable=R0903

    """Class:  SubProcess3

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        communicate

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

    def communicate(self):

        """Method:  communicate

        Description:  Mock representation of subprocess.communicate method.

        Arguments:

        """

        return b"Hash_Results", True


class SubProcess():                                     # pylint:disable=R0903

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        communicate

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

    def communicate(self):

        """Method:  communicate

        Description:  Mock representation of subprocess.communicate method.

        Arguments:

        """

        return "Hash_Results", True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_tofile_false
        test_tofile_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.file_path = "/path/file.txt"
        self.to_file = False
        self.outfile = "/path/file.txt.md5.txt"
        self.results = "Hash_Results"

    @mock.patch("gen_libs.write_file")
    @mock.patch("gen_libs.subprocess.PIPE")
    @mock.patch("gen_libs.subprocess.Popen")
    def test_tofile_false(self, mock_popen, mock_pipe, mock_write):

        """Function:  test_tofile_false

        Description:  Test with to_file set to False.

        Arguments:

        """

        mock_popen.return_value = SubProcess3()
        mock_pipe.return_value = "Pipe_to_process"
        mock_write.return_value = True

        self.assertEqual(gen_libs.make_md5_hash(self.file_path, self.to_file),
                         self.results)

    @mock.patch("gen_libs.write_file")
    @mock.patch("gen_libs.subprocess.PIPE")
    @mock.patch("gen_libs.subprocess.Popen")
    def test_tofile_true(self, mock_popen, mock_pipe, mock_write):

        """Function:  test_tofile_true

        Description:  Test with to_file set to True.

        Arguments:

        """

        mock_popen.return_value = SubProcess3()
        mock_pipe.return_value = "Pipe_to_process"
        mock_write.return_value = True

        self.assertEqual(gen_libs.make_md5_hash(self.file_path), self.outfile)


if __name__ == "__main__":
    unittest.main()
