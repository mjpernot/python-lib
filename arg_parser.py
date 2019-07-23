# Classification (U)

"""Program:  arg_parser.py

    Description:  A library program that contains a number of modules that
        parse the argument list on the command line.

    Functions:
        arg_add_def
        arg_cond_req
        arg_cond_req_or
        arg_default
        arg_dir_chk_crt
        arg_file_chk
        arg_noreq_xor
        arg_parse2
        arg_require
        arg_req_or_lst
        arg_req_xor
        arg_set_path
        arg_validate
        arg_valid_val
        arg_wildcard
        arg_xor_dict
        _file_create
        _parse_multi
        _parse_single

"""

# Libraries and Global Variables

# Standard
import sys
import os
import operator
import glob

# Local
import gen_libs
import version

__version__ = version.__version__


def arg_add_def(args_array, def_array=None, opt_req_list=None, **kwargs):

    """Function:  arg_add_def

    Description:  Adds options along with their default values to the argument
        array if they are missing.  Can also add in the required argument list
        to the function call and this will add only those required argument
        options if they are missing and have default values in the default
        array list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) def_array -> List of options with their default values.
        (input) opt_req_list -> Options that are required.
        (output) args_array -> Array of command line options and values.

    """

    if def_array and opt_req_list:

        # Add missing required options with default values to argument array.
        for x in set(opt_req_list) & \
                (set(def_array.keys()) - set(args_array.keys())):
            args_array[x] = def_array[x]

    elif def_array:

        # Add all default values to argument array.
        for x in set(def_array.keys()) - set(args_array.keys()):
            args_array[x] = def_array[x]

    return args_array


def arg_cond_req(args_array, opt_con_req_list):

    """Function:  arg_cond_req

    Description:  This checks a dictionary list array for options that require
        other options to be included in the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_con_req_list -> Dictionary list containing the option as
            the dictionary key to a list of arguments that are required for the
            dictionary key option.
        (output) exit_flag -> True or false if args are included.

    """

    exit_flag = True

    for x in set(args_array.keys()) & set(opt_con_req_list.keys()):

        for y in set(opt_con_req_list[x]) - set(args_array.keys()):
            exit_flag = False
            print("Error:  Option {0} requires options {1}.".
                  format(x, opt_con_req_list[x]))
            break

    return exit_flag


def arg_cond_req_or(args_array, opt_con_req_dict):

    """Function:  arg_cond_req_or

    Description:  Checks a dictionary list array for options that require one
        or more options to be included in the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_con_req_dict -> List options that might be required.
        (output) or_flag -> True or False on the Or List selection.

    """

    or_flag = True
    for x in set(opt_con_req_dict.keys()) & set(args_array.keys()):
        tmp_flag = False

        for y in set(opt_con_req_dict[x]) & set(args_array.keys()):
            tmp_flag = True
            break

        if not tmp_flag:
            print("Error: Option {0} requires one of these options {1}".
                  format(x, opt_con_req_dict[x]))
            or_flag = tmp_flag

    return or_flag


def arg_default(arg, args_array, opt_def_dict, **kwargs):

    """Function:  arg_default

    Description:  Checks to see if an argument has a default value and if so
        assigns that value to the option in the args_array list.

    Arguments:
        (input) arg -> Argument option.
        (input) args_array -> Array of command line options and values.
        (input) opt_def_dict -> Dict with options and default values.
        (output) args_array -> Array of command line options and values.

    """

    if arg in opt_def_dict:
        args_array[arg] = opt_def_dict[arg]
        return args_array

    else:
        sys.exit("Error: Arg {0} missing value".format(arg))


def arg_dir_chk_crt(args_array, dir_chk_list, dir_crt_list=None):

    """Function:  arg_dir_chk_crt

    Description:  Checks to see if the directory options have access to the
        directories and create directory if requested.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) dir_chk_list -> Options which will have directories.
        (input) dir_crt_list -> Options to create directories if not present.
        (output) exit_flag -> If directories are unavailable.

    """

    if dir_crt_list is None:
        dir_crt_list = []

    exit_flag = False

    for x in set(dir_chk_list) & set(args_array.keys()):

        if not os.path.isdir(args_array[x]):

            if x in dir_crt_list:

                try:
                    os.makedirs(args_array[x])

                except:
                    print("Error:  Unable to create {0}".format(args_array[x]))
                    exit_flag = True

            else:
                print("Error:  {0} does not exist.".format(args_array[x]))
                exit_flag = True

        elif not os.access(args_array[x], os.W_OK) and x in dir_crt_list:
            print("Error: {0} is not writable.".format(args_array[x]))
            exit_flag = True

    return exit_flag


def arg_file_chk(args_array, file_chk_list, file_crt_list=None):

    """Function:  arg_file_chk

    Description:  Checks to see if the file options have access to the files.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) file_chk_list -> Options which will have files included.
        (input) file_crt_list -> Options require files to be created.
        (output) exit_flag -> If files are unavailable.

    """

    if file_crt_list is None:
        file_crt_list = []

    exit_flag = False

    for x in set(args_array.keys()) & set(file_chk_list):

        if isinstance(args_array[x], list):
            tmp_list = args_array[x]

        else:
            tmp_list = [args_array[x]]

        for name in tmp_list:

            try:
                fname = open(name, "r")
                fname.close()

            except IOError as (errno, strerror):

                exit_flag = _file_create(name, x, file_crt_list, errno,
                                         strerror, exit_flag)

    return exit_flag


def arg_noreq_xor(args_array, xor_noreq_list):

    """Function:  arg_noreq_xor

    Description:  Does an XOR check between two options or if neither one is
        part of the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) xor_noreq_list -> Dictionary of the two XOR options.
        (output) xor_flag -> True or false.

    """

    xor_flag = True
    for x in xor_noreq_list:

        # Xor between key and values in dictionary.
        if not (operator.xor((x in args_array),
                             (xor_noreq_list[x] in args_array)) or
                (x not in args_array and xor_noreq_list[x] not in args_array)):

            print("Options: {0} or {1}, not both.".format(x,
                                                          xor_noreq_list[x]))
            xor_flag = False

    return xor_flag


def arg_parse2(argv, opt_val_list, opt_def_dict=None, **kwargs):

    """Function:  arg_parse2

    Description:  Next version of arg_parse.  This version not only parses the
        command line arguments into an array, but includes an option for a
        dictionary which allows arguments to have default values if no value is
        passed with the argument.
        Additional notes on major changes:
            - Removed the opt_noval_list option, it assumes anything not in
                opt_val_list array is valid and sets the option to True.
            - Removed the exit_flag variable and instead uses the sys.exit
                command to exit the function and program.
            - Modified the opt_val_list array to have the "-" included with the
                option when checking for options in the argv command line.

    Arguments:
        (input) argv -> Arguments from the command line.
        (input) opt_val_list -> Options which require values.
        (input) opt_def_dict -> Dict with options and default values.
        (input) **kwargs:
            multi_val - List of options that may contain multiple values
            opt_val - List of options that may allow 0 or 1 value for option.
        (output) args_array -> Array of command line options and values.

    """

    if opt_def_dict is None:
        opt_def_dict = {}

    multi_list = list(kwargs.get("multi_val", []))
    opt_val = list(kwargs.get("opt_val", []))
    args_array = {}

    while argv:

        # Look for new option, always begin with "-".
        if argv[0][0] == "-":
            if argv[0] in multi_list:
                argv, args_array = _parse_multi(argv, args_array, opt_def_dict)

            elif argv[0] in opt_val_list or argv[0] in opt_val:
                argv, args_array = _parse_single(argv, args_array,
                                                 opt_def_dict, opt_val)

            else:
                args_array[argv[0]] = True

        argv = argv[1:]

    return args_array


def arg_require(args_array, opt_req_list):

    """Function:  arg_require

    Description:  Checks to see if the required options are included.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_req_list -> Options that are required.
        (output) exit_flag -> If required options not listed.

    """

    exit_flag = False

    for x in set(opt_req_list) - set(args_array.keys()):
        print("Error:  The '{0}' option is required".format(x))
        exit_flag = True

    return exit_flag


def arg_req_or_lst(args_array, opt_or_dict_list):

    """Function:  arg_req_or_lst

    Description:  Does a check on the dictionary list that requires the first
        option of the dictionary list to be in the argument list OR one or more
        of the options in the associated list to be in the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_or_dict_list -> Dictionary list of options for OR.
        (output) or_flag -> True or False on the Or List selection.

    """

    or_flag = True

    for x in set(opt_or_dict_list.keys()) - set(args_array.keys()):
        tmp_flag = False

        for y in set(opt_or_dict_list[x]) & set(args_array.keys()):
            tmp_flag = True
            break

        if not tmp_flag:
            print("Error:  Option: {0} or one of these: {1} is required.".
                  format(x, opt_or_dict_list[x]))
            or_flag = tmp_flag

    return or_flag


def arg_req_xor(args_array, opt_xor_list):

    """Function:  arg_req_xor

    Description:  Does an XOR check between two options.
        NOTE:  Does not handle multiple xor pairs.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_xor_list -> dict of options that are required XOR.
        (output) return -> True or false.

    """

    status_flag = True

    for x in opt_xor_list:

        # Xor between key and values in dictionary.
        if not operator.xor((x in args_array),
                            (opt_xor_list[x] in args_array)):
            print("Option {0} or {1}, but not both.".format(x,
                                                            opt_xor_list[x]))
            status_flag = False

    return status_flag


def arg_set_path(args_array, arg_opt):

    """Function:  arg_set_path

    Description:  Return dir path from argument list or return empty string.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) arg_opt -> Argument option holding directory path.
        (output) Directory path.

    """

    args_array = dict(args_array)

    if arg_opt in args_array:
        return args_array[arg_opt] + "/"

    else:
        return ""


def arg_validate(args_array, valid_func):

    """Function:  arg_validate

    Description:  Validates data for certain options based on a dictionary
        list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) valid_func -> Dictionary list of options & functions.
        (output) status_flag -> True or False on validity of data.

    """

    args_array = dict(args_array)
    status_flag = True

    for x in set(valid_func.keys()) & set(args_array.keys()):

        # Call function from function list.
        if not valid_func[x](args_array[x]):
            print("Error:  Invalid format: {0} '{1}'".format(x, args_array[x]))
            status_flag = False

    return status_flag


def arg_valid_val(args_array, opt_valid_val, **kwargs):

    """Function:  arg_valid_val

    Description:  Validates data for options based on a dictionary list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_valid_val -> Dictionary of options & their valid values
        (output) status_flag -> True or False on validity of data.

    """

    args_array = dict(args_array)
    opt_valid_val = dict(opt_valid_val)
    status_flag = True

    # Intersects the keys in args_array and opt_valid_val.
    for x in set(args_array.keys()) & set(opt_valid_val.keys()):

        # If passed value is valid for this option.
        if not args_array[x] in opt_valid_val[x]:
            print("Error:  Incorrect value ({0}) for option: {1}".
                  format(args_array[x], x))
            status_flag = False

    return status_flag


def arg_wildcard(args_array, opt_wildcard, **kwargs):

    """Function:  arg_wildcard

    Description:  Expand wildcard file argument and replace the wildcard value
        with a list of file names.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_wildcard -> List of wildcard options.
        (output) args_array -> Array of command line options and values.

    """

    args_array = dict(args_array)
    opt_wildcard = list(opt_wildcard)

    for opt in opt_wildcard:
        args_array[opt] = glob.glob(args_array[opt])

    return args_array


def arg_xor_dict(args_array, opt_xor_dict):

    """Function:  arg_xor_dict

    Description:  Does a Xor check between a key in opt_xor_dict and its values
        using args_array for the check.  Therefore, the key can be in
        args_array or one or more of its values can be in arg_array, but both
        can not appear in args_array.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_xor_dict -> Dictionary with key and values that will be xor
            with each other.
        (output) xor_flag -> True or False on validity of options.

    """

    args_array = dict(args_array)
    opt_xor_dict = dict(opt_xor_dict)
    xor_flag = True

    for x in set(opt_xor_dict.keys()) & set(args_array.keys()):

        for y in set(opt_xor_dict[x]) & set(args_array.keys()):
            print("Option {0} or {1}, but not both.".format(x, y))
            xor_flag = False
            break

    return xor_flag


def _file_create(name, option, file_crt_list, errno, strerror, exit_flag,
                 **kwargs):

    """Function:  _file_create

    Description:  Used to create a file if in file_crt_list and previously
        determined was not present.

    NOTE:  Used by the arg_file_chk() to reduce the complexity rating.

    Arguments:
        (input) name -> File path and name.
        (input) option -> Option being checked.
        (input) file_crt_list -> Options that require files to be created.
        (input) errno -> Current error status from file_crt_list function.
        (input) strerror -> Current error message from file_crt_list function.
        (input) exit_flag -> Current status of file_crt_list function.
        (output) exit_flag -> True|False - if file creation fails.

    """

    file_crt_list = list(file_crt_list)

    if option in file_crt_list and errno == 2:

        try:
            fname = open(name, "w")
            fname.close()

        except IOError as (errno, strerror):
            # Unable to create file.
            print("I/O Error: ({0}): {1}".format(errno, strerror))
            print("Check option: '{0}', file: '{1}'".format(option, name))
            exit_flag = True

    # File not present.
    else:
        print("I/O Error: ({0}): {1}".format(errno, strerror))
        print("Check option: '{0}', file: '{1}'".format(option, name))
        exit_flag = True

    return exit_flag


def _parse_multi(argv, args_array, opt_def_dict, **kwargs):

    """Function:  _parse_multi

    Description:  Processes a multi-value argument in command line
        arguments.  Modifys the args_array by adding a dictionary key and a
        list of values.

    NOTE:  Used by the arg_parse2() to reduce the complexity rating.

    Arguments:
        (input) argv -> Arguments from the command line.
        (input) args_array -> Array of command line options and values.
        (input) opt_def_dict -> Dict with options and default values.
        (output) argv -> Arguments from the command line.
        (output) args_array -> Array of command line options and values.

    """

    argv = list(argv)
    args_array = dict(args_array)
    opt_def_dict = dict(opt_def_dict)

    # If no value in argv for option and it's not an integer.
    if len(argv) < 2 or (argv[1][0] == "-" and not gen_libs.chk_int(argv[1])):

        # See if default value is available for argument.
        args_array = arg_default(argv[0], args_array, opt_def_dict)

    else:
        # Handle multiple values for argument.
        args_array[argv[0]] = []
        x = 0
        tmp_argv = argv[1:]

        # Process values until next argument.
        while tmp_argv:
            if tmp_argv[0][0] == "-":
                break

            else:
                args_array[argv[0]].append(tmp_argv[0])

            x = x + 1
            tmp_argv = tmp_argv[1:]

        # Move to argument after the multiple values.
        argv = argv[x:]

    return argv, args_array


def _parse_single(argv, args_array, opt_def_dict, opt_val, **kwargs):

    """Function:  _parse_single

    Description:  Processes a single-value argument in command line
        arguments.  Modifys the args_array by adding a dictionary key and a
        value.

    NOTE:  Used by the arg_parse2() to reduce the complexity rating.

    Arguments:
        (input) argv -> Arguments from the command line.
        (input) args_array -> Array of command line options and values.
        (input) opt_def_dict -> Dict with options and default values.
        (input) opt_val -> List of options allow None or 1 value for option.
        (output) argv -> Arguments from the command line.
        (output) args_array -> Array of command line options and values.

    """

    argv = list(argv)
    args_array = dict(args_array)
    opt_def_dict = dict(opt_def_dict)
    opt_val = list(opt_val)

    # If no value in argv for option and it is not an integer.
    if len(argv) < 2 or (argv[1][0] == "-" and not gen_libs.chk_int(argv[1])):
        if argv[0] in opt_val:
            args_array[argv[0]] = None

        else:
            # See if default value is available for argument.
            args_array = arg_default(argv[0], args_array, opt_def_dict)

    else:
        args_array[argv[0]] = argv[1]
        argv = argv[1:]

    return argv, args_array
