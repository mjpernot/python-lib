#!/usr/bin/python
# Classification (U)

"""Program:  ProgressBar_init.py

    Description:  Unit testing of ProgressBar.__init__ in gen_class.py.

    Usage:
        test/unit/gen_class/ProgressBar_init.py

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
        test_default -> Test with minimum number of arguments.
        test_user_values -> Test with user values for arguments.
        test_width_zero -> Test with zero width argument.
        test_width_less_zero -> Test with less than zero width argument.

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

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg)

        self.assertEqual((BAR.msg, BAR.width, BAR.progress_sym, BAR.empty_sym),
                         (self.msg, self.width, self.progress_sym,
                          self.empty_sym))

    def test_user_values(self):

        """Function:  test_user_values

        Description:  Test __init__ method with user values for arguments.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg, 30, "@", "#")

        self.assertEqual((BAR.msg, BAR.width, BAR.progress_sym, BAR.empty_sym),
                         (self.msg, 30, "@", "#"))

    def test_width_zero(self):

        """Function:  test_width_zero

        Description:  Test __init__ method with zero for width argument.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg, 0)

        self.assertEqual((BAR.msg, BAR.width, BAR.progress_sym, BAR.empty_sym),
                         (self.msg, 20, self.progress_sym, self.empty_sym))

    def test_width_less_zero(self):

        """Function:  test_width_less_zero

        Description:  Test __init__ method with less than zero width argument.

        Arguments:
            None

        """

        BAR = gen_class.ProgressBar(self.msg, -10)

        self.assertEqual((BAR.msg, BAR.width, BAR.progress_sym, BAR.empty_sym),
                         (self.msg, 20, self.progress_sym, self.empty_sym))


if __name__ == "__main__":
    unittest.main()
