# Classification (U)

"""Program:  is_base64.py

    Description:  Unit testing of is_base64 in pulled_search.py.

    Usage:
        test/unit/gen_libs/is_base64.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import gen_libs                     # pylint:disable=E0401,R0402,C0413
import version                      # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_with_int_data
        test_with_bytes_data5
        test_with_bytes_data4
        test_with_bytes_data3
        test_with_bytes_data2
        test_with_bytes_data
        test_with_str_data5
        test_with_str_data4
        test_with_str_data3
        test_with_str_data2
        test_with_str_data
        test_with_encoded_data

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = 'dGhpcyBpcyBhIHRlc3RhIG92ZXIgYW5kIG92ZXIxMjM0'
        self.data2 = 'this is a testa over and over'
        self.data3 = 'this is a testa over and over1'
        self.data4 = 'this is a testa over and over12'
        self.data5 = 'this is a testa over and over123'
        self.data6 = 'this is a testa over and over1234'

        self.bytes = bytes(self.data2, "utf-8")
        self.bytes2 = bytes(self.data3, "utf-8")
        self.bytes3 = bytes(self.data4, "utf-8")
        self.bytes4 = bytes(self.data5, "utf-8")
        self.bytes5 = bytes(self.data6, "utf-8")
        self.bytes6 = 12345

    def test_with_int_data(self):

        """Function:  test_with_int_data

        Description:  Test with integer data.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.bytes6))

    def test_with_bytes_data5(self):

        """Function:  test_with_bytes_data5

        Description:  Test with bytes data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.bytes5))

    def test_with_bytes_data4(self):

        """Function:  test_with_bytes_data4

        Description:  Test with bytes data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.bytes4))

    def test_with_bytes_data3(self):

        """Function:  test_with_bytes_data3

        Description:  Test with bytes data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.bytes3))

    def test_with_bytes_data2(self):

        """Function:  test_with_bytes_data2

        Description:  Test with bytes data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.bytes2))

    def test_with_bytes_data(self):

        """Function:  test_with_bytes_data

        Description:  Test with bytes data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.bytes))

    def test_with_str_data5(self):

        """Function:  test_with_str_data5

        Description:  Test with string data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.data6))

    def test_with_str_data4(self):

        """Function:  test_with_str_data4

        Description:  Test with string data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.data5))

    def test_with_str_data3(self):

        """Function:  test_with_str_data3

        Description:  Test with string data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.data4))

    def test_with_str_data2(self):

        """Function:  test_with_str_data2

        Description:  Test with string data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.data3))

    def test_with_str_data(self):

        """Function:  test_with_str_data

        Description:  Test with string data of different lengths.

        Arguments:

        """

        self.assertFalse(gen_libs.is_base64(self.data2))

    def test_with_encoded_data(self):

        """Function:  test_with_encoded_data

        Description:  Test with encoded data.

        Arguments:

        """

        self.assertTrue(gen_libs.is_base64(self.data))


if __name__ == "__main__":
    unittest.main()
