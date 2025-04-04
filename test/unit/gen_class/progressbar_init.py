# Classification (U)

"""Program:  progressbar_init.py

    Description:  Unit testing of ProgressBar.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/progressbar_init.py

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
        test_user_values
        test_width_zero
        test_width_less_zero

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

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg)

        self.assertEqual(
            (bar1.msg, bar1.width, bar1.progress_sym, bar1.empty_sym),
            (self.msg, self.width, self.progress_sym, self.empty_sym))

    def test_user_values(self):

        """Function:  test_user_values

        Description:  Test __init__ method with user values for arguments.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg, 30, "@", "#")

        self.assertEqual(
            (bar1.msg, bar1.width, bar1.progress_sym, bar1.empty_sym),
            (self.msg, 30, "@", "#"))

    def test_width_zero(self):

        """Function:  test_width_zero

        Description:  Test __init__ method with zero for width argument.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg, 0)

        self.assertEqual(
            (bar1.msg, bar1.width, bar1.progress_sym, bar1.empty_sym),
            (self.msg, 20, self.progress_sym, self.empty_sym))

    def test_width_less_zero(self):

        """Function:  test_width_less_zero

        Description:  Test __init__ method with less than zero width argument.

        Arguments:

        """

        bar1 = gen_class.ProgressBar(self.msg, -10)

        self.assertEqual(
            (bar1.msg, bar1.width, bar1.progress_sym, bar1.empty_sym),
            (self.msg, 20, self.progress_sym, self.empty_sym))


if __name__ == "__main__":
    unittest.main()
