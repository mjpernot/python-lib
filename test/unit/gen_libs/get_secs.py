# Classification (U)

"""Program:  get_secs.py

    Description:  Unit testing of get_secs in gen_libs.py.

    Usage:
        test/unit/gen_libs/get_secs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class TD():                                             # pylint:disable=R0903

    """Class:  TD

    Description:  Class is a representation of datetime delta class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Mail class.

        Arguments:

        """

        self.days = 10
        self.seconds = 2200


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_secs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.tdelta = TD()
        self.outsecs = 866200

    def test_get_secs(self):

        """Function:  test_get_secs

        Description:  Test get_secs function.

        Arguments:

        """

        self.assertEqual(gen_libs.get_secs(self.tdelta), self.outsecs)


if __name__ == "__main__":
    unittest.main()
