# Classification (U)

"""Program:  keycaseinsensitivedict_has_key.py

    Description:  Unit testing of keycaseinsensitivedict.has_key in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_has_key.py

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
        test_lowercase2
        test_lowercase
        test_uppercase2
        test_uppercase
        test_numeric2
        test_numeric

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        data = {"This": "Is", "And": "Line", 4: "Fourth"}
        self.cidict = gen_class.KeyCaseInsensitiveDict(data)

    def test_lowercase2(self):

        """Function:  test_lowercase2

        Description:  Test with lowercase key.

        Arguments:

        """

        self.assertFalse(self.cidict.has_key("that"))

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase key.

        Arguments:

        """

        self.assertTrue(self.cidict.has_key("this"))

    def test_uppercase2(self):

        """Function:  test_uppercase2

        Description:  Test with uppercase key.

        Arguments:

        """

        self.assertFalse(self.cidict.has_key("THAT"))

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase key.

        Arguments:

        """

        self.assertTrue(self.cidict.has_key("THIS"))

    def test_numeric2(self):

        """Function:  test_numeric2

        Description:  Test with numeric key.

        Arguments:

        """

        self.assertFalse(self.cidict.has_key(5))

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric key.

        Arguments:

        """

        self.assertTrue(self.cidict.has_key(4))


if __name__ == "__main__":
    unittest.main()
