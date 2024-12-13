# Classification (U)

"""Program:  keycaseinsensitivedict_contains.py

    Description:  Unit testing of keycaseinsensitivedict.__contains__ in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_contains.py

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

        self.assertNotIn("that", self.cidict)

    def test_lowercase(self):

        """Function:  test_lowercase

        Description:  Test with lowercase key.

        Arguments:

        """

        self.assertIn("this", self.cidict)

    def test_uppercase2(self):

        """Function:  test_uppercase2

        Description:  Test with uppercase key.

        Arguments:

        """

        self.assertNotIn("THAT", self.cidict)

    def test_uppercase(self):

        """Function:  test_uppercase

        Description:  Test with uppercase key.

        Arguments:

        """

        self.assertIn("THIS", self.cidict)

    def test_numeric2(self):

        """Function:  test_numeric2

        Description:  Test with numeric key.

        Arguments:

        """

        self.assertNotIn(5, self.cidict)

    def test_numeric(self):

        """Function:  test_numeric

        Description:  Test with numeric key.

        Arguments:

        """

        self.assertIn(4, self.cidict)


if __name__ == "__main__":
    unittest.main()
