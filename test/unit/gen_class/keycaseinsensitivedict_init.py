# Classification (U)

"""Program:  keycaseinsensitivedict_init.py

    Description:  Unit testing of keycaseinsensitivedict.__init__ in
        gen_class.py.

    Usage:
        test/unit/gen_class/keycaseinsensitivedict_init.py

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
        test_base
        test_empty_dict
        test_data_dict

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cidict = gen_class.KeyCaseInsensitiveDict()

    def test_base(self):

        """Function:  test_base

        Description:  Test base class of init.

        Arguments:

        """

        self.assertTrue(
            isinstance(self.cidict, gen_class.KeyCaseInsensitiveDict))

    def test_empty_dict(self):

        """Function:  test_packages

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.assertEqual(self.cidict, dict())

    def test_data_dict(self):

        """Function:  test_data_dict

        Description:  Test with data in dictionary.

        Arguments:

        """

        data = {"This": "Is", "A": "Test"}
        results = {"this": "Is", "a": "Test"}
        cidict = gen_class.KeyCaseInsensitiveDict(data)

        self.assertEqual(cidict, results)


if __name__ == "__main__":
    unittest.main()
