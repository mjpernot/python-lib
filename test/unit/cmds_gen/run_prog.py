#!/usr/bin/python
# Classification (U)

"""Program:  run_prog.py

    Description:  Unit testing of run_prog in cmds_gen.py.

    Usage:
        test/unit/cmds_gen/run_prog.py

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
import cmds_gen
import version

__version__ = version.__version__


class SubProcess(object):

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__ -> Initialize configuration environment.
        communicate -> Mock representation of subprocess.communicate method.
        wait -> Mock representation of subprocess.wait method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

        pass

    def communicate(self):

        """Method:  communicate

        Description:  Mock representation of subprocess.communicate method.

        Arguments:

        """

        return "Data", True

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_other_option -> Test with other option selected.
        test_retdata_option -> Test with retdata option selected.
        test_file_option -> Test with file option selected.
        taerDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cmd = "testme"
        self.fname = "./test/unit/cmds_gen/tmp/test_run_prog"
        self.retdata = True
        self.return_data = "Data"

    @mock.patch("gen_libs.subprocess.Popen")
    def test_other_option(self, mock_open):

        """Function:  test_other_option

        Description:  Test with other option selected.

        Arguments:

        """

        mock_open.return_value = SubProcess()

        self.assertFalse(cmds_gen.run_prog(self.cmd))

    @mock.patch("gen_libs.subprocess.PIPE")
    @mock.patch("gen_libs.subprocess.Popen")
    def test_retdata_option(self, mock_open, mock_pipe):

        """Function:  test_retdata_option

        Description:  Test with retdata option selected.

        Arguments:

        """

        mock_open.return_value = SubProcess()
        mock_pipe.return_value = "Pipe_to_process"

        self.assertEqual(cmds_gen.run_prog(self.cmd, retdata=self.retdata),
                         self.return_data)

    @mock.patch("gen_libs.subprocess.Popen")
    def test_file_option(self, mock_open):

        """Function:  test_file_option

        Description:  Test with file option selected.

        Arguments:

        """

        mock_open.return_value = SubProcess()

        self.assertFalse(cmds_gen.run_prog(self.cmd, ofile=self.fname))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.fname):
            os.remove(self.fname)


if __name__ == "__main__":
    unittest.main()
