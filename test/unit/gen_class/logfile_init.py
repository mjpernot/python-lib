#!/usr/bin/python
# Classification (U)

"""Program:  logfile_init.py

    Description:  Unit testing of LogFile.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_init.py

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

        pass

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        log = gen_class.LogFile()

        self.assertEqual((log.loglist, log.regex, log.marker, log.linemarker,
                          log.keyword, log.ignore),
                         ([], None, None, None, [], []))


if __name__ == "__main__":
    unittest.main()
