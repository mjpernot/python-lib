#!/usr/bin/python
# Classification (U)

"""Program:  progressbar_calc_and_update.py

    Description:  Unit testing of ProgressBar.calc_and_update in gen_class.py.

    Usage:
        test/unit/gen_class/progressbar_calc_and_update.py

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
import mock

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
        test_zero_one -> Test with zero and one arguments.
        test_zero_percent -> Test with zero percent completed.
        test_fifty_percent -> Test with 50 percent completed.
        test_hundred_percent -> Test with 100 percent completed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.msg = "TEST BAR"
        self.width = 20
        self.progress_sym = "#"
        self.empty_sym = " "

    @mock.patch("gen_class.ProgressBar.update")
    def test_zero_one(self, mock_bar):

        """Function:  test_zero_one

        Description:  Test calc_and_update method with zero and one arguments.

        Arguments:

        """

        mock_bar.return_value = True

        bar = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertFalse(bar.calc_and_update(0, 1))

    @mock.patch("gen_class.ProgressBar.update")
    def test_zero_percent(self, mock_bar):

        """Function:  test_zero_percent

        Description:  Test calc_and_update method with zero percent completed.

        Arguments:

        """

        mock_bar.return_value = True

        bar = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertFalse(bar.calc_and_update(0, 100))

    @mock.patch("gen_class.ProgressBar.update")
    def test_fifty_percent(self, mock_bar):

        """Function:  test_fifty_percent

        Description:  Test calc_and_update method with 50 percent completed.

        Arguments:

        """

        mock_bar.return_value = True

        bar = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertFalse(bar.calc_and_update(50, 100))

    @mock.patch("gen_class.ProgressBar.update")
    def test_hundred_percent(self, mock_bar):

        """Function:  test_hundred_percent

        Description:  Test calc_and_update method with 100 percent completed.

        Arguments:

        """

        mock_bar.return_value = True

        bar = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        self.assertFalse(bar.calc_and_update(100, 100))


if __name__ == "__main__":
    unittest.main()
