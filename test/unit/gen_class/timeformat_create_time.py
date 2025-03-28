# Classification (U)

"""Program:  timeformat_create_time.py

    Description:  Unit testing of TimeFormat.create_time in gen_class.py.

    Usage:
        test/unit/gen_class/timeformat_create_time.py

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
        test_rdtg
        test_msecs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.tform = gen_class.TimeFormat()

    def test_rdtg(self):

        """Function:  test_rdtg

        Description:  Test the rdtg attribute.

        Arguments:

        """

        self.tform.create_time()

        self.assertTrue(self.tform.rdtg)

    def test_msecs(self):

        """Function:  test_msecs

        Description:  Test the msecs attribute.

        Arguments:

        """

        self.tform.create_time()

        self.assertTrue(self.tform.msecs)


if __name__ == "__main__":
    unittest.main()
