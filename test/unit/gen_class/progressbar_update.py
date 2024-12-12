# Classification (U)

"""Program:  progressbar_update.py

    Description:  Unit testing of ProgressBar.update in gen_class.py.

    Usage:
        test/unit/gen_class/progressbar_update.py

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
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_message
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

    def test_no_message(self):

        """Function:  test_no_message

        Description:  Test with no message passed.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(None, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(bar1.update(50))

    def test_zero_percent(self):

        """Function:  test_zero_percent

        Description:  Test update method with zero percent completed.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(bar1.update(0))

    def test_fifty_percent(self):

        """Function:  test_fifty_percent

        Description:  Test update method with 50 percent completed.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(bar1.update(50))

    def test_hundred_percent(self):

        """Function:  test_hundred_percent

        Description:  Test update method with 100 percent completed.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg, self.width, self.progress_sym,
                                    self.empty_sym)

        with gen_libs.no_std_out():
            self.assertFalse(bar1.update(100))


if __name__ == "__main__":
    unittest.main()
