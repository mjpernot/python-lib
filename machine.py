# Classification (U)

"""Program:  machine.py

    Description:  Base class for all machines.  This class has the methods for
        accomplishing tasks on different o/s platforms.

    Classes:
        Machine
            Linux
            Solaris

"""

# Libraries and Global Variables
from __future__ import absolute_import

# Standard

# Local
try:
    from . import version
except (ValueError, ImportError) as err:
    msg = err.args
    if msg[0] == "Attempted relative import in non-package" or \
       msg[0] == "attempted relative import with no known parent package":
        import version

__version__ = version.__version__


class Machine(object):

    """Class:  Machine

    Description:  Base class for all machines.

    Methods:
        __init__ -> Class instance initilization.

    """

    pass


class Linux(Machine):

    """Class:  Linux

    Description:  Class with methods and attributes for Linux operating system.

    Methods:
        __init__ -> Class instance initilization.

    """

    defaults_file = "/etc/my.cnf"

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the Linux class.

        Arguments:

        """

        pass
