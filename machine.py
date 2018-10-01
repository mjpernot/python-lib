# Classification (U)

###############################################################################
#
# Filename:     machine.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               None
#
###############################################################################

"""Program:  machine.py

    Description:  Base class for all machines.  This class has the methods for
        accomplishing tasks on different o/s platforms.

    Classes:
        Machine
            Linux
            Solaris

"""

###############################################################################
# Libraries and Global Variables

# Standard

# Local
import version

# Version Information
__version__ = version.__version__


class Machine(object):

    """Class:  Machine

    Description:  Base class for all machines.

    Super-Class:  object

    Sub-Classes:
        Linux
        Solaris

    Methods:
        __init__ -> Class instance initilization.

    """

    pass


class Linux(Machine):

    """Class:  Linux

    Description:  Class with methods and attributes for Linux operating system.

    Super-Class:  Machine

    Sub-Classes:

    Methods:
        __init__ -> Class instance initilization.

    """

    defaults_file = "/opt/lampstack/mysql/my.cnf"

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the Linux class.

        Arguments:

        """

        pass


class Solaris(Machine):

    """Class:  Solaris

    Description:  Class with methods and attributes for Solaris operating
        system.

    Super-Class:  Machine

    Sub-Classes:

    Methods:
        __init__ -> Class instance initilization.

    """

    defaults_file = "None"

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the Solaris class.

        Arguments:

        """

        pass
