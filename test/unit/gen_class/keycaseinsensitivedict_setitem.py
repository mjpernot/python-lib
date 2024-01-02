# Classification (U)

"""Program:  keycaseinsensitivedict_setitem.py

    Description:  Unit testing of keycaseinsensitivedict.__setitem__ in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_setitem.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase key.

        Arguments:

        """

        self.cidict["and"] = "And"

        self.assertEqual(self.cidict, self.results)

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase key.

        Arguments:

        """

        self.cidict["And"] = "And"

        self.assertEqual(self.cidict, self.results)

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric key.

        Arguments:

        """

        self.cidict[4] = "Fourth"

        self.assertEqual(self.cidict, self.results2)


if __name__ == "__main__":
    unittest.main()
