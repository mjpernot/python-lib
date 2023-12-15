# Classification (U)

"""Program:  keycaseinsensitivedict_update.py

    Description:  Unit testing of keycaseinsensitivedict.update in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_update.py

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
        test_new_multiple_entries
        test_new_entry
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

        data = {"This": "Is", "and": "And", 4: "Fourth"}
        self.cidict = gen_class.KeyCaseInsensitiveDict(data)
        self.results = {"this": "Is", "and": "And2", 4: "Fourth"}
        self.results2 = {"this": "Is", "and": "And", 4: "Fourth2"}
        self.results3 = {
            "this": "Is", "and": "And", 4: "Fourth", "another": "Line"}
        self.results4 = {
            "this": "Is", "and": "And", 4: "Fourth", "another": "Line",
            "last": "Test"}

    def test_new_multiple_entries(self):

        """Function:  test_new_multiple_entries

        Description:  Test with updating with multiple new keys.

        Arguments:

        """

        self.cidict.update({"Another": "Line", "Last": "Test"})

        self.assertEqual(self.cidict, self.results4)

    def test_new_entry(self):

        """Function:  test_new_entry

        Description:  Test with updating with new key.

        Arguments:

        """

        self.cidict.update({"Another": "Line"})

        self.assertEqual(self.cidict, self.results3)

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase key.

        Arguments:

        """

        self.cidict.update({"and": "And2"})

        self.assertEqual(self.cidict, self.results)

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase key.

        Arguments:

        """

        self.cidict.update({"AND": "And2"})

        self.assertEqual(self.cidict, self.results)

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric key.

        Arguments:

        """

        self.cidict.update({4: "Fourth2"})

        self.assertEqual(self.cidict, self.results2)


if __name__ == "__main__":
    unittest.main()
