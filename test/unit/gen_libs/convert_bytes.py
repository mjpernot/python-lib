# Classification (U)

"""Program:  convert_bytes.py

    Description:  Unit testing of convert_bytes in gen_libs.py.

    Usage:
        test/unit/gen_libs/convert_bytes.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                                 # pylint:disable=E0401,C0413
import version                                  # pylint:disable=C0413,E0401

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_convert_dict
        test_convert_int
        test_convert_bytes
        test_convert_str

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = "Data String"
        self.data2 = b"Data String2"
        self.data3 = 1234
        self.data4 = {"key": "value"}
        self.results = b"Data String"
        self.results2 = b"Data String2"

    def test_convert_dict(self):

        """Function:  test_convert_dict

        Description:  Test with dictionary.

        Arguments:

        """

        self.assertIsNone(gen_libs.convert_bytes(self.data4))

    def test_convert_int(self):

        """Function:  test_convert_int

        Description:  Test with integer.

        Arguments:

        """

        self.assertIsNone(gen_libs.convert_bytes(self.data3))

    def test_convert_bytes(self):

        """Function:  test_convert_bytes

        Description:  Test with bytes.

        Arguments:

        """

        self.assertEqual(gen_libs.convert_bytes(self.data2), self.results2)

    def test_convert_str(self):

        """Function:  test_convert_str

        Description:  Test with a string.

        Arguments:

        """

        self.assertEqual(gen_libs.convert_bytes(self.data), self.results)


if __name__ == "__main__":
    unittest.main()
