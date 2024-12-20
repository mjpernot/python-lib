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
import unittest
import mock

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
        test_zero_one
        test_zero_percent
        test_fifty_percent
        test_hundred_percent

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

        bar1 = gen_class.ProgressBar(
            self.msg, self.width, self.progress_sym, self.empty_sym)

        self.assertFalse(bar1.calc_and_update(0, 1))

    @mock.patch("gen_class.ProgressBar.update")
    def test_zero_percent(self, mock_bar):

        """Function:  test_zero_percent

        Description:  Test calc_and_update method with zero percent completed.

        Arguments:

        """

        mock_bar.return_value = True

        bar1 = gen_class.ProgressBar(
            self.msg, self.width, self.progress_sym, self.empty_sym)

        self.assertFalse(bar1.calc_and_update(0, 100))

    @mock.patch("gen_class.ProgressBar.update")
    def test_fifty_percent(self, mock_bar):

        """Function:  test_fifty_percent

        Description:  Test calc_and_update method with 50 percent completed.

        Arguments:

        """

        mock_bar.return_value = True

        bar1 = gen_class.ProgressBar(
            self.msg, self.width, self.progress_sym, self.empty_sym)

        self.assertFalse(bar1.calc_and_update(50, 100))

    @mock.patch("gen_class.ProgressBar.update")
    def test_hundred_percent(self, mock_bar):

        """Function:  test_hundred_percent

        Description:  Test calc_and_update method with 100 percent completed.

        Arguments:

        """

        mock_bar.return_value = True

        bar1 = gen_class.ProgressBar(
            self.msg, self.width, self.progress_sym, self.empty_sym)

        self.assertFalse(bar1.calc_and_update(100, 100))


if __name__ == "__main__":
    unittest.main()
