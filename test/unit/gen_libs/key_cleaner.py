# Classification (U)

"""Program:  key_cleaner.py

    Description:  Unit testing of key_cleaner in gen_libs.py.

    Usage:
        test/unit/gen_libs/key_cleaner.py

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
        test_key_single_level
        test_key_multi_level
        test_key_cleaner_multi_list
        test_key_cleaner_single_list
        test_key_cleaner_dict

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pre_value = "no.ne"
        self.post_value = "no.na"
        self.data = {self.pre_value: "value2"}
        self.data2 = [{self.pre_value: "value2"}]
        self.data3 = [{self.pre_value: "value2"}, {self.pre_value: "value2"}]
        self.data4 = {'heya': 'A', 'heyb': 'B', 'keyc': 'C', 'heyd': 'D'}
        self.data5 = {'heya': [{'heyb': 'B'}, {'keyc': 'C'}, {'heyd': 'D'}]}
        self.char = "e"
        self.repl = "a"
        self.results = {self.post_value: "value2"}
        self.results2 = [{self.post_value: "value2"}]
        self.results3 = [
            {self.post_value: "value2"}, {self.post_value: "value2"}]
        self.results4 = {'HEYa': 'A', 'HEYb': 'B', 'keyc': 'C', 'HEYd': 'D'}
        self.results5 = {'HEYa': [{'HEYb': 'B'}, {'keyc': 'C'}, {'HEYd': 'D'}]}

    def test_key_single_level(self):

        """Function:  test_key_single_level

        Description:  Test with dictionaries at single level.

        Arguments:

        """

        self.assertEqual(
            gen_libs.key_cleaner(self.data4, "hey", "HEY"), self.results4)

    def test_key_multi_level(self):

        """Function:  test_key_multi_level

        Description:  Test with dictionaries at multiple levels.

        Arguments:

        """

        self.assertEqual(
            gen_libs.key_cleaner(self.data5, "hey", "HEY"), self.results5)

    def test_key_cleaner_multi_list(self):

        """Function:  test_key_cleaner_multi_list

        Description:  Test with multiple item list passed.

        Arguments:

        """

        self.assertEqual(gen_libs.key_cleaner(self.data3, self.char,
                                              self.repl), self.results3)

    def test_key_cleaner_single_list(self):

        """Function:  test_key_cleaner_single_list

        Description:  Test with single item list passed.

        Arguments:

        """

        self.assertEqual(gen_libs.key_cleaner(self.data2, self.char,
                                              self.repl), self.results2)

    def test_key_cleaner_dict(self):

        """Function:  test_key_cleaner_dict

        Description:  Test with dictionary passed.

        Arguments:

        """

        self.assertEqual(gen_libs.key_cleaner(self.data, self.char, self.repl),
                         self.results)


if __name__ == "__main__":
    unittest.main()
