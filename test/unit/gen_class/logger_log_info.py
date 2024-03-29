# Classification (U)

"""Program:  logger_log_info.py

    Description:  Unit testing of Logger.log_info in gen_class.py.

    Usage:
        test/unit/gen_class/logger_log_info.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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

        self.name = "Logger_log_info_test"
        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_class/tmp/Logger_log_info_test.txt")

    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="INFO")
        log_file.log_info("TEST")

        with open(self.f_name, 'r') as fhdr:
            cnt = fhdr.read().count('INFO TEST')

        self.assertEqual(cnt, 1)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()
