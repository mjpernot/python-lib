#!/usr/bin/python
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

        bar = gen_class.ProgressBar(self.msg)

        self.assertEqual((bar.msg, bar.width, bar.progress_sym, bar.empty_sym),
                         (self.msg, self.width, self.progress_sym,
                          self.empty_sym))

    def test_user_values(self):

        """Function:  test_user_values

        Description:  Test __init__ method with user values for arguments.

        Arguments:

        """

        bar = gen_class.ProgressBar(self.msg, 30, "@", "#")

        self.assertEqual((bar.msg, bar.width, bar.progress_sym, bar.empty_sym),
                         (self.msg, 30, "@", "#"))

    def test_width_zero(self):

        """Function:  test_width_zero

        Description:  Test __init__ method with zero for width argument.

        Arguments:

        """

        bar = gen_class.ProgressBar(self.msg, 0)

        self.assertEqual((bar.msg, bar.width, bar.progress_sym, bar.empty_sym),
                         (self.msg, 20, self.progress_sym, self.empty_sym))

    def test_width_less_zero(self):

        """Function:  test_width_less_zero

        Description:  Test __init__ method with less than zero width argument.

        Arguments:

        """

        bar = gen_class.ProgressBar(self.msg, -10)

        self.assertEqual((bar.msg, bar.width, bar.progress_sym, bar.empty_sym),
                         (self.msg, 20, self.progress_sym, self.empty_sym))


if __name__ == "__main__":
    unittest.main()
