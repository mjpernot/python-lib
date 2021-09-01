#!/usr/bin/python
# Classification (U)

"""Program:  programlock_del.py

    Description:  Unit testing of ProgramLock.__del__ in gen_class.py.

    Usage:
        test/unit/gen_class/programlock_del.py

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
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_unlock
        test_no_file
        test_no_lock
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.test_path = os.path.join(os.getcwd(), "test/unit/gen_class")
        self.test_file = os.path.join(self.test_path, "test_file.txt")
        self.f_ptr = open(self.test_file, "w")
        self.tmp_path = os.path.join("/", "tmp")
        self.argv = ["/opt/local/python/ProgramLock_init.py"]
        self.flavor_id = "TEST"
        self.lock = None

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

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.side_effect = [True, True]
        mock_tmp.return_value = self.tmp_path
        mock_file.isfile.return_value = True
        mock_link.return_value = True

        self.lock = gen_class.ProgramLock(self.argv, self.flavor_id)
        del self.lock

        self.assertFalse(hasattr(self, "LOCK"))

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

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.side_effect = [True, True]
        mock_tmp.return_value = self.tmp_path
        mock_file.return_value = False

        self.lock = gen_class.ProgramLock(self.argv, self.flavor_id)
        del self.lock

        self.assertFalse(hasattr(self, "LOCK"))

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_no_lock(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_no_lock

        Description:  Test __del__ method with lock set to false in class.

        Arguments:

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.side_effect = [True, True]
        mock_tmp.return_value = self.tmp_path

        self.lock = gen_class.ProgramLock(self.argv, self.flavor_id)
        self.lock.lock_created = False
        del self.lock

        self.assertFalse(hasattr(self, "LOCK"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
