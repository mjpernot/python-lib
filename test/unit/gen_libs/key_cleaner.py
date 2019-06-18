#!/usr/bin/python
# Classification (U)

"""Program:  key_cleaner.py

    Description:  Unit testing of key_cleaner in gen_libs.py.

    Usage:
        test/unit/gen_libs/key_cleaner.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_key_cleaner -> Test key_cleaner function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {"no.ne": "value2"}
        self.char = "e"
        self.repl = "a"
        self.results = {"no.na": "value2"}

    def test_key_cleaner(self):

        """Function:  test_key_cleaner

        Description:  Test key_cleaner function.

        Arguments:

        """

        self.assertEqual(gen_libs.key_cleaner(self.data, self.char, self.repl),
                         self.results)


if __name__ == "__main__":
    unittest.main()
