#!/usr/bin/python
# Classification (U)

"""Program:  disk_usage.py

    Description:  Unit testing of disk_usage in gen_libs.py.

    Usage:
        test/unit/gen_libs/disk_usage.py

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
import collections
import mock

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


class Stat(object):

    """Class:  Stat

    Description:  Class is a representation of os.statvfs class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Mail class.

        Arguments:

        """

        self.f_bavail = 100
        self.f_frsize = 220
        self.f_blocks = 150
        self.f_bfree = 25


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_disk_usage

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.path = "/test/path"
        self.stat = Stat()

        _ntuple = collections.namedtuple("usage", "total used free")
        self.usage = _ntuple(33000, 27500, 22000)

    @mock.patch("gen_libs.os.statvfs")
    def test_disk_usage(self, mock_stat):

        """Function:  test_disk_usage

        Description:  Test disk_usage function.

        Arguments:

        """

        mock_stat.return_value = self.stat

        self.assertEqual(gen_libs.disk_usage(self.path), self.usage)


if __name__ == "__main__":
    unittest.main()
