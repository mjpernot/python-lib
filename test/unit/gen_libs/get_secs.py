#!/usr/bin/python
# Classification (U)

"""Program:  get_secs.py

    Description:  Unit testing of get_secs in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_secs.py

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


class TD(object):

    """Class:  TD

    Description:  Class is a representation of datetime delta class.

    Super-Class:  object

    Sub-Classes:  None

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Mail class.

        Arguments:
                None

        """

        self.days = 10
        self.seconds = 2200


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Unit testing initilization.
        test_get_secs -> Test get_secs function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.td = TD()
        self.outsecs = 866200

    def test_get_secs(self):

        """Function:  test_get_secs

        Description:  Test get_secs function.

        Arguments:

        """

        self.assertEqual(gen_libs.get_secs(self.td), self.outsecs)


if __name__ == "__main__":
    unittest.main()
