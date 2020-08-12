#!/usr/bin/python
# Classification (U)

"""Program:  logfile_set_predicate.py

    Description:  Unit testing of LogFile.set_predicate in gen_class.py.

    Usage:
        test/unit/gen_class/logfile_set_predicate.py

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
        test_set_predicate_invalid -> Test with invalid value.
        test_set_predicate_all -> Test with with all value.
        test_set_predicate_any -> Test with with any value.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    def test_set_predicate_invalid(self):

        """Function:  test_set_predicate_invalid

        Description:  Test with invalid value.

        Arguments:

        """

        log = gen_class.LogFile()
        log.set_predicate("invalid")

        self.assertEqual(log.predicate, any)

    def test_set_predicate_all(self):

        """Function:  test_set_predicate_all

        Description:  Test with with all value.

        Arguments:

        """

        log = gen_class.LogFile()
        log.set_predicate("and")

        self.assertEqual(log.predicate, all)

    def test_set_predicate_any(self):

        """Function:  test_set_predicate_any

        Description:  Test with with any value.

        Arguments:

        """

        log = gen_class.LogFile()
        log.set_predicate("or")

        self.assertEqual(log.predicate, any)


if __name__ == "__main__":
    unittest.main()
