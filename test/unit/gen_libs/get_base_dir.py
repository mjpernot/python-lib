#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      get_base_dir.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_libs        => v1.32.0 or higher
#
###############################################################################

"""Program:  get_base_dir.py

    Description:  Unit testing of get_base_dir in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_base_dir.py

    Arguments:
        None

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

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_get_base_dir -> Test with current program path.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.cur_path = os.path.dirname(os.path.realpath(__file__))

    def test_get_base_dir(self):

        """Function:  test_get_base_dir

        Description:  Test get_base_dir function with 0 pattern found.

        Arguments:
            None

        """

        self.assertEqual(gen_libs.get_base_dir(sys.argv[0]), self.cur_path)


if __name__ == "__main__":
    unittest.main()