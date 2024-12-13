# Classification (U)

"""Program:  keycaseinsensitivedict_getitem.py

    Description:  Unit testing of keycaseinsensitivedict.__getitem__ in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_getitem.py

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
        test_lowercase
        test_uppercase
        test_numeric

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {"This": "Is", "A": "Test", "and": "line", 4: "Numeric"}
        self.cidict = gen_class.KeyCaseInsensitiveDict(self.data)
        self.results = "Is"
        self.results2 = "Numeric"

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase key.

        Arguments:

        """

        self.assertEqual(self.cidict["this"], self.results)

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase key.

        Arguments:

        """

        self.assertEqual(self.cidict["THIS"], self.results)

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric key.

        Arguments:

        """

        self.assertEqual(self.cidict[4], self.results2)


if __name__ == "__main__":
    unittest.main()
