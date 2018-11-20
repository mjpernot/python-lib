# Classification (U)

"""Program:  cmds_gen.py

    Description:  Library of general function calls that can be used by
        different classes.  These methods are general use and can be used by a
        variety of classes as long as they follow the same standard.

    Functions:
        add_cmd
        create_cfg_array
        disconnect
        is_add_cmd
        run_prog

"""

# Libraries and Global Variables

# Standard
import os
import subprocess

# Local
import version

# Version
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

    # Append before returning, appending on return does not make the change.
    if "val" in kwargs:
        cmd.append(kwargs["arg"] + kwargs["val"])

    else:
        cmd.append(kwargs["arg"])

    return cmd


def create_cfg_array(cfg_file, **kwargs):

    """Function:  create_cfg_array

    Description:  Parses a configuration file which can contain multiple
        configuration connections & creates an array of configurations.  This
        is for general class use and will require the first line of the
        configuration file to be the "user" entry and the key and the value
        will be delimited by "=" (equal sign).

    Arguments:
        (input) cfg_file -> Configuration file.
        (input) **kwargs:
            cfg_path - Configuration directory path.
        (output) cfg_array -> Array of configurations.

    """

    cfg_array = []
    cfg_dict = {}

    cfg_path = kwargs.get("cfg_path", "./")

    # Does config file exists in current location.
    if os.path.isfile(cfg_file):
        fname = open(cfg_file, "r")

    else:
        fname = open(os.path.join(cfg_path, cfg_file), "r")

    for line in fname:

        # Ignore comment lines.
        if line[0] != "#":
            key, value = line.split("=")

            # Set each entry in the config to it's own array based on 'user'.
            # If the key is "user" (new slave) and config dictionary exist.
            if key.strip() == "user" and cfg_dict:

                cfg_array.append(cfg_dict)
                cfg_dict = {}

            cfg_dict[key.strip()] = value.strip().rstrip()

    # Execute after 'for' loop.
    else:
        # Add last dict to config array.
        cfg_array.append(cfg_dict)

    fname.close()

    return cfg_array


def disconnect(*args):

    """Function:  disconnect

    Description:  Disconnects a class database connection.  Will check to see
        if an argument is an array; if so will loop on the array to disconnect
        all connections.  Will require a disconnect method within the class.
        The disconnect method will be particular to that class.

    Arguments:
        (input) *arg -> One or more connection instances.

    """

    for x in args:

        if isinstance(x, list):
            for y in x:
                y.disconnect()

        else:
            x.disconnect()


def is_add_cmd(args_array, cmd, opt_arg_list, **kwargs):

    """Function:  is_add_cmd

    Description:  Determine if any additional options need to be added to the
        command line.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) cmd -> List array containing the program arguments.
        (input) opt_arg_list -> Dictionary of additional options.
        (input) **kwargs:
            None
        (output) cmd -> List array containing the program arguments.

    """

    for x in opt_arg_list:

        # Is option in array and is set to True.
        if x in args_array and args_array[x] and isinstance(args_array[x],
                                                            bool):

            if isinstance(opt_arg_list[x], list):

                for y in opt_arg_list[x]:
                    cmd = add_cmd(cmd, arg=y)

            else:
                cmd = add_cmd(cmd, arg=opt_arg_list[x])

        elif x in args_array:
            cmd = add_cmd(cmd, arg=opt_arg_list[x], val=args_array[x])

    return cmd


def run_prog(cmd, **kwargs):

    """Function:  run_prog

    Description:  Opens a system call to run the program command and write the
        output as specified in **kwargs or standard out.

    Arguments:
        (input) cmd -> List array holding program command line.
        (input) **kwargs:
            ofile -> Name of file to write output to.
            retdata -> True|False - Return output to calling function.

    """

    # Write to file.
    if kwargs.get("ofile", False):
        with open(kwargs["ofile"], "wb") as f_name:
            P1 = subprocess.Popen(cmd, stdout=f_name)
            P1.wait()

    # Return data to calling function.
    elif kwargs.get("retdata", False):
        P1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = P1.communicate()

        return out

    # Write to standard out.
    else:
        P1 = subprocess.Popen(cmd)
        P1.wait()
