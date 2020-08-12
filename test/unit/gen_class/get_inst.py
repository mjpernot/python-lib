#!/usr/bin/python
# Classification (U)

"""Program:  get_inst.py

    Description:  Unit testing of get_inst in gen_class.py.

    Usage:
        test/unit/gen_class/get_inst.py

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

# Local
sys.path.append(os.getcwd())
import gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_get_inst -> Test returning command line.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class ModInst(object):

            """Class:  ModInst

            Description:  Class is a representation of a module instance.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the class.

                Arguments:

                """

                pass

        self.modinst = ModInst()
        self.results = ModInst()

    def test_get_inst(self):

        """Function:  test_get_inst

        Description:  Test returning command line.

        Arguments:

        """

        self.assertEqual(
            type(gen_class.get_inst(self.modinst)), type(self.results))


if __name__ == "__main__":
    unittest.main()
