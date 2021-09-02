#!/usr/bin/python
# Classification (U)

"""Program:  make_md5_hash.py

    Description:  Unit testing of make_md5_hash in gen_libs.py.

    Usage:
        test/integration/gen_libs/make_md5_hash.py

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

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


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

        self.base_path = "test/integration/gen_libs/basefiles"
        self.file_path = os.path.join(self.base_path, "md5_file.txt")
        self.md5_file = os.path.join(self.base_path, "md5_file.txt.md5.txt")

    def test_tofile_false(self):

        """Function:  test_tofile_false

        Description:  Test with to_file set to False.

        Arguments:

        """

        data = gen_libs.make_md5_hash(self.file_path, to_file=False).split(" ")

        self.assertEqual(len(data), 1)

    def test_tofile_true(self):

        """Function:  test_tofile_true

        Description:  Test with to_file set to True.

        Arguments:

        """

        gen_libs.make_md5_hash(self.file_path)

        self.assertTrue(os.path.isfile(self.file_path))

        with open(self.md5_file) as fname:
            fcontent = fname.readlines()

        self.assertEqual(len(fcontent), 1)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.md5_file):
            os.remove(self.md5_file)


if __name__ == "__main__":
    unittest.main()
