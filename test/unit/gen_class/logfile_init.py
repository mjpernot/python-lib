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
import unittest

# Local
sys.path.append(os.getcwd())
import gen_class                    # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

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
