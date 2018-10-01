#!/usr/bin/python
# Classification (U)

###############################################################################
#
# Program:      ProgressBar_calc_and_update.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               gen_class       => 1.33.0 or higher
#               gen_libs        => 1.33.0 or higher
#
###############################################################################

"""Program:  ProgressBar_calc_and_update.py

    Description:  Unit testing of ProgressBar.calc_and_update in gen_class.py.

    Usage:
        test/unit/gen_class/ProgressBar_calc_and_update.py

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
import mock

# Local
sys.path.append(os.getcwd())
import gen_class
import gen_libs
import version

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_zero_one -> Test with zero and one arguments.
        test_zero_percent -> Test with zero percent completed.
        test_fifty_percent -> Test with 50 percent completed.
        test_hundred_percent -> Test with 100 percent completed.
        tearDown -> Clean up of testing environment.

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

    @mock.patch("gen_class.ProgressBar")
    def test_zero_one(self, mock_bar):

        """Function:  test_zero_one

        Description:  Test calc_and_update method with zero and one arguments.

        Arguments:
            mock_bar -> Mock Ref:  gen_class.ProgressBar

        """

        mock_bar.update.return_value = True

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertTrue(BAR.calc_and_update(0, 1))

    @mock.patch("gen_class.ProgressBar")
    def test_zero_percent(self, mock_bar):

        """Function:  test_zero_percent

        Description:  Test calc_and_update method with zero percent completed.

        Arguments:
            mock_bar -> Mock Ref:  gen_class.ProgressBar

        """

        mock_bar.update.return_value = True

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertTrue(BAR.calc_and_update(0, 100))

    @mock.patch("gen_class.ProgressBar")
    def test_fifty_percent(self, mock_bar):

        """Function:  test_fifty_percent

        Description:  Test calc_and_update method with 50 percent completed.

        Arguments:
            mock_bar -> Mock Ref:  gen_class.ProgressBar

        """

        mock_bar.update.return_value = True

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertTrue(BAR.calc_and_update(50, 100))

    @mock.patch("gen_class.ProgressBar")
    def test_hundred_percent(self, mock_bar):

        """Function:  test_hundred_percent

        Description:  Test calc_and_update method with 100 percent completed.

        Arguments:
            mock_bar -> Mock Ref:  gen_class.ProgressBar

        """

        mock_bar.update.return_value = True

        BAR = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertTrue(BAR.calc_and_update(100, 100))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:
            None

        """

        BAR = None


if __name__ == "__main__":
    unittest.main()
