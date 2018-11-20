#!/usr/bin/python
# Classification (U)

"""Program:  ProgressBar_update.py

    Description:  Unit testing of ProgressBar.update in gen_class.py.

    Usage:
        test/unit/gen_class/ProgressBar_update.py

    Arguments:
        None

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
import gen_libs
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_zero_percent -> Test with zero percent completed.
        test_fifty_percent -> Test with 50 percent completed.
        test_hundred_percent -> Test with 100 percent completed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.msg = "TEST BAR"
        self.width = 20
        self.progress_sym = "#"
        self.empty_sym = " "

    def test_zero_percent(self):

        """Function:  test_zero_percent

        Description:  Test update method with zero percent completed.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(BAR.update(0))

    def test_fifty_percent(self):

        """Function:  test_fifty_percent

        Description:  Test update method with 50 percent completed.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(BAR.update(50))

    def test_hundred_percent(self):

        """Function:  test_hundred_percent

        Description:  Test update method with 100 percent completed.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(BAR.update(100))


if __name__ == "__main__":
    unittest.main()
