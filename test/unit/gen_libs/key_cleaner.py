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
        test_key_cleaner_tuple
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
        self.data4 = ({self.pre_value: "value2"}, {self.pre_value: "value2"})
        self.char = "e"
        self.repl = "a"
        self.results = {self.post_value: "value2"}
        self.results2 = [{self.post_value: "value2"}]
        self.results3 = [{self.post_value: "value2"},
                         {self.post_value: "value2"}]
        self.results4 = ({self.pre_value: "value2"},
                         {self.pre_value: "value2"})

    @unittest.skip("Error:  Unable to handle tuple.")
    def test_key_cleaner_tuple(self):

        """Function:  test_key_cleaner_tuple

        Description:  Test with tuple passed.

        Arguments:

        """

        self.assertEqual(gen_libs.key_cleaner(self.data4, self.char,
                                              self.repl), self.results4)

    @unittest.skip("Error:  Unable to handle multiple item list.")
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
