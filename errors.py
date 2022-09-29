# Classification (U)

"""Program:  errors.py

    Description:  Base class for the server class exception errors.

    Classes:
        Error
            EmptyRowError
            NoOptionError
            SlaveNotRunningError
            NotMasterError
            NotSlaveError
            BadStatusVariableError

"""

# Libraries and Global Variables

# Standard

# Local
import version

__version__ = version.__version__


class Error(Exception):

    """Class:  Error

    Description:  Base class for all exceptions for general use.

    Methods:

    """

    pass


class EmptyRowError(Exception):

    """Class:  EmptyRowError

    Description:  Exception raised when attempting to fetch a key from an empty
        row.

    Methods:

    """

    pass


class NoOptionError(Exception):

    """Class:  NoOptionError

    Description:  Exception raised when a function does not find an option.

    Methods:

    """

    pass


class SlaveNotRunningError(Exception):

    """Class:  SlaveNotRunningError

    Description:  Exception raised when a slave is not running, but was
        expected to be running.

    Methods:

    """

    pass


class NotMasterError(Exception):

    """Class:  NotMasterError

    Description:  Exception raised when the server is not a master and the
        operation is illegal to run on a non-master.

    Methods:

    """

    pass


class NotSlaveError(Exception):

    """Class:  NotSlaveError

    Description:  Exception raised when the server is not a slave and the
        operation is illegal to run on a non-slave.

    Methods:

    """

    pass


class NotYetImplementedError(Exception):

    """Class:  NotYetImplementedError

    Description:  Exception raised when calling to a method that has not been
        finished.

    Methods:

    """

    pass
