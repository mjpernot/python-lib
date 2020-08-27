#!/usr/bin/python
# Classification (U)

"""Program:  system_init.py

    Description:  Unit testing of System.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/system_init.py

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
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.host_name = "hostname"
        self.host = "host"

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        system = gen_class.System(self.host, self.host_name)

        self.assertEqual((system.host_name, system.host),
                         (self.host_name, self.host))


if __name__ == "__main__":
    unittest.main()
