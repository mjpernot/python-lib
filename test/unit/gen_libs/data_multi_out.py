#!/usr/bin/python
# Classification (U)

"""Program:  data_multi_out.py

    Description:  Unit testing of data_multi_out in gen_libs.py.

    Usage:
        test/unit/gen_libs/data_multi_out.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock
import json

# Local
sys.path.append(os.getcwd())
import gen_libs
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_data_is_dict -> Test data is a dictionary.
        test_data_is_not_dict -> Test data is not a dictionary.
        test_data_to_mail -> Test data is being converted to a Mail message.
        test_data_not_to_mail -> Test data is not converted to a Mail message.
        test_data_to_std -> Test data is sent to standard out.
        test_data_not_to_std -> Test data is being suppressed to standard out.
        test_data_nonjson_to_mail -> Test data is converted to a Mail message.
        test_data_json_to_mail -> Test json data to mail in correct format.
        test_data_not_to_file -> Test data is not being written to file.
        test_data_to_file -> Test data is being written to file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        class Mail(object):

            """Class:  Mail

            Description:  Class which is a representation of the Mail class.

            Super-Class:  object

            Sub-Classes:  None

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the Mail class.

                Arguments:
                        None

                """

                self.msg = ""

            def add_2_msg(self, txt_ln=None):

                """Method:  add_2_msg

                Description:  Add text to text string if data is present.

                Arguments:
                    (input) txt_ln -> Line of text to add to message.

                """

                if txt_ln:
                    self.msg = self.msg + txt_ln

        self.MAIL = Mail()

        self.data = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.mail_data = \
            '{\n    "a": 1, \n    "c": 3, \n    "b": 2, \n    "d": 4\n}'
        self.mail_data2 = \
            '{\n    "a": 1, \n    "c": 3, \n    "b": 2, \n    "d": 4\n}\n'
        self.err_msg = \
            "Error:  Unable to convert to JSON format, not a dictionary"
        self.data_list = ["a", 1, "b", 2, "c", 3, "d", 4]

    def test_data_to_file_error(self):

        """Function:  test_data_to_file_error

        Description:  Test data is not written to file due to error.

        Arguments:
            None

        """

        self.assertEqual(gen_libs.data_multi_out(self.data_list,
                                                 json_fmt=True,
                                                 o_file="File_Name",
                                                 sup_std=True),
                         (True, self.err_msg))

    @mock.patch("json.dump")
    def test_data_is_dict(self, mock_json):

        """Function:  test_data_is_dict

        Description:  Test data is a dictionary.

        Arguments:
            mock_json -> Mock Ref:  json.dump

        """

        mock_json.return_value = self.data

        with gen_libs.no_std_out():
            self.assertEqual(gen_libs.data_multi_out(self.data, json_fmt=True),
                             (False, None))

    def test_data_is_not_dict(self):

        """Function:  test_data_is_not_dict

        Description:  Test data is not a dictionary.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            self.assertEqual(gen_libs.data_multi_out("Test_String",
                                                     json_fmt=True),
                             (True, self.err_msg))

    @mock.patch("json.dump")
    def test_data_to_mail(self, mock_json):

        """Function:  test_data_to_mail

        Description:  Test data is being converted to a Mail message.

        Arguments:
            mock_json -> Mock Ref:  json.dump

        """

        mock_json.return_value = self.data

        with gen_libs.no_std_out():
            gen_libs.data_multi_out(self.data, json_fmt=True, MAIL=self.MAIL)

        self.assertEqual(self.MAIL.msg, self.mail_data)

    @mock.patch("json.dump")
    def test_data_not_to_mail(self, mock_json):

        """Function:  test_data_not_to_mail

        Description:  Test data is not being converted to a Mail message.

        Arguments:
            mock_json -> Mock Ref:  json.dump

        """

        mock_json.return_value = self.data

        with gen_libs.no_std_out():
            gen_libs.data_multi_out(self.data, json_fmt=True, MAIL=None)

        self.assertEqual(self.MAIL.msg, "")

    def test_data_to_std(self):

        """Function:  test_data_to_std

        Description:  Test data is sent to standard out.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            self.assertEqual(gen_libs.data_multi_out(self.data), (False, None))

    def test_data_not_to_std(self):

        """Function:  test_data_not_to_std

        Description:  Test data is being suppressed to standard out.

        Arguments:
            None

        """

        self.assertEqual(gen_libs.data_multi_out(self.data, sup_std=True),
                         (False, None))

    def test_data_nonjson_to_mail(self):

        """Function:  test_data_nonjson_to_mail

        Description:  Test data is being converted to a Mail message.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            gen_libs.data_multi_out(self.data, MAIL=self.MAIL)

        self.assertEqual(self.MAIL.msg, self.mail_data2)

    def test_data_json_to_mail(self):

        """Function:  test_data_json_to_mail

        Description:  Test json data going to mail in correct format.

        Arguments:
            None

        """

        with gen_libs.no_std_out():
            gen_libs.data_multi_out(self.data, json_fmt=True, MAIL=self.MAIL)

        self.assertEqual(self.MAIL.msg, self.mail_data)

    def test_data_not_to_file(self):

        """Function:  test_data_not_to_file

        Description:  Test data is not being written to file.

        Arguments:
            None

        """

        self.assertEqual(gen_libs.data_multi_out(self.data, o_file=None,
                                                 sup_std=True), (False, None))

    @mock.patch("gen_libs.write_file")
    def test_data_to_file(self, mock_write):

        """Function:  test_data_to_file

        Description:  Test data is being written to file.

        Arguments:
            mock_write -> Mock Ref:  gen_libs.write_file

        """

        mock_write.return_value = True

        self.assertEqual(gen_libs.data_multi_out(self.data, o_file="File_Name",
                                                 sup_std=True), (False, None))


if __name__ == "__main__":
    unittest.main()
