# Classification (U)

"""Program:  keycaseinsensitivedict_keylower.py

    Description:  Unit testing of keycaseinsensitivedict._keylower in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_keylower.py

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

        self.data = {"This": "Is", "A": "Test"}
        self.data2 = {"this": "Is", "a": "Test"}
        self.data3 = {1: "Is", 2: "Test"}
        self.results = {"this": "Is", "a": "Test"}
        self.results2 = {1: "Is", 2: "Test"}

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase data.

        Arguments:

        """

        cidict = gen_class.KeyCaseInsensitiveDict(self.data2)

        self.assertEqual(cidict, self.results)

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase data.

        Arguments:

        """

        cidict = gen_class.KeyCaseInsensitiveDict(self.data)

        self.assertEqual(cidict, self.results)

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric data.

        Arguments:

        """

        cidict = gen_class.KeyCaseInsensitiveDict(self.data3)

        self.assertEqual(cidict, self.results2)


if __name__ == "__main__":
    unittest.main()
