#!/usr/bin/python
# Classification (U)

"""Program:  print_list.py

    Description:  Unit testing of print_list in gen_libs.py.

    Usage:
        test/unit/gen_libs/print_list.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import filecmp

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

__version__ = version.__version__


def linecnt(fname):

    """Function:  linecnt

    Description:  Count number of lines in a file.

    Arguments:
        (input) fname
        (output) Number of lines in the file.

    """

    return sum(1 for _ in open(fname))


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mode_a_empty6
        test_mode_a_empty5
        test_mode_a_empty4
        test_mode_a_empty3
        test_mode_a_empty2
        test_mode_a_empty
        test_mode_w_empty3 -> Test with write mode with empty list
        test_mode_w_empty2 -> Test with write mode with empty list
        test_mode_w_empty -> Test with write mode with empty list
        test_mode_a_passed3
        test_mode_a_passed2
        test_mode_a_passed
        test_mode_a_passed3
        test_mode_a_passed2
        test_mode_a_passed
        test_mode_w_default3
        test_mode_w_default2
        test_mode_w_default
        test_write_multi_file3
        test_write_multi_file2
        test_write_multi_file
        test_write_file3
        test_write_file2
        test_write_file
        test_std_out3
        test_std_out2
        test_std_out
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        base_path = "test/unit/gen_libs/testfiles"
        self.file = os.path.join(os.getcwd(), base_path, "print_list_file")
        self.res_file = os.path.join(os.getcwd(), base_path, "print_list_1")
        self.res_file2 = os.path.join(os.getcwd(), base_path, "print_list_2")
        self.res_file3 = os.path.join(os.getcwd(), base_path, "print_list_3")
        self.res_file4 = os.path.join(os.getcwd(), base_path, "print_list_4")
        self.mode = "a"
        self.mode2 = "w"
        self.data = ["First line of data"]
        self.data2 = ["First line of data", "Second line of data"]
        self.data3 = []

    def test_mode_a_empty6(self):

        """Function:  test_mode_a_empty6

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode)

        self.assertTrue(filecmp.cmp(self.file, self.res_file4))

    def test_mode_a_empty5(self):

        """Function:  test_mode_a_empty5

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode)

        self.assertEqual(linecnt(self.file), 0)

    def test_mode_a_empty4(self):

        """Function:  test_mode_a_empty4

        Description:  Test with append mode with empty list.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode)

        self.assertTrue(os.path.isfile(self.file))

    def test_mode_a_empty3(self):

        """Function:  test_mode_a_empty3

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode)

        self.assertTrue(filecmp.cmp(self.file, self.res_file2))

    def test_mode_a_empty2(self):

        """Function:  test_mode_a_empty2

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode)

        self.assertEqual(linecnt(self.file), 2)

    def test_mode_a_empty(self):

        """Function:  test_mode_a_empty

        Description:  Test with append mode with empty list.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode)

        self.assertTrue(os.path.isfile(self.file))

    def test_mode_w_empty3(self):

        """Function:  test_mode_w_empty3

        Description:  Test with write mode with empty list.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode2)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode2)

        self.assertTrue(filecmp.cmp(self.file, self.res_file4))

    def test_mode_w_empty2(self):

        """Function:  test_mode_w_empty2

        Description:  Test with write mode with empty list.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode2)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode2)

        self.assertEqual(linecnt(self.file), 0)

    def test_mode_w_empty(self):

        """Function:  test_mode_w_empty

        Description:  Test with write mode with empty list.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode2)
        gen_libs.print_list(self.data3, ofile=self.file, mode=self.mode2)

        self.assertTrue(os.path.isfile(self.file))

    def test_mode_a_passed3(self):

        """Function:  test_mode_a_passed3

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)

        self.assertTrue(filecmp.cmp(self.file, self.res_file3))

    def test_mode_a_passed2(self):

        """Function:  test_mode_a_passed2

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)

        self.assertEqual(linecnt(self.file), 4)

    def test_mode_a_passed(self):

        """Function:  test_mode_a_passed

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)
        gen_libs.print_list(self.data2, ofile=self.file, mode=self.mode)

        self.assertTrue(os.path.isfile(self.file))

    def test_mode_w_passed3(self):

        """Function:  test_mode_w_passed3

        Description:  Test with file mode of overwrite passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data, ofile=self.file, mode=self.mode2)
        gen_libs.print_list(self.data, ofile=self.file, mode=self.mode2)

        self.assertTrue(filecmp.cmp(self.file, self.res_file))

    def test_mode_w_passed2(self):

        """Function:  test_mode_w_passed2

        Description:  Test with file mode of overwrite passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data, ofile=self.file, mode=self.mode2)
        gen_libs.print_list(self.data, ofile=self.file, mode=self.mode2)

        self.assertEqual(linecnt(self.file), 1)

    def test_mode_w_passed(self):

        """Function:  test_mode_w_passed

        Description:  Test with file mode of overwrite passing mode.

        Arguments:

        """

        gen_libs.print_list(self.data, ofile=self.file, mode=self.mode2)
        gen_libs.print_list(self.data, ofile=self.file, mode=self.mode2)

        self.assertTrue(os.path.isfile(self.file))

    def test_mode_w_default3(self):

        """Function:  test_mode_w_default3

        Description:  Test with file mode of overwrite using default setting.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file)
        gen_libs.print_list(self.data2, ofile=self.file)

        self.assertTrue(filecmp.cmp(self.file, self.res_file2))

    def test_mode_w_default2(self):

        """Function:  test_mode_w_default2

        Description:  Test with file mode of overwrite using default setting.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file)
        gen_libs.print_list(self.data2, ofile=self.file)

        self.assertEqual(linecnt(self.file), 2)

    def test_mode_w_default(self):

        """Function:  test_mode_w_default

        Description:  Test with file mode of overwrite using default setting.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file)
        gen_libs.print_list(self.data2, ofile=self.file)

        self.assertTrue(os.path.isfile(self.file))

    def test_write_multi_file3(self):

        """Function:  test_write_multi_file3

        Description:  Test with writing multiple lines to file.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file)

        self.assertTrue(filecmp.cmp(self.file, self.res_file2))

    def test_write_multi_file2(self):

        """Function:  test_write_multi_file2

        Description:  Test with writing multiple lines to file.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file)

        self.assertEqual(linecnt(self.file), 2)

    def test_write_multi_file(self):

        """Function:  test_write_multi_file

        Description:  Test with writing multiple lines to file.

        Arguments:

        """

        gen_libs.print_list(self.data2, ofile=self.file)

        self.assertTrue(os.path.isfile(self.file))

    def test_write_file3(self):

        """Function:  test_write_file3

        Description:  Test with writing to file.

        Arguments:

        """

        gen_libs.print_list(self.data, ofile=self.file)

        self.assertTrue(filecmp.cmp(self.file, self.res_file))

    def test_write_file2(self):

        """Function:  test_write_file2

        Description:  Test with writing to file.

        Arguments:

        """

        gen_libs.print_list(self.data, ofile=self.file)

        self.assertEqual(linecnt(self.file), 1)

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test with writing to file.

        Arguments:

        """

        gen_libs.print_list(self.data, ofile=self.file)

        self.assertTrue(os.path.isfile(self.file))

    def test_std_out3(self):

        """Function:  test_std_out3

        Description:  Test with empty list.

        Arguments:

        """

        self.assertFalse(gen_libs.print_list(self.data3))

    def test_std_out2(self):

        """Function:  test_std_out2

        Description:  Test with printing multiple lines to standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.print_list(self.data2))

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test with printing to standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(gen_libs.print_list(self.data))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
