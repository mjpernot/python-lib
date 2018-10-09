#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      ProgramLock_init.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_class       => 1.33.0 or higher
#
###############################################################################

"""Program:  ProgramLock_init.py

    Description:  Unit testing of ProgramLock.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/ProgramLock_init.py

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
        test_default -> Test __init__ method with default arguments.
        test_flavor -> Test __init__ method with flavor argument.
        test_lock -> Test __init__ method with lock successful.
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

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_default(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:
            mock_path -> Mock Ref:  gen_class.os.path.abspath
            mock_open -> Mock Ref:  gen_class.open
            mock_lock -> Mock Ref:  gen_class.fcntl.lockf
            mock_tmp -> Mock Ref:  gen_class.tempfile.gettempdir

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.return_value = True
        mock_tmp.return_value = "/tmp"

        self.LOCK = gen_class.ProgramLock(self.argv)

        self.assertEqual((self.LOCK.lock_created, self.LOCK.f_ptr,
                          self.LOCK.lock_file),
                         (True, self.f_ptr,
                          "/tmp/-opt-local-python-ProgramLock_init-.lock"))

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_flavor(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_flavor

        Description:  Test __init__ method with flavor argument.

        Arguments:
            mock_path -> Mock Ref:  gen_class.os.path.abspath
            mock_open -> Mock Ref:  gen_class.open
            mock_lock -> Mock Ref:  gen_class.fcntl.lockf
            mock_tmp -> Mock Ref:  gen_class.tempfile.gettempdir

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.return_value = True
        mock_tmp.return_value = "/tmp"

        self.LOCK = gen_class.ProgramLock(self.argv, self.flavor_id)

        self.assertEqual((self.LOCK.lock_created, self.LOCK.f_ptr,
                          self.LOCK.lock_file),
                         (True, self.f_ptr,
                          "/tmp/-opt-local-python-ProgramLock_init-TEST.lock"))

    @mock.patch("gen_class.tempfile.gettempdir")
    @mock.patch("gen_class.fcntl.lockf")
    @mock.patch("gen_class.open")
    @mock.patch("gen_class.os.path.abspath")
    def test_lock(self, mock_path, mock_open, mock_lock, mock_tmp):

        """Function:  test_lock

        Description:  Test __init__ method with lock successful.

        Arguments:
            mock_path -> Mock Ref:  gen_class.os.path.abspath
            mock_open -> Mock Ref:  gen_class.open
            mock_lock -> Mock Ref:  gen_class.fcntl.lockf
            mock_tmp -> Mock Ref:  gen_class.tempfile.gettempdir

        """

        mock_path.return_value = self.argv[0]
        mock_open.return_value = self.f_ptr
        mock_lock.return_value = True
        mock_tmp.return_value = "/tmp"

        self.LOCK = gen_class.ProgramLock(self.argv, self.flavor_id)

        self.assertEqual((self.LOCK.lock_created, self.LOCK.f_ptr,
                          self.LOCK.lock_file),
                         (True, self.f_ptr,
                          "/tmp/-opt-local-python-ProgramLock_init-TEST.lock"))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:
            None

        """

        os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()