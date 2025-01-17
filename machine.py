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

# Standard

# Local
try:
    from . import version

except (ValueError, ImportError) as err:
    import version

__version__ = version.__version__


class Machine():                                    # pylint:disable=R0903

    """Class:  Machine

    Description:  Base class for all machines.

    Methods:
        __init__ -> Class instance initilization.

    """

    pass                                            # pylint:disable=W0107


class Linux(Machine):                               # pylint:disable=R0903

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

        pass                                        # pylint:disable=W0107
