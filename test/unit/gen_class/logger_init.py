#!/usr/bin/python
# Classification (U)

"""Program:  logger_init.py

    Description:  Unit testing of Logger.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/logger_init.py

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
        test_mode_write
        test_mode_append
        test_mode_default
        test_critical_setting
        test_error_setting
        test_warning_setting
        test_debug_setting
        test_info_setting
        test_default_setting
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Logger_init_test"
        self.f_name = os.path.join(
            os.getcwd(), "test/unit/gen_class/tmp/Logger_init_test.txt")

    def test_mode_write(self):

        """Function:  test_mode_write

        Description:  Test with write mode setting.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, mode="w")

        self.assertTrue(log_file.handler)

    def test_mode_append(self):

        """Function:  test_mode_append

        Description:  Test with append mode setting.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, mode="a")

        self.assertTrue(log_file.handler)

    def test_mode_default(self):

        """Function:  test_mode_default

        Description:  Test with default mode setting.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name)

        self.assertTrue(log_file.handler)

    def test_critical_setting(self):

        """Function:  test_critical_setting

        Description:  Test with critical settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="CRITICAL")

        self.assertEqual(log_file.log.level, 50)

    def test_error_setting(self):

        """Function:  test_error_setting

        Description:  Test with error settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="ERROR")

        self.assertEqual(log_file.log.level, 40)

    def test_warning_setting(self):

        """Function:  test_warning_setting

        Description:  Test with warning settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="WARNING")

        self.assertEqual(log_file.log.level, 30)

    def test_debug_setting(self):

        """Function:  test_debug_setting

        Description:  Test with debug settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="DEBUG")

        self.assertEqual(log_file.log.level, 10)

    def test_info_setting(self):

        """Function:  test_info_setting

        Description:  Test with info settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name, level="INFO")

        self.assertEqual(log_file.log.level, 20)

    def test_default_setting(self):

        """Function:  test_default_setting

        Description:  Test with default settings.

        Arguments:

        """

        log_file = gen_class.Logger(self.name, self.f_name)

        self.assertEqual(log_file.log.level, 20)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        os.remove(self.f_name)


if __name__ == "__main__":
    unittest.main()
