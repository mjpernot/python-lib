#!/usr/bin/python
# Classification (U)

"""Program:  programlock_init.py

    Description:  Unit testing of ProgramLock.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/programlock_init.py

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
        setUp -> Initialize testing environment.
        test_default -> Test __init__ method with default arguments.
        test_flavor -> Test __init__ method with flavor argument.
        test_lock -> Test __init__ method with lock successful.
        tearDown -> Clean up of testing environment.

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
        self.lock_file = "-opt-local-python-ProgramLock_init-.lock"
        self.lock_file2 = "-opt-local-python-ProgramLock_init-TEST.lock"
        self.results = os.path.join(self.tmp_path, self.lock_file)
        self.results2 = os.path.join(self.tmp_path, self.lock_file2)

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_default(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.return_value = True
        mock_tmp.return_value = self.tmp_path

        self.lock = gen_class.ProgramLock(self.argv)

        self.assertEqual((self.lock.lock_created, self.lock.f_ptr,
                          self.lock.lock_file),
                         (True, self.f_ptr, self.results))

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_flavor(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_flavor

        Description:  Test __init__ method with flavor argument.

        Arguments:

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.return_value = True
        mock_tmp.return_value = self.tmp_path

        self.lock = gen_class.ProgramLock(self.argv, self.flavor_id)

        self.assertEqual((self.lock.lock_created, self.lock.f_ptr,
                          self.lock.lock_file),
                         (True, self.f_ptr, self.results2))

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_lock(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_lock

        Description:  Test __init__ method with lock successful.

        Arguments:

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.return_value = True
        mock_tmp.return_value = self.tmp_path

        self.lock = gen_class.ProgramLock(self.argv, self.flavor_id)

        self.assertEqual((self.lock.lock_created, self.lock.f_ptr,
                          self.lock.lock_file),
                         (True, self.f_ptr, self.results2))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
