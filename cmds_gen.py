# Classification (U)

"""Program:  cmds_gen.py

    Description:  Library of general function calls that can be used by
        different classes.  These methods are general use and can be used by a
        variety of classes as long as they follow the same standard.

    Functions:
        add_cmd
        create_cfg_array
        disconnect
        get_sub
        is_add_cmd

"""

# Libraries and Global Variables

# Standard

# Local
import version

__version__ = version.__version__


def add_cmd(cmd, **kwargs):

    """Function:  add_cmd

    Description:  Append name of argument and possibly value for the argument
        to the command line list array.

    Arguments:
        (input) cmd -> List array containing the program setup.
        (input) **kwargs:
            arg -> Name of argument being added.
            val -> Value for argument being added.
        (output) cmd -> List array containing the program setup.

    """

    cmd = list(cmd)

    # Append before returning, appending on return does not make the change.
    if "val" in kwargs:
        cmd.append(kwargs["arg"] + kwargs["val"])

    else:
        cmd.append(kwargs["arg"])

    return cmd


def is_add_cmd(args_array, cmd, opt_arg_list):

    """Function:  is_add_cmd

    Description:  Determine if any additional options need to be added to the
        command line.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) cmd -> List array containing the program arguments.
        (input) opt_arg_list -> Dictionary of additional options.
        (output) cmd -> List array containing the program arguments.

    """

    cmd = list(cmd)
    args_array = dict(args_array)
    opt_arg_list = dict(opt_arg_list)

    for opt in opt_arg_list:

        # Is option in array and is set to True.
        if opt in args_array and args_array[opt] \
           and isinstance(args_array[opt], bool):

            if isinstance(opt_arg_list[opt], list):

                for item in opt_arg_list[opt]:
                    cmd = add_cmd(cmd, arg=item)

            else:
                cmd = add_cmd(cmd, arg=opt_arg_list[opt])

        elif opt in args_array:
            cmd = add_cmd(cmd, arg=opt_arg_list[opt], val=args_array[opt])

    return cmd
