#!/usr/bin/python
# Classification (U)

"""Program:  system_set_host_name.py

    Description:  Unit testing of System.set_host_name in gen_class.py.

    Usage:
        test/unit/gen_class/system_set_host_name.py

    Arguments:

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
        test_server_call
        test_manual

    """

    def setUp(self):

        """Function:  setUp

        Description:  set_host_nameialization for unit testing.

        Arguments:

        """

        self.host_name = "hostname"
        self.host_name2 = "hostname2"
        self.host = "host"

    @mock.patch("gen_class.socket.gethostname")
    def test_server_call(self, mock_socket):

        """Function:  test_server_call

        Description:  Test with setting hostname with server call.

        Arguments:

        """

        mock_socket.return_value = self.host_name2

        system = gen_class.System(self.host, self.host_name)
        system.set_host_name()

        self.assertEqual((system.host_name, system.host),
                         (self.host_name2, self.host))

    def test_manual(self):

        """Function:  test_manual

        Description:  Test with setting host manually.

        Arguments:

        """

        system = gen_class.System(self.host, self.host_name)
        system.set_host_name(self.host_name2)

        self.assertEqual((system.host_name, system.host),
                         (self.host_name2, self.host))


if __name__ == "__main__":
    unittest.main()
