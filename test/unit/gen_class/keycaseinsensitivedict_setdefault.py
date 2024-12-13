# Classification (U)

"""Program:  keycaseinsensitivedict_setdefault.py

    Description:  Unit testing of keycaseinsensitivedict.setdefault in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_setdefault.py

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
        test_existing
        test_lowercase
        test_uppercase
        test_numeric

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        data = {"This": "Is"}
        self.cidict = gen_class.KeyCaseInsensitiveDict(data)
        self.results = {"this": "Is", "and": "And"}
        self.results2 = {"this": "Is", 4: "Fourth"}
        self.results3 = {"this": "Is"}

    def test_existing(self):

        """Function:  test_existing

        Description:  Test with existing key.

        Arguments:

        """

        self.cidict.setdefault("This", "And")

        self.assertEqual(self.cidict, self.results3)

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase key.

        Arguments:

        """

        self.cidict.setdefault("and", "And")

        self.assertEqual(self.cidict, self.results)

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase key.

        Arguments:

        """

        self.cidict.setdefault("And", "And")

        self.assertEqual(self.cidict, self.results)

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric key.

        Arguments:

        """

        self.cidict.setdefault(4, "Fourth")

        self.assertEqual(self.cidict, self.results2)


if __name__ == "__main__":
    unittest.main()
