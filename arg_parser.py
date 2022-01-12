# Classification (U)

"""Program:  arg_parser.py

    Description:  A library program that contains a number of modules that
        parse the argument list on the command line.

    Functions:
        arg_add_def
        arg_cond_req
        arg_cond_req_or
        arg_default
        arg_dir_chk
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
        _make_dir
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


def arg_add_def(args_array, def_array=None, opt_req_list=None):

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

    args_array = dict(args_array)

    if def_array and opt_req_list:
        def_array = dict(def_array)
        opt_req_list = list(opt_req_list)

        # Add missing required options with default values to argument array.
        for item in set(opt_req_list) & \
                (set(def_array.keys()) - set(args_array.keys())):
            args_array[item] = def_array[item]

    elif def_array:
        def_array = dict(def_array)

        # Add all default values to argument array.
        for item in set(def_array.keys()) - set(args_array.keys()):
            args_array[item] = def_array[item]

    return args_array


def arg_cond_req(args_array, opt_con_req):

    """Function:  arg_cond_req

    Description:  This checks a dictionary list array for options that require
        other options to be included in the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_con_req -> Dictionary list containing the option as
            the dictionary key to a list of arguments that are required for the
            dictionary key option.
        (output) status -> True|False - If required args are included.

    """

    args_array = dict(args_array)
    opt_con_req = dict(opt_con_req)
    status = True

    for item in set(args_array.keys()) & set(opt_con_req.keys()):

        for _ in set(opt_con_req[item]) - set(args_array.keys()):
            status = False
            print("Error:  Option {0} requires options {1}.".
                  format(item, opt_con_req[item]))
            break

    return status


def arg_cond_req_or(args_array, opt_con_req_dict):

    """Function:  arg_cond_req_or

    Description:  Checks a dictionary list array for options that require one
        or more options to be included in the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_con_req_dict -> Dict of options that might be required.
        (output) status -> True|False - If options are the argument list.

    """

    args_array = dict(args_array)
    opt_con_req_dict = dict(opt_con_req_dict)
    status = True

    for item in set(opt_con_req_dict.keys()) & set(args_array.keys()):
        tmp_flag = False

        for _ in set(opt_con_req_dict[item]) & set(args_array.keys()):
            tmp_flag = True
            break

        if not tmp_flag:
            print("Error: Option {0} requires one of these options {1}".
                  format(item, opt_con_req_dict[item]))
            status = tmp_flag

    return status


def arg_default(arg, args_array, opt_def_dict):

    """Function:  arg_default

    Description:  Checks to see if an argument has a default value and if so
        assigns that value to the option in the args_array list.

    Note:  This function will overwrite an existing value for an argument if
        one is already present in the args_array dictionary.

    Arguments:
        (input) arg -> Argument option.
        (input) args_array -> Array of command line options and values.
        (input) opt_def_dict -> Dict with options and default values.
        (output) args_array -> Array of command line options and values.

    """

    args_array = dict(args_array)
    opt_def_dict = dict(opt_def_dict)

    if arg in opt_def_dict:
        args_array[arg] = opt_def_dict[arg]
        return args_array

    else:
        sys.exit("Error: Arg {0} missing value".format(arg))


def arg_dir_chk(args_array, dir_perms_chk):

    """Function:  arg_dir_chk

    Description:  Checks to see if the directory has the correct permissions.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) dir_chk_perms -> Options with their directory perms in octal.
        (output) status -> True|False - If directories have correct perms.

    """

    args_array = dict(args_array)
    dir_perms_chk = dict(dir_perms_chk)
    status = True

    for item in set(dir_perms_chk) & set(args_array):

        if not os.path.isdir(args_array[item]) or \
           not os.access(args_array[item], os.X_OK):
            print("Error: {0} does not exist or has permission denied.".format(
                args_array[item]))
            status = False

        if gen_libs.octal_to_str(dir_perms_chk[item])[0] == "r" and \
           not os.access(args_array[item], os.R_OK):
            print("Error: {0} is not readable.".format(args_array[item]))
            status = False

        if gen_libs.octal_to_str(dir_perms_chk[item])[1] == "w" and \
           not os.access(args_array[item], os.W_OK):
            print("Error: {0} is not writable.".format(args_array[item]))
            status = False

    return status


def arg_dir_chk_crt(args_array, dir_chk_list, dir_crt_list=None):

    """Function:  arg_dir_chk_crt

    Description:  Checks to see if the directory options have access to the
        directories and create directory if requested.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) dir_chk_list -> Options which will have directories.
        (input) dir_crt_list -> Options to create directories if not present.
        (output) status -> True|False - If directories are unavailable.

    """

    args_array = dict(args_array)
    dir_chk_list = list(dir_chk_list)
    status = False

    if dir_crt_list is None:
        dir_crt_list = []

    else:
        dir_crt_list = list(dir_crt_list)

    if set(dir_crt_list).issubset(set(dir_chk_list)):

        for item in set(dir_chk_list) & set(args_array.keys()):

            if not os.path.isdir(args_array[item]) and item in dir_crt_list:
                status = _make_dir(args_array[item], status)

            elif not os.path.isdir(args_array[item]):
                print("Error: {0} does not exist.".format(args_array[item]))
                status = True

            elif not os.access(args_array[item], os.W_OK):
                print("Error: {0} is not writable.".format(args_array[item]))
                status = True

    else:
        print("Error:  dir_crt_list: {0} is not a subset of dir_chk_list: {1}"
              .format(dir_crt_list, dir_chk_list))
        status = True

    return status


def arg_file_chk(args_array, file_chk_list, file_crt_list=None):

    """Function:  arg_file_chk

    Description:  Checks to see if the file options have access to the files.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) file_chk_list -> Options which will have files included.
        (input) file_crt_list -> Options require files to be created.
        (output) status -> True|False - If files are unavailable.

    """

    args_array = dict(args_array)
    file_chk_list = list(file_chk_list)

    if file_crt_list is None:
        file_crt_list = []

    else:
        file_crt_list = list(file_crt_list)

    status = False

    for item in set(args_array.keys()) & set(file_chk_list):

        if isinstance(args_array[item], list):
            tmp_list = list(args_array[item])

        else:
            tmp_list = [args_array[item]]

        for name in tmp_list:

            try:
                fname = open(name, "r")
                fname.close()

            except IOError as (errno, strerror):

                status = _file_create(name, item, file_crt_list, errno,
                                      strerror, status)

    return status


def arg_noreq_xor(args_array, xor_noreq):

    """Function:  arg_noreq_xor

    Description:  Does an XOR check between two options or if neither one is
        part of the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) xor_noreq -> Dictionary of the two XOR options.
        (output) status -> True|False - If only one option has been selected.

    """

    args_array = dict(args_array)
    xor_noreq = dict(xor_noreq)
    status = True

    for opt in xor_noreq:

        # Xor between key and values in dictionary.
        if not (operator.xor((opt in args_array),
                             (xor_noreq[opt] in args_array)) or
                (opt not in args_array and xor_noreq[opt] not in args_array)):

            print("Options: {0} or {1}, not both.".format(opt, xor_noreq[opt]))
            status = False

    return status


def arg_parse2(argv, opt_val_list, opt_def_dict=None, **kwargs):

    """Function:  arg_parse2

    Description:  Next version of arg_parse.  This version not only parses the
        command line arguments into an array, but includes an option for a
        dictionary which allows arguments to have default values if no value is
        passed with the argument.  It assumes anything not in opt_val_list
        array is valid and sets the option to True.

    Arguments:
        (input) argv -> Arguments from the command line.
        (input) opt_val_list -> Options which require values.
        (input) opt_def_dict -> Dict with options and default values.
        (input) **kwargs:
            multi_val - List of options that may contain multiple values
            opt_val - List of options that may allow 0 or 1 value for option.
        (output) args_array -> Array of command line options and values.

    """

    argv = list(argv)
    opt_val_list = list(opt_val_list)

    if opt_def_dict is None:
        opt_def_dict = {}

    else:
        opt_def_dict = dict(opt_def_dict)

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
        (output) status -> True|False - If required option is not listed.

    """

    args_array = dict(args_array)
    opt_req_list = list(opt_req_list)
    status = False

    for item in set(opt_req_list) - set(args_array.keys()):
        print("Error:  The '{0}' option is required".format(item))
        status = True

    return status


def arg_req_or_lst(args_array, opt_or_dict):

    """Function:  arg_req_or_lst

    Description:  Does a check on the dictionary list that requires the first
        option of the dictionary list to be in the argument list OR one or more
        of the options in the associated list to be in the argument list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_or_dict -> Dictionary list of options for OR.
        (output) status -> True|False - If requirements have been meet.

    """

    args_array = dict(args_array)
    opt_or_dict = dict(opt_or_dict)
    status = True

    for item in set(opt_or_dict.keys()) - set(args_array.keys()):
        tmp_flag = False

        for _ in set(opt_or_dict[item]) & set(args_array.keys()):
            tmp_flag = True
            break

        if not tmp_flag:
            print("Error:  Option: {0} or one of these: {1} is required.".
                  format(item, opt_or_dict[item]))
            status = tmp_flag

    return status


def arg_req_xor(args_array, opt_xor):

    """Function:  arg_req_xor

    Description:  Does an XOR check between two options.
        NOTE:  Does not handle multiple xor pairs.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_xor -> dict of options that are required XOR.
        (output) status -> True|False - If one option has been selected.

    """

    args_array = dict(args_array)
    opt_xor = dict(opt_xor)
    status = True

    for item in opt_xor:

        # Xor between key and values in dictionary.
        if not operator.xor((item in args_array),
                            (opt_xor[item] in args_array)):
            print("Option {0} or {1}, but not both.".format(item,
                                                            opt_xor[item]))
            status = False

    return status


def arg_set_path(args_array, arg_opt):

    """Function:  arg_set_path

    Description:  Return dir path from argument list or return empty string.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) arg_opt -> Argument option holding directory path.
        (output) Returns directory path or empty string.

    """

    args_array = dict(args_array)

    if arg_opt in args_array:
        return os.path.join(args_array[arg_opt], "")

    return ""


def arg_validate(args_array, valid_func):

    """Function:  arg_validate

    Description:  Validates data for certain options based on a dictionary
        list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) valid_func -> Dictionary list of options & functions.
        (output) status -> True|False - If format is valid.

    """

    args_array = dict(args_array)
    status = True

    for item in set(valid_func.keys()) & set(args_array.keys()):

        # Call function from function list.
        if not valid_func[item](args_array[item]):
            print("Error:  Invalid format: {0} '{1}'"
                  .format(item, args_array[item]))
            status = False

    return status


def arg_valid_val(args_array, opt_valid_val):

    """Function:  arg_valid_val

    Description:  Validates data for options based on a dictionary list.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_valid_val -> Dictionary of options & their valid values
        (output) status -> True|False - If format is valid.

    """

    args_array = dict(args_array)
    opt_valid_val = dict(opt_valid_val)
    status = True

    # Intersects the keys in args_array and opt_valid_val.
    for item in set(args_array.keys()) & set(opt_valid_val.keys()):

        # If passed value is valid for this option.
        if not args_array[item] in opt_valid_val[item]:
            print("Error:  Incorrect value ({0}) for option: {1}".
                  format(args_array[item], item))
            status = False

    return status


def arg_wildcard(args_array, opt_wildcard):

    """Function:  arg_wildcard

    Description:  Expand wildcard file argument and replace the wildcard value
        with a list of file names.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_wildcard -> List of wildcard options.
        (output) args_array -> Array of command line options and values.

    Example:
        Input:
            args_array = {"-a": ["cmds*", "arg*"], "-b": ["gen*"],
                          "-c": "*class*"}
            opt_wildcard = ["-a", "-b", "-c"]
        Output:
            {'-a': ['cmds_gen.py', 'arg_parser.py'], '-c': ['gen_class.py'],
             '-b': ['gen_libs.py', 'gen_class.py']}

    """

    args_array = dict(args_array)
    opt_wildcard = list(opt_wildcard)

    for opt in opt_wildcard:
        if opt in args_array.keys() and isinstance(args_array[opt], list):
            t_list = [glob.glob(item) for item in args_array[opt]]
            args_array[opt] = [item1 for item2 in t_list for item1 in item2]

        elif opt in args_array.keys() and isinstance(args_array[opt], str):
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
        (output) status -> True|False - If key or value is in args_array.

    """

    args_array = dict(args_array)
    opt_xor_dict = dict(opt_xor_dict)
    status = True

    for opt in set(opt_xor_dict.keys()) & set(args_array.keys()):

        for item in set(opt_xor_dict[opt]) & set(args_array.keys()):
            print("Option {0} or {1}, but not both.".format(opt, item))
            status = False
            break

    return status


def _file_create(name, option, file_crt_list, errno, strerror, status):

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
        (input) status -> Current status of file_crt_list function.
        (output) status -> True|False - If file creation fails.

    """

    file_crt_list = list(file_crt_list)

    if option in file_crt_list and errno == 2:

        try:
            fname = open(name, "w")
            fname.close()

        except IOError as (err, strerr):
            # Unable to create file.
            print("I/O Error: ({0}): {1}".format(err, strerr))
            print("Check option: '{0}', file: '{1}'".format(option, name))
            status = True

    # File not present.
    else:
        print("File Error: ({0}): {1}".format(errno, strerror))
        print("Check option: '{0}', file: '{1}'".format(option, name))
        status = True

    return status


def _make_dir(dirname, status):

    """Function:  _make_dir

    Description:  Tries to create a directory and capture any exceptions.

    NOTE:  Used by the arg_dir_chk_crt() to reduce the complexity rating.

    Arguments:
        (input) dirname -> Directory name.
        (input) status -> True|False - If directories are unavailable.
        (output) status -> True|False - If directories are unavailable.

    """

    try:
        os.makedirs(dirname)

    except OSError as (errno, strerr):
        if errno == 13 or errno == 17:
            print("Error:  {0} for {1}".format(strerr, dirname))
            status = True

        else:
            print("Error {0}:  Message:  {1} for {2}".format(
                errno, strerr, dirname))
            status = True

    return status


def _parse_multi(argv, args_array, opt_def_dict):

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
        cnt = 0
        tmp_argv = argv[1:]

        # Process values until next argument.
        while tmp_argv:
            if tmp_argv[0][0] == "-":
                break

            else:
                args_array[argv[0]].append(tmp_argv[0])

            cnt = cnt + 1
            tmp_argv = tmp_argv[1:]

        # Move to argument after the multiple values.
        argv = argv[cnt:]

    return argv, args_array


def _parse_single(argv, args_array, opt_def_dict, opt_val):

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
