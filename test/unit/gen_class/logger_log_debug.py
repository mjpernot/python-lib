# Classification (U)

"""Program:  logger_log_debug.py

    Description:  Unit testing of Logger.log_debug in gen_class.py.

    Usage:
        test/unit/gen_class/logger_log_debug.py

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
        setUp
        test_default_setting
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Logger_log_debug_test"
        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_class/tmp/Logger_log_debug_test.txt")

    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="DEBUG")
        log_file.log_debug("TEST")

        with open(self.f_name, 'r') as fhdr:
            cnt = fhdr.read().count('DEBUG TEST')

        self.assertEqual(cnt, 1)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()
