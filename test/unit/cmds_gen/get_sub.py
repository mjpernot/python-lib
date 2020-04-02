#!/usr/bin/python
# Classification (U)

"""Program:  get_sub.py

    Description:  Unit testing of get_sub in cmds_gen.py.

    Usage:
        test/unit/cmds_gen/get_sub.py

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
import cmds_gen
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_get_sub -> Test returning command line.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class Sub(object):

            """Class:  Sub

            Description:  Class is a representation of a subprocess module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                pass

        self.subinst = Sub()
        self.results = Sub()

    def test_get_sub(self):

        """Function:  test_get_sub

        Description:  Test returning command line.

        Arguments:

        """

        self.assertEqual(
            type(cmds_gen.get_sub(self.subinst)), type(self.results))


if __name__ == "__main__":
    unittest.main()
