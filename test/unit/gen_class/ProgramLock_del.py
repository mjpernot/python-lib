#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      ProgramLock_del.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_class       => 1.33.0 or higher
#
###############################################################################

"""Program:  ProgramLock_del.py

    Description:  Unit testing of ProgramLock.__del__ in gen_class.py.

    Usage:
        test/unit/gen_class/ProgramLock_del.py

    Arguments:
        None

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
import gen_class
import version

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_unlock -> Test __del__ method with unlock successful.
        test_no_file -> Test __del__ method with no file to unlink.
        test_no_lock -> Test __del__ method with lock set to false in class.
        tearDown -> Clean up of testing environment.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.test_path = os.path.join(os.getcwd(), "test/unit/gen_class")
        self.test_file = os.path.join(self.test_path, "test_file.txt")
        self.f_ptr = open(self.test_file, "w")

        self.argv = ["/opt/local/python/ProgramLock_init.py"]
        self.flavor_id = "TEST"
        self.LOCK = None

    @mock.patch("gen_class.os.unlink")
    @mock.patch("gen_class.os.path.isfile")
    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_unlock(self, mock_path, mock_open, mock_lock, mock_tmp, mock_file,
                    mock_link):

        """Function:  test_unlock

        Description:  Test __del__ method with unlock successful.

        Arguments:
            mock_path -> Mock Ref:  gen_class.os.path.abspath
            mock_open -> Mock Ref:  gen_class.open
            mock_lock -> Mock Ref:  gen_class.fcntl.lockf
            mock_tmp -> Mock Ref:  gen_class.tempfile.gettempdir
            mock_file -> Mock Ref:  gen_class.os.path.isfile
            mock_link -> Mock Ref:  gen_class.os.unlink

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.side_effect = [True, True]
        mock_tmp.return_value = "/tmp"
        mock_file.isfile.return_value = True
        mock_link.return_value = True

        self.LOCK = gen_class.ProgramLock(self.argv, self.flavor_id)

        del self.LOCK

        if hasattr(self, "LOCK"):
            status = True
        else:
            status = False

        self.assertFalse(status)

    @mock.patch("gen_class.os.path.isfile")
    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_no_file(self, mock_path, mock_open, mock_lock, mock_tmp,
                     mock_file):

        """Function:  test_no_file

        Description:  Test __del__ method with no file to unlink.

        Arguments:
            mock_path -> Mock Ref:  gen_class.os.path.abspath
            mock_open -> Mock Ref:  gen_class.open
            mock_lock -> Mock Ref:  gen_class.fcntl.lockf
            mock_tmp -> Mock Ref:  gen_class.tempfile.gettempdir
            mock_file -> Mock Ref:  gen_class.os.path.isfile

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.side_effect = [True, True]
        mock_tmp.return_value = "/tmp"
        mock_file.return_value = False

        self.LOCK = gen_class.ProgramLock(self.argv, self.flavor_id)

        del self.LOCK

        if hasattr(self, "LOCK"):
            status = True
        else:
            status = False

        self.assertFalse(status)

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_no_lock(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_no_lock

        Description:  Test __del__ method with lock set to false in class.

        Arguments:
            mock_path -> Mock Ref:  gen_class.os.path.abspath
            mock_open -> Mock Ref:  gen_class.open
            mock_lock -> Mock Ref:  gen_class.fcntl.lockf
            mock_tmp -> Mock Ref:  gen_class.tempfile.gettempdir

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.side_effect = [True, True]
        mock_tmp.return_value = "/tmp"

        self.LOCK = gen_class.ProgramLock(self.argv, self.flavor_id)

        self.LOCK.lock_created = False

        del self.LOCK

        if hasattr(self, "LOCK"):
            status = True
        else:
            status = False

        self.assertFalse(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:
            None

        """

        os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
