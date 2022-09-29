# Classification (U)

"""Program:  gen_class.py

    Description:  Class that has class definitions for general use.

    Function:
        get_inst
        setup_mail

    Classes:
        ArgParser
        Daemon
        LogFile
        ProgressBar
        SingleInstanceException
        ProgramLock
        System
            Mail
        TimeFormat
        Logger
        Yum

"""

# Libraries and Global Variables
from __future__ import print_function
from __future__ import absolute_import

# Standard
import sys
import os
import subprocess
import fcntl
import tempfile
import logging
import socket
import smtplib
import time
import atexit
import signal
import platform
import getpass
import operator
import glob
import datetime
import io

# Third-party
import gzip
import json
import re

# yum==3.4.3 does not work in Python 3
if sys.version_info < (3, 0):
    import yum

# Local
import gen_libs
import version

__version__ = version.__version__

# Global
MASK = "0"


def get_inst(cmd):

    """Function:  get_inst

    Description:  Returns the module instance header.

    Arguments:
        (input) cmd -> Module library.
        (output) -> Return module instance.

    """

    sub = cmd

    return sub


def setup_mail(to_line, subj=None, frm_line=None):

    """Function:  setup_mail

    Description:  Initialize a mail instance.  Provide 'from line' if one is
        not passed.

    Arguments:
        (input) to_line -> Mail to line.  Either a string or list.
        (input) subj -> Mail subject line.  Either a string or list.
        (input) frm_line -> Mail from line.
        (output) Mail instance.

    """

    if isinstance(to_line, list):
        to_line = list(to_line)

    if isinstance(subj, list):
        subj = list(subj)

    if not frm_line:
        frm_line = getpass.getuser() + "@" + socket.gethostname()

    return Mail(to_line, subj, frm_line)


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class which holds a parsed argument list and has a number of
        methods that parse the argument list from the command line.

    Note:  The ArgParser class was originally a set of libraries and were
        converted to this class.  Below is a mapping of the library
        variables to the class attributes.  There were a number of renames
        to simplfy the naming scheme and also resolve naming conflicts.  The
        mapping is broken out by the method they are used in.

        Method
            Old name            -> New name

        arg_parse2
            argv                -> argv
            args_array          -> args_array
            opt_val_list        -> opt_val
            opt_def_dict        -> opt_def
            multi_val           -> multi_val
            opt_val             -> opt_val_bin

        arg_add_def
            def_array           -> defaults
            opt_req_list        -> opt_req

        arg_cond_req
            opt_con_req         -> opt_con_req

        arg_cond_req_or
            opt_con_req_dict    -> opt_con_or

        arg_default
            opt_def_dict        -> opt_def
                Same as the arg_parse2.opt_def

        arg_dir_chk
            dir_perms_chk       -> dir_perms_chk

        arg_dir_chk_crt
            dir_chk_list        -> dir_chk
            dir_crt_list        -> dir_crt

        arg_dir_crt
            dir_perms_crt       -> dir_perms_crt

        arg_file_chk
            file_chk_list       -> file_chk
            file_crt_list       -> file_crt

        arg_noreq_xor
            xor_noreq           -> xor_noreq

        arg_require
            opt_req_list        -> opt_req
                Same as the arg_add_def.opt_req

        arg_req_or_lst
            opt_or_dict         -> opt_or

        arg_req_xor
            opt_xor             -> opt_xor

        arg_validate
            valid_func          -> valid_func

        arg_valid_val
            opt_valid_val       -> opt_valid_val

        opt_wildcard
            opt_wildcard        -> opt_wildcard

        arg_xor_dict
            opt_xor_dict        -> opt_xor_val

    Methods:
        __init__
        arg_add_def
        arg_cond_req
        arg_cond_req_or
        arg_default
        arg_dir_chk
        arg_dir_chk_crt
        arg_dir_crt
        arg_exist
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
        get_args
        get_args_keys
        get_val
        insert_arg
        parse_multi
        parse_single
        update_arg

    """

    def __init__(self, argv, opt_val=None, opt_def=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the ArgParser class.

        Arguments:
            (input) argv -> Arguments from the command line
            (input) opt_val -> Options which require values
            (input) opt_def -> Dict with options and default values
            (input) **kwargs:
                defaults -> List of options with their default values
                dir_chk -> Options which will have directories
                dir_crt -> Options to create directories if not present
                dir_perms_chk -> Directory check options with their directory
                    perms in octal
                dir_perms_crt -> Directory creation options with their
                    directory perms in octal
                file_perm_chk -> File check options with their perms in octal
                file_crt -> Options require files to be created
                multi_val - List of options that may contain multiple values
                opt_con_or -> Dictionary of options that require one or more
                    options
                opt_con_req -> Dictionary list containing the option as the
                    dictionary key to a list of arguments that are required for
                    the dictionary key option
                opt_or -> Dictionary list of options for "or" operator
                opt_req -> Options that are required
                opt_val_bin - List of options that allow zero values or one
                    value for the option
                opt_valid_val -> Dictionary of options & their valid values
                opt_wildcard -> List of wildcard options
                opt_xor -> Dictionary of options that are required XOR
                opt_xor_val -> Dictionary with key and values that will be xor
                    with each other
                valid_func -> Dictionary list of options & functions
                xor_noreq -> Dictionary of the two XOR options
                do_parse -> True|False - Run the arg_parse2 method during the
                    initialization process for the class.  Default is False.
                    NOTE:  If a parsing error occurs, only a print error
                        message will be displayed.  Not recommended for
                        automated job runs.

        """

        # For arg_parse2 and arg_default methods
        self.argv = list(argv)
        self.args_array = dict()
        self.opt_val = list() if opt_val is None else list(opt_val)
        self.opt_def = dict() if opt_def is None else dict(opt_def)
        self.multi_val = list(kwargs.get("multi_val", []))
        self.opt_val_bin = list(kwargs.get("opt_val_bin", []))

        # For arg_add def and arg_require methods
        self.defaults = dict(kwargs.get("defaults", {}))
        self.opt_req = list(kwargs.get("opt_req", []))

        # For arg_cond_req method
        self.opt_con_req = dict(kwargs.get("opt_con_req", {}))

        # For arg_cond_req_or method
        self.opt_con_or = dict(kwargs.get("opt_con_or", {}))

        # For arg_dir_chk method
        self.dir_perms_chk = dict(kwargs.get("dir_perms_chk", {}))

        # For arg_dir_chk_crt method
        self.dir_chk = list(kwargs.get("dir_chk", []))
        self.dir_crt = list(kwargs.get("dir_crt", []))

        # For arg_dir_crt method
        self.dir_perms_crt = dict(kwargs.get("dir_perms_crt", {}))

        # For arg_file_chk method
        self.file_perm_chk = dict(kwargs.get("file_perm_chk", {}))
        self.file_crt = list(kwargs.get("file_crt", []))

        # For arg_noreq_xor method
        self.xor_noreq = dict(kwargs.get("xor_noreq", {}))

        # For arg_req_or_lst method
        self.opt_or = dict(kwargs.get("opt_or", {}))

        # For arg_req_xor method
        self.opt_xor = dict(kwargs.get("opt_xor", {}))

        # For arg_validate method
        self.valid_func = dict(kwargs.get("valid_func", {}))

        # For arg_valid_val method
        self.opt_valid_val = dict(kwargs.get("opt_valid_val", {}))

        # For opt_wildcard method
        self.opt_wildcard = list(kwargs.get("opt_wildcard", []))

        # For arg_xor_dict method
        self.opt_xor_val = dict(kwargs.get("opt_xor_val", {}))

        if kwargs.get("do_parse", False) and not self.arg_parse2():
            print("Error:  An error occurred during the parsing of argv.")

    def arg_add_def(self, **kwargs):

        """Method:  arg_add_def

        Description:  Adds options along with their default values to the
            argument array if they are missing.  Can also add in the required
            argument list to the function call and this will add only those
            required argument options if they are missing and have default
            values in the default array list.

        Arguments:
            (input) **kwargs:
                defaults -> List of options with their default values
                opt_req -> Options that are required

        """

        defaults = dict(kwargs.get("defaults", self.defaults))
        opt_req = list(kwargs.get("opt_req", self.opt_req))

        if defaults and opt_req:

            # Add missing required options with default values to arg_array.
            for item in set(opt_req) & (
                    set(defaults.keys()) - set(self.args_array.keys())):

                self.args_array[item] = defaults[item]

        elif defaults:

            # Add any missing default values to arg_array.
            for item in set(defaults.keys()) - set(self.args_array.keys()):
                self.args_array[item] = defaults[item]

    def arg_cond_req(self, **kwargs):

        """Method:  arg_cond_req

        Description:  This checks a dictionary list array for options that
            require other options to be included in the argument list.

        Arguments:
            (input) **kwargs:
                opt_con_req -> Dictionary list containing the option as the
                    dictionary key to a list of arguments that are required for
                    the dictionary key option
            (output) status -> True|False - If required args are included

        """

        opt_con_req = dict(kwargs.get("opt_con_req", self.opt_con_req))
        status = True

        for item in set(self.args_array.keys()) & set(opt_con_req.keys()):

            for _ in set(opt_con_req[item]) - set(self.args_array.keys()):
                status = False
                print("Error:  Option {0} requires options {1}.".
                      format(item, opt_con_req[item]))
                break

        return status

    def arg_cond_req_or(self, **kwargs):

        """Method:  arg_cond_req_or

        Description:  Checks a dictionary list array for options that require
            one or more options to be included in the argument list.

        Arguments:
            (input) **kwargs:
                opt_con_or -> Dict of options that might be required
            (output) status -> True|False - If options are the argument list

        """

        opt_con_or = dict(kwargs.get("opt_con_or", self.opt_con_or))
        status = True

        for item in set(opt_con_or.keys()) & set(self.args_array.keys()):
            tmp_flag = False

            for _ in set(opt_con_or[item]) & set(self.args_array.keys()):
                tmp_flag = True
                break

            if not tmp_flag:
                print("Error: Option {0} requires one of these options {1}".
                      format(item, opt_con_or[item]))
                status = tmp_flag

        return status

    def arg_default(self, arg, **kwargs):

        """Method:  arg_default

        Description:  Checks to see if an argument has a default value and if
            so assigns that value to the option in the args_array list.

        Arguments:
            (input) arg -> Argument option.
            (input) **kwargs:
                opt_def -> Dict with options and default values
            (output) status -> True|False - If default was added successfully

        """

        opt_def = dict(kwargs.get("opt_def", self.opt_def))
        status = True

        if arg in opt_def and arg not in self.args_array:
            self.args_array[arg] = opt_def[arg]

        elif arg not in opt_def:
            print("Warning: Arg {0} missing default value".format(arg))
            status = False

        return status

    def arg_dir_chk(self, **kwargs):

        """Method:  arg_dir_chk

        Description:  Checks to see if the directory has the correct
            permissions.

        Arguments:
            (input) **kwargs:
                dir_perms_chk -> Directory check options with their directory
                    perms in octal
            (output) status -> True|False - If directories have correct perms

        """

        dir_perms_chk = dict(kwargs.get("dir_perms_chk", self.dir_perms_chk))
        status = True

        for item in set(dir_perms_chk) & set(self.args_array):

            if not os.path.isdir(self.args_array[item]):
                print("Error: {0} does not exist.".
                      format(self.args_array[item]))
                status = False

            else:
                status = status & gen_libs.chk_perm(
                    self.args_array[item], dir_perms_chk[item])

        return status

    def arg_dir_chk_crt(self, **kwargs):

        """Method:  arg_dir_chk_crt

        Description:  Checks to see if the directory options have access to the
            directories and create directory if requested.

        Arguments:
            (input) **kwargs:
                dir_chk -> Options which will have directories
                dir_crt -> Options to create directories if not present
            (output) status -> True|False - If directories are available

        """

        dir_chk = list(kwargs.get("dir_chk", self.dir_chk))
        dir_crt = list(kwargs.get("dir_crt", self.dir_crt))
        status = True

        if set(dir_crt).issubset(set(dir_chk)):

            for item in set(dir_chk) & set(self.args_array.keys()):

                if not os.path.isdir(self.args_array[item]) and \
                   item in dir_crt:

                    status = gen_libs.make_dir(self.args_array[item])

                elif not os.path.isdir(self.args_array[item]):
                    print("Error: {0} does not exist.".
                          format(self.args_array[item]))
                    status = False

                elif not os.access(self.args_array[item], os.W_OK):
                    print("Error: {0} is not writable.".
                          format(self.args_array[item]))
                    status = False

        else:
            print("Error:  dir_crt_list: {0} is not a subset of dir_chk: {1}"
                  .format(dir_crt, dir_chk))
            status = False

        return status

    def arg_dir_crt(self, **kwargs):

        """Method:  arg_dir_crt

        Description:  Creates a directory if it doesn't exist and also checks
            to see if the directory has the correct permissions.

        Arguments:
            (input) **kwargs:
                dir_perms_crt -> Directory creation options with their
                    directory perms in octal
            (output) status -> True|False - If directories have correct perms
                and/or was created successfully

        """

        dir_perms_crt = dict(kwargs.get("dir_perms_crt", self.dir_perms_crt))
        status = True

        for item in set(dir_perms_crt) & set(self.args_array.keys()):

            if not os.path.isdir(self.args_array[item]):
                tmp_status = gen_libs.make_dir(self.args_array[item])

            else:
                tmp_status = True

            if tmp_status:
                status = status & gen_libs.chk_perm(
                    self.args_array[item], dir_perms_crt[item])

            else:
                status = status & tmp_status
                print("Error: {0} was not created.".
                      format(self.args_array[item]))

        return status

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Checks to see if argument option exists in the arg_array.

        Arguments:
            (input) arg -> Argument option being checked
            (output) True|False - If argument exist

        """

        return True if arg in self.args_array else False

    def arg_file_chk(self, **kwargs):

        """Method:  arg_file_chk

        Description:  Checks to see if the file options have access to the
            files.

        Arguments:
            (input) **kwargs:
                file_perm_chk -> File check options with their perms in octal
                file_crt -> Options require files to be created
            (output) status -> True|False - If files are available

        """

        file_perm_chk = dict(kwargs.get("file_perm_chk", self.file_perm_chk))
        file_crt = list(kwargs.get("file_crt", self.file_crt))
        status = True

        for option in set(self.args_array) & set(file_perm_chk):
            f_list = list(self.args_array[option])             \
                if isinstance(self.args_array[option], list)   \
                else [self.args_array[option]]

            for fname in f_list:
                if os.path.isfile(fname):
                    status = status & gen_libs.chk_perm(
                        fname, file_perm_chk[option])

                elif option in file_crt:
                    try:
                        fhldr = open(fname, "w")
                        fhldr.close()

                    except IOError as err_msg:
                        (err, strerr) = err_msg.args
                        print("I/O Error: ({0}): {1}".format(err, strerr))
                        print("Option: '{0}' File: '{1}'".format(option,
                                                                 fname))
                        status = status & False

                else:
                    print("Error - File: '{0}' is missing.".format(fname))
                    status = status & False

        return status

    def arg_noreq_xor(self, **kwargs):

        """Method:  arg_noreq_xor

        Description:  Does an XOR check between two options or if neither one
            is part of the argument list.

        Arguments:
            (input) **kwargs:
                xor_noreq -> Dictionary of the two XOR options
            (output) status -> True|False - If only one option has been
                selected

        """

        xor_noreq = dict(kwargs.get("xor_noreq", self.xor_noreq))
        status = True

        for opt in xor_noreq:

            # Xor between key and values in dictionary.
            if not (operator.xor((opt in self.args_array),
                                 (xor_noreq[opt] in self.args_array)) or
                    (opt not in self.args_array and
                     xor_noreq[opt] not in self.args_array)):

                print("Options: {0} or {1}, not both.".
                      format(opt, xor_noreq[opt]))
                status = False

        return status

    def arg_parse2(self, **kwargs):

        """Method:  arg_parse2

        Description:  Parses the command line arguments into arg_array, but
            includes an option for a dictionary which allows arguments to have
            default values if no value is passed with the argument.  It assumes
            anything not in opt_val is valid and sets the option to True.

        Arguments:
            (input) **kwargs:
                opt_val -> Options which require values
                opt_def -> Dict with options and default values
                multi_val - List of options that may contain multiple values
                opt_val_bin - List of options that allow zero values or one
                    value for the option
            (output) status -> True|False - If successfully parse argv.

        """

        opt_val = list(kwargs.get("opt_val", self.opt_val))
        multi_val = list(kwargs.get("multi_val", self.multi_val))
        opt_def = dict(kwargs.get("opt_def", self.opt_def))
        opt_val_bin = list(kwargs.get("opt_val_bin", self.opt_val_bin))
        status = True

        while self.argv:

            # Look for new option, always begin with "-".
            if self.argv[0][0] == "-":
                if self.argv[0] in multi_val:
                    status = self.parse_multi(opt_def=opt_def)

                elif self.argv[0] in opt_val or self.argv[0] in opt_val_bin:
                    status = self.parse_single(
                        opt_def=opt_def, opt_val_bin=opt_val_bin)

                else:
                    self.args_array[self.argv[0]] = True

            self.argv = self.argv[1:]

        return status

    def arg_require(self, **kwargs):

        """Method:  arg_require

        Description:  Checks to see if the required options are included.

        Arguments:
            (input) **kwargs:
                opt_req -> Options that are required
            (output) status -> True|False - It required options are
                included

        """

        opt_req = list(kwargs.get("opt_req", self.opt_req))
        status = True

        for item in set(opt_req) - set(self.args_array.keys()):
            print("Error:  The '{0}' option is required".format(item))
            status = False

        return status

    def arg_req_or_lst(self, **kwargs):

        """Method:  arg_req_or_lst

        Description:  Does a check on the dictionary list that requires the
            first option of the dictionary list to be in the argument list OR
            one or more of the options in the associated list to be in the
            argument list.

        Arguments:
            (input) **kwargs:
                opt_or -> Dictionary list of options for "or" operator
            (output) status -> True|False - If requirements have been meet

        """

        opt_or = dict(kwargs.get("opt_or", self.opt_or))
        status = True

        for option in set(opt_or.keys()) - set(self.args_array.keys()):
            tmp_flag = False

            for _ in set(opt_or[option]) & set(self.args_array.keys()):
                tmp_flag = True
                break

            if not tmp_flag:
                print("Error:  Option: {0} or one of these: {1} is required.".
                      format(option, opt_or[option]))
                status = tmp_flag

        return status

    def arg_req_xor(self, **kwargs):

        """Method:  arg_req_xor

        Description:  Does an XOR check between two required options.

        WARNING:  Does not handle multiple xor pairs.

        Arguments:
            (input) **kwargs:
                opt_xor -> Dictionary of options that are required XOR
            (output) status -> True|False - If one option has been selected

        """

        opt_xor = dict(kwargs.get("opt_xor", self.opt_xor))
        status = True

        for option in opt_xor:

            # Xor between key and values in dictionary.
            if not operator.xor((option in self.args_array),
                                (opt_xor[option] in self.args_array)):

                print("Option {0} or {1}, but not both.".
                      format(option, opt_xor[option]))
                status = False

        return status

    def arg_set_path(self, arg_opt):

        """Method:  arg_set_path

        Description:  Return dir path from argument list or return empty
            string.

        Arguments:
            (input) arg_opt -> Argument option holding directory path
            (output) path -> Returns directory path, if detected

        """

        path = os.path.join(
            self.args_array[arg_opt] if arg_opt in self.args_array else "")

        return path

    def arg_validate(self, **kwargs):

        """Method:  arg_validate

        Description:  Validates data for certain options based on a dictionary
            list.

        Arguments:
            (input) **kwargs:
                valid_func -> Dictionary list of options & functions
            (output) status -> True|False - If format is valid

        """

        valid_func = dict(kwargs.get("valid_func", self.valid_func))
        status = True

        for opt in set(valid_func.keys()) & set(self.args_array.keys()):

            # Call function from function list.
            if not valid_func[opt](self.args_array[opt]):
                print("Error:  Invalid format: {0} '{1}'"
                      .format(opt, self.args_array[opt]))
                status = False

        return status

    def arg_valid_val(self, **kwargs):

        """Method:  arg_valid_val

        Description:  Validates data for options based on a dictionary list.

        Arguments:
            (input) **kwargs:
                opt_valid_val -> Dictionary of options & their valid values
            (output) status -> True|False - If format is valid

        """

        opt_valid_val = dict(kwargs.get("opt_valid_val", self.opt_valid_val))
        status = True

        for option in set(self.args_array.keys()) & set(opt_valid_val.keys()):

            # If passed value is invalid for this option.
            if self.args_array[option] not in opt_valid_val[option]:
                print("Error:  Incorrect value ({0}) for option: {1}".
                      format(self.args_array[option], option))
                status = False

        return status

    def arg_wildcard(self, **kwargs):

        """Method:  arg_wildcard

        Description:  Expand wildcard file argument and replace the wildcard
            value with a list of file names.

        Arguments:
            (input) **kwargs:
                opt_wildcard -> List of wildcard options

        Example:
            Input:
                args_array = {"-a": ["cmds*", "arg*"], "-b": ["gen*"],
                              "-c": "*class*"}
                opt_wildcard = ["-a", "-b", "-c"]
            Output:
                {'-a': ['cmds_gen.py', 'arg_parser.py'],
                 '-c': ['gen_class.py'],
                 '-b': ['gen_libs.py', 'gen_class.py']}

        """

        opt_wildcard = list(kwargs.get("opt_wildcard", self.opt_wildcard))

        for opt in opt_wildcard:
            if opt in list(self.args_array.keys()) and \
               isinstance(self.args_array[opt], list):

                t_list = [glob.glob(item) for item in self.args_array[opt]]
                self.args_array[opt] = [
                    item1 for item2 in t_list for item1 in item2]

            elif opt in list(self.args_array.keys()) and isinstance(
                    self.args_array[opt], str):

                self.args_array[opt] = glob.glob(self.args_array[opt])

    def arg_xor_dict(self, **kwargs):

        """Method:  arg_xor_dict

        Description:  Does a Xor check between a key in opt_xor_val and its
            values using args_array for the check.  Therefore, the key can be
            in args_array or one or more of its values can be in arg_array, but
            both can not appear in args_array.

        Arguments:
            (input) **kwargs:
                opt_xor_val -> Dictionary with key and values that will be xor
                    with each other
            (output) status -> True|False - If one option is in args_array

        """

        opt_xor_val = dict(kwargs.get("opt_xor_val", self.opt_xor_val))
        status = True

        for opt in set(opt_xor_val.keys()) & set(self.args_array.keys()):

            for item in set(opt_xor_val[opt]) & set(self.args_array.keys()):
                print("Option {0} or {1}, but not both.".format(opt, item))
                status = False
                break

        return status

    def delete_arg(self, arg_key):

        """Method:  delete_arg

        Description:  Deletes a key from the args_array attribute.

        Arguments:
            (input) arg_key -> Key for dictionary
            (output) status -> True|False - If successfully updated
            (output) err -> Error message if update failed

        """

        err = None
        status = True

        if arg_key in self.args_array:
            del self.args_array[arg_key]

        else:
            status = False
            err = "Arg key does not exists"

        return status, err

    def get_args(self):

        """Method:  get_args

        Description:  Return the args_array attribute.

        Arguments:
            (output) Return args_array attribute in dictionary format

        """

        return self.args_array

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Return the keys from the args_array attribute.

        Arguments:
            (output) Return args_array attribute keys in list format

        """

        return list(self.args_array.keys())

    def get_val(self, skey, **kwargs):

        """Method:  get_val

        Description:  Looks for the search key in args_array and returns the
            value for that key, otherwise returns a default value.

        Notes:  Default return value is None.

        Arguments:
            (input) **kwargs:
                def_val -> Default value if search key is not found
            (output) Return value for search key or default value

        """

        def_val = kwargs.get("def_val", None)

        if isinstance(def_val, list):
            def_val = list(def_val)

        elif isinstance(def_val, dict):
            def_val = dict(def_val)

        return self.args_array.get(skey, def_val)

    def insert_arg(self, arg_key, arg_val, **kwargs):

        """Method:  insert_arg

        Description:  Inserts a key and value into the args_array attribute.
            Will not overwrite an existing key unless with the overwrite
            option set.

        Arguments:
            (input) arg_key -> Key for dictionary
            (input) arg_value -> Value for dictionary
            (input) **kwargs:
                overwrite -> True|False - Overwrite existing data
            (output) status -> True|False - If successfully inserted data
            (output) err -> Error message if insertion failed

        """

        err = None
        status = True
        overwrite = kwargs.get("overwrite", False)

        if arg_key in self.args_array and not overwrite:
            status = False
            err = "Key already exists"

        else:
            self.args_array[arg_key] = arg_val

        return status, err

    def parse_multi(self, **kwargs):

        """Method:  parse_multi

        Description:  Processes a multi-value argument in command line
            arguments.  Modifies the args_array attribute by adding a
            dictionary key and a list of values.

        Arguments:
            (input) **kwargs:
                opt_def -> Dictionary with options and default values
            (output) status -> True|False - If successfully parse argv.

        """

        opt_def = dict(kwargs.get("opt_def", self.opt_def))
        status = True

        # If no value in argv for option and it's not an integer.
        if len(self.argv) < 2 or (
                self.argv[1][0] == "-" and not gen_libs.chk_int(self.argv[1])):

            # See if default value is available for argument.
            status = self.arg_default(self.argv[0], opt_def=opt_def)

        else:
            # Handle multiple values for argument.
            self.args_array[self.argv[0]] = list()
            cnt = 0
            tmp_argv = self.argv[1:]

            # Process values until next argument.
            while tmp_argv:
                if tmp_argv[0][0] == "-":
                    break

                else:
                    self.args_array[self.argv[0]].append(tmp_argv[0])

                cnt += 1
                tmp_argv = tmp_argv[1:]

            # Move to argument after the multiple values.
            self.argv = self.argv[cnt:]

        return status

    def parse_single(self, **kwargs):

        """Method:  parse_single

        Description:  Processes a single-value argument in command line
            arguments.  Modifies the args_array attribute by adding a
            dictionary key and a value.

        Arguments:
            (input) **kwargs:
                opt_def -> Dictionary with options and default values
                opt_val_bin -> List of options that allow zero values or one
                    value for the option
            (output) status -> True|False - If successfully parse argv.

        """

        opt_def = dict(kwargs.get("opt_def", self.opt_def))
        opt_val_bin = list(kwargs.get("opt_val_bin", self.opt_val_bin))
        status = True

        # If no value in argv for option and it is not an integer.
        if len(self.argv) < 2 or (
                self.argv[1][0] == "-" and not gen_libs.chk_int(self.argv[1])):

            if self.argv[0] in opt_val_bin:
                self.args_array[self.argv[0]] = None

            else:
                # See if default value is available for argument.
                status = self.arg_default(self.argv[0], opt_def=opt_def)

        else:
            self.args_array[self.argv[0]] = self.argv[1]
            self.argv = self.argv[1:]

        return status

    def update_arg(self, arg_key, arg_val, **kwargs):

        """Method:  update_arg

        Description:  Updates a value in the args_array attribute.  Will not
            insert into args_array unless the insert option is set.

        Arguments:
            (input) arg_key -> Key for dictionary
            (input) arg_value -> Value for dictionary
            (input) **kwargs:
                insert -> True|False - Insert data if no entry exists
            (output) status -> True|False - If successfully updated
            (output) err -> Error message if update failed

        """

        err = None
        status = True
        insert = kwargs.get("insert", False)

        if arg_key in self.args_array \
           or (arg_key not in self.args_array and insert):
            self.args_array[arg_key] = arg_val

        else:
            status = False
            err = "Arg key does not exists"

        return status, err


class Daemon(object):

    """Class:  Daemon

    Description:  Class that creates and runs a Python program as a daemon
        program in include starting, stopping and restarting the process.

    Methods:
        __init__
        daemonize
        delpid
        start
        stop
        restart
        run

    Possible Bug:  Sometimes during start and stop operations an error is
        encountered on a sys.stderr.write command that states: "unsupported
        format character".  Unable to reproduce the error and thus fix the
        error.

    """

    DEV_NULL = "/dev/null"

    def __init__(self, pidfile, stdin=DEV_NULL, stdout=DEV_NULL,
                 stderr=DEV_NULL, argv_list=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Daemon class.

        Arguments:
            (input) pidfile -> Path and name of pidfile for program
            (input) stdin -> Standard in setting
            (input) stdout -> Standard out setting
            (input) stderr -> Standard error setting
            (input) argv_list -> List of command line options and values

        """

        if argv_list is None:
            self.argv_list = []

        else:
            self.argv_list = list(argv_list)

        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):

        """Method:  daemonize

        Description:  Fork the program into a background process and create
            a pidfile to track the process.

        Note:  Will do the UNIX double-fork magic (see Stevens, "Advanced
            Programming in the UNIX Environment" for details.

        Arguments:

        """

        global MASK

        # Do first fork
        try:
            pid = os.fork()

            if pid > 0:
                # Exit first parent
                sys.exit(0)

        except OSError as err:
            sys.stderr.write("Fork #1 failed: %d (%s)\n" %
                             (err.errno, err.strerror))
            sys.exit(1)

        # Decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(int(MASK))

        # Do second fork
        try:
            pid = os.fork()

            if pid > 0:
                # Exit from second parent
                sys.exit(0)

        except OSError as err:
            sys.stderr.write("Fork #2 failed: %d (%s)\n" %
                             (err.errno, err.strerror))
            sys.exit(1)

        # Redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        sdi = open(self.stdin, "r")
        sdo = open(self.stdout, "a+")

        # Cannot open unbuffered writes in Python 3
        if sys.version_info < (3, 0):
            sde = open(self.stderr, "a+", 0)

        else:
            sde = open(self.stderr, "a+")

        os.dup2(sdi.fileno(), sys.stdin.fileno())
        os.dup2(sdo.fileno(), sys.stdout.fileno())
        os.dup2(sde.fileno(), sys.stderr.fileno())

        # Write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        with open(self.pidfile, "w+") as fhdr:
            fhdr.write(pid + "\n")

    def delpid(self):

        """Method:  delpid

        Description:  Remove pidfile from the file system.

        Arguments:

        """

        os.remove(self.pidfile)

    def start(self):

        """Method:  start

        Description:  Start the daemon process.

        Arguments:

        """

        # Check for a pidfile to see if the daemon already runs.
        try:
            with open(self.pidfile, "r") as pfile:
                pid = int(pfile.read().strip())

        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exists.  Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):

        """Method:  stop

        Description:  Kill the daemon process.

        Arguments:

        """

        # Get the pid from the pidfile
        try:
            with open(self.pidfile, "r") as pfile:
                pid = int(pfile.read().strip())

        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist.  Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)

            # Not an error in a restart
            return

        # Try killing the daemon process
        try:
            inst = get_inst(os)

            while 1:
                inst.kill(pid, signal.SIGTERM)
                time.sleep(0.1)

        except OSError as msg:
            err = str(msg.args)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)

            else:
                print(str(msg.args))
                sys.exit(1)

    def restart(self):

        """Method:  restart

        Description:  Stop and restart the daemon process.

        Arguments:

        """

        self.stop()
        self.start()

    def run(self):

        """Method:  run

        Description:  Stub method holder, will contain the code to execute.
            Override this method when subclassing Daemon.  It will be called
            after the process has been daemonized by start() or restart().

        Arguments:

        """


class LogFile(object):

    """Class:  LogFile

    Description:  Class that stores and manipulates log entries either from
        files or standard in.  Stores log entries that allows for selective
        searching of log entries based on regex, keyword, and ignore.

    Methods:
        __init__
        get_marker
        find_marker
        filter_ignore
        filter_keyword
        filter_regex
        load_ignore
        load_keyword
        load_loglist
        load_marker
        load_regex
        set_marker
        set_predicate

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the LogFile class.

        Arguments:

        """

        self.loglist = []
        self.regex = None
        self.marker = None
        self.linemarker = None
        self.keyword = []
        self.predicate = any
        self.ignore = []
        self.lastline = None

    def get_marker(self):

        """Method:  get_marker

        Description:  Return the last line of the loglist array.

        Arguments:

        """

        if self.loglist:
            return self.loglist[-1]

        return None

    def find_marker(self, update=False):

        """Method:  find_marker

        Description:  Find the marker in the loglist array.

        Arguments:
            (input) update -> True|False: Update loglist based on marker found

        """

        if self.marker and self.loglist:
            for cnt, line in enumerate(self.loglist):
                if line.rstrip() == self.marker:
                    self.linemarker = cnt + 1
                    break

            if update and self.linemarker is not None:
                self.loglist = self.loglist[self.linemarker:]
                self.linemarker = 0

    def filter_ignore(self, use_marker=False):

        """Method:  filter_ignore

        Description:  Removed ignore entries from loglist array.

        Arguments:
            (input) use_marker -> True|False: Start check from marker.

        """

        if self.ignore and self.loglist:
            if use_marker and self.linemarker > 0:
                self.loglist = [item for item in self.loglist[self.linemarker:]
                                if not any(line in item.lower()
                                           for line in self.ignore)]

            else:
                self.loglist = [item for item in self.loglist
                                if not any(line in item.lower()
                                           for line in self.ignore)]

    def filter_keyword(self, use_marker=False):

        """Method:  filter_keyword

        Description:  Keep only keyword entries in loglist array.

        Arguments:
            (input) use_marker -> True|False: Start check from marker.

        """

        if self.keyword and self.loglist:
            if use_marker and self.linemarker > 0:
                self.loglist = [item for item in self.loglist[self.linemarker:]
                                if self.predicate(line in item.lower()
                                                  for line in self.keyword)]

            else:
                self.loglist = [item for item in self.loglist
                                if self.predicate(line in item.lower()
                                                  for line in self.keyword)]

    def filter_regex(self, use_marker=False):

        """Method:  filter_regex

        Description:  Keep only regex entries that match in loglist array.

        Arguments:
            (input) use_marker -> True|False: Start check from marker.

        """

        if self.regex and self.loglist:
            if use_marker and self.linemarker > 0:
                self.loglist = [item for item in self.loglist[self.linemarker:]
                                if re.search(self.regex, item)]

            else:
                self.loglist = [item for item in self.loglist
                                if re.search(self.regex, item)]

    def load_ignore(self, data):

        """Method:  load_ignore

        Description:  Load ignore list from object.

        Arguments:
            (input) data -> Holds ignore list as a file, list or string.

        """

        if (sys.version_info < (3, 0) and isinstance(data, file)) \
           or (sys.version_info > (2, 8) and isinstance(data, io.IOBase)):
            self.ignore.extend(
                [item.lower().rstrip().rstrip("\n") for item in data])

        elif isinstance(data, list):
            data = list(data)
            self.ignore.extend(
                [item.lower().rstrip().rstrip("\n") for item in data])

        elif isinstance(data, str):
            self.ignore.append(data.lower().rstrip().rstrip("\n"))

    def load_keyword(self, data, fld_delimit=" "):

        """Method:  load_keyword

        Description:  Load keyword list from object.

        Arguments:
            (input) data -> Holds keyword list as a file, list or string.
            (input) fld_delimit -> Field delimiter for a string object.

        """

        if (sys.version_info < (3, 0) and isinstance(data, file)) \
           or (sys.version_info > (2, 8) and isinstance(data, io.IOBase)):
            self.keyword.extend([x.lower().rstrip().rstrip("\n")
                                 for x in data])

        elif isinstance(data, list):
            data = list(data)
            self.keyword.extend([x.lower().rstrip().rstrip("\n")
                                 for x in data])

        elif isinstance(data, str):
            self.keyword.extend(
                data.lower().rstrip().rstrip("\n").split(fld_delimit))

    def load_loglist(self, data, dictkey=None):

        """Method:  load_loglist

        Description:  Load log entries into loglist array from object.

        Arguments:
            (input) data -> Holds log entries as a file, list, string, or dict.
            (input) dictkey -> Dictionary key value for dictionary object.

        """

        if (sys.version_info < (3, 0) and
           isinstance(data, (file, gzip.GzipFile))) \
           or (sys.version_info > (2, 8) and
           isinstance(data, (io.IOBase, gzip.GzipFile))):
            self.loglist.extend([x.rstrip().rstrip("\n") for x in data])

        elif isinstance(data, list):
            data = list(data)
            self.loglist.extend([x.rstrip().rstrip("\n") for x in data])

        elif isinstance(data, str):
            self.loglist.extend(data.rstrip().split("\n"))

        elif isinstance(data, dict) and dictkey:
            data = dict(data)

            if dictkey in data:
                self.load_loglist(data=data[dictkey])

        self.set_marker()

    def load_marker(self, data):

        """Method:  load_marker

        Description:  Load marker entry from object.

        Arguments:
            (input) data -> Holds marker entry as a file or string

        """

        if (sys.version_info < (3, 0) and isinstance(data, file)) \
           or (sys.version_info > (2, 8) and isinstance(data, io.IOBase)):
            self.marker = data.readline().rstrip().rstrip("\n")

        elif isinstance(data, str):
            self.marker = data.rstrip().rstrip("\n")

    def load_regex(self, data):

        """Method:  load_regex

        Description:  Load regext entries from object.

        Note:  If passing in r"data_string" (raw strings) then any embedded
            "\n" (newlines) will not be split upon in the string operation.

        Arguments:
            (input) data -> Marker entry as a file handler, list, or string

        """

        if (sys.version_info < (3, 0) and isinstance(data, file)) \
           or (sys.version_info > (2, 8) and isinstance(data, io.IOBase)):
            self.regex = "|".join(str(x.strip().strip("\n")) for x in data)

        elif isinstance(data, list):
            data = list(data)
            self.regex = "|".join(str(x.strip().strip("\n")) for x in data)

        elif isinstance(data, str):
            self.regex = "|".join(data.rstrip().split("\n"))

    def set_marker(self):

        """Method:  set_marker

        Description:  Set lastline attribute to last entry in loglist array.

        Arguments:

        """

        if self.loglist:
            self.lastline = self.get_marker()

    def set_predicate(self, predicate):

        """Method:  set_predicate

        Description:  Set search predicate for keyword search.

        Arguments:
            (input) predicate -> and|or:  Corresponds to all and any functions

        """

        if predicate == "and":
            self.predicate = all

        elif predicate == "or":
            self.predicate = any


class ProgressBar(object):

    """Class:  ProgressBar

    Description:  Class that displays and updates a progress bar for an ongoing
        operation.

    Methods:
        __init__
        update
        calc_and_update

    """

    def __init__(self, msg, width=20, progress_sym="#", empty_sym=" "):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgressBar class.

        Arguments:
            (input) msg -> General message describing the operation.
            (input) width -> Width of the progress bar.
            (input) progress_sym -> Character displaying completed.
            (input) empty_sym -> Character displaying uncompleted.

        """

        self.width = width

        if self.width <= 0:
            self.width = 20

        self.msg = msg
        self.progress_sym = progress_sym
        self.empty_sym = empty_sym

    def update(self, progress):

        """Method:  update

        Description:  Calculates the total number of blocks completed in the
            progress bar and displays the progress bar.

        Arguments:
            (input) progress -> Precentage completed in whole numbers.

        """

        total_blocks = self.width
        filled_blocks = int(round(progress // (100 / float(total_blocks))))
        empty_blocks = total_blocks - filled_blocks

        # Compile the progress bar of completed and uncompleted blocks.
        progress_bar = self.progress_sym * filled_blocks + self.empty_sym \
            * empty_blocks

        if not self.msg:
            self.msg = ""

        progress_msg = "\r{0} {1} {2}%".format(self.msg, progress_bar,
                                               progress)

        # Overwrite the existing progress bar with the updated progress bar.
        sys.stdout.write(progress_msg)
        sys.stdout.flush()

    def calc_and_update(self, done, total):

        """Method:  calc_and_update

        Description:  Calculate the percentage completed.

        Arguments:
            (input) done -> Number of items completed.
            (input) total -> Total number of items to complete.

        """

        progress = int(round((done / float(total)) * 100))
        self.update(progress)


class SingleInstanceException(Exception):

    """Class:  SingleInstanceException

    Description:  Class exception for the ProgramLock class when an instance
        lock has been detected.

    Methods:

    """

    pass


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class that creates a file lock instance and in which other
        programs using the same parameters will detect the lock as already
        present and prevent a second program instance from starting.

    Methods:
        __init__
        __del__

    """

    def __init__(self, argv, flavor_id=""):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgramLock class.

        Arguments:
            (input) argv -> Arguments from the command line.
            (input) flavor_id -> Unique identifier for an instance.

        """

        argv = list(argv)
        self.lock_created = False

        # Creates filename based on the full path to the program file.
        basename = os.path.splitext(os.path.abspath(argv[0]))[0].replace(
            "/", "-").replace(":", "-").replace("\\", "-") + "-%s" \
            % flavor_id + ".lock"

        self.lock_file = os.path.normpath(tempfile.gettempdir()) + "/" \
            + basename

        self.f_ptr = open(self.lock_file, "w")
        self.f_ptr.flush()

        # Creates a lock on the file, will fail if one is already present.
        try:
            fcntl.lockf(self.f_ptr, fcntl.LOCK_EX | fcntl.LOCK_NB)

        except IOError:
            raise SingleInstanceException()

        self.lock_created = True

    def __del__(self):

        """Method:  __del__

        Description:  Deletion of the ProgramLock instance.

        Arguments:

        """

        if not self.lock_created:
            return

        fcntl.lockf(self.f_ptr, fcntl.LOCK_UN)
        self.f_ptr.close()

        if os.path.isfile(self.lock_file):
            os.unlink(self.lock_file)


class System(object):

    """Class:  System

    Description:  Class which is a representation of a Linux server.  A server
        object is used as a proxy for operating with the system.  The basic
        methods and attributes to contain information about the physical
        server.

    Methods:
        __init__
        set_host_name

    """

    def __init__(self, host=None, host_name=None):

        """Method:  __init__

        Description:  Initialization of an instance of the System class.

        Arguments:
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        self.host = host
        self.host_name = host_name

    def set_host_name(self, host_name=None):

        """Method:  set_host_name

        Description:  Set the hostname attribute either from argument or pull
            from the server.

        Arguments:
            (input) host_name -> Host name of server.

        """

        if host_name:
            self.host_name = host_name

        else:
            self.host_name = socket.gethostname()


class Mail(System):

    """Class:  Mail

    Description:  Class which is a representation of an email.  An email object
        is used as a proxy for creating an email.  The basic methods and
        attributes include reading in the message, creating the message body,
        and sending the email.

    Methods:
        __init__
        add_2_msg
        read_stdin
        create_body
        create_subject
        send_mail
        send_mailx
        print_email

    """

    def __init__(self, toaddr, subj=None, frm=None, msg_type=None,
                 host_name=None, host=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail class.

        Arguments:
            (input) toaddr -> To email address.
            (input) subj -> Subject line of mail.
            (input) msg_type -> Type of email being sent.
            (input) frm -> From email address.
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        super(Mail, self).__init__(host, host_name)

        if isinstance(subj, list):
            subj = list(subj)

        if isinstance(toaddr, list):
            self.toaddr = list(toaddr)

        else:
            self.toaddr = toaddr

        if frm:
            self.frm = frm

        else:
            self.frm = getpass.getuser() + "@" + socket.gethostname()

        self.subj = None
        self.create_subject(subj)
        self.msg_type = msg_type
        self.msg = ""

    def add_2_msg(self, txt_ln=None, new_line=False):

        """Method:  add_2_msg

        Description:  Add text to text string if data is present.

        Arguments:
            (input) txt_ln -> Line of text to add to message.
            (input) new_line -> True | False - Add a newline between lines.

        """

        newln = "\n" if new_line else ""

        if txt_ln:

            if isinstance(txt_ln, str):
                if self.msg:
                    self.msg = self.msg + newln + txt_ln

                else:
                    self.msg = txt_ln

            else:
                if self.msg:
                    self.msg = self.msg + newln + json.dumps(txt_ln)

                else:
                    self.msg = json.dumps(txt_ln)

    def read_stdin(self):

        """Method:  read_stdin

        Description:  Loops through standard in and sends anything to be added
            to the message.

        Arguments:

        """

        inst = get_inst(sys)

        for line in inst.stdin:
            self.add_2_msg(line)

    def create_body(self):

        """Method:  create_body

        Description:  Combines subject line and message into a single entity.

        Arguments:

        """

        # Pull first 30 characters from message.
        if not self.subj:
            self.subj = self.msg[:30]

        return "Subject: %s\n\n%s" % (self.subj, self.msg)

    def create_subject(self, subj=None, delimiter=" "):

        """Method:  create_subject

        Description:  Creates or overwrites a subject to the email.

        Arguments:
            (input) subj -> Subject line.
            (input) delimiter -> Subject line delimiter if using a list.

        """

        if subj:
            if isinstance(subj, list):
                self.subj = delimiter.join(str(item) for item in list(subj))

            else:
                self.subj = subj

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Opens connection to smtp and mails out the message body
            to the email address.  Call to create_body() puts "Subj:" into the
            message which is required for sendmail.

        Note:  Setup the send_mailx call to allow programs using the current
            send_mail to need only an argument option.

        Arguments:
            (input) use_mailx -> True|False - To use mailx command.

        """

        if use_mailx:
            self.send_mailx()

        else:
            inst = get_inst(smtplib)
            server = inst.SMTP("localhost")
            server.sendmail(self.frm, self.toaddr, self.create_body())
            server.quit()

    def send_mailx(self):

        """Method:  send_mailx

        Description:  Opens a subprocess to mail out the message and subject
            to the email address.

        Note:  This was created due to the some mail guards not working with
            the smtplib module, but will work fine with mailx.

        Arguments:

        """

        self.subj = self.subj.replace(" ", "")

        if isinstance(self.toaddr, list):
            self.toaddr = " ".join(str(item) for item in list(self.toaddr))

        inst = get_inst(subprocess)
        proc1 = inst.Popen(['echo', self.msg], stdout=inst.PIPE)
        proc2 = inst.Popen(['mailx', '-s', self.subj, self.toaddr],
                           stdin=proc1.stdout)
        proc2.wait()

    def print_email(self):

        """Method:  print_email

        Description:  Prints email message to standard out.

        Arguments:

        """

        return "To: %s\nFrom: %s\n%s" % (
            self.toaddr, self.frm, self.create_body())


class TimeFormat(object):

    """Class:  TimeFormat

    Description:  Class which represents different time formats which can be
        formatted with pre-defined time formats or user-defined time formats.
        Formats are held in an attribute and then can create time hacks using
        these different formats.  To include microseconds to be added to the
        time formats.

    Notes:
        Pre-defined time format expressions:
            Time Expression     Reference   Description
            %Y%m%d              ymd         YearMonthDay
            %d%m%Y              dmy         DayMonthYear

        Most common time format variables:
            %Y  Four digit year
            %y  Two digit year
            %m  Month as decimal number
            %d  Day of the month
            %M  Minutes
            %H  Hours in a day based on 24 hour clock
            %I  Hours in a day based on 12 hour clock
            %p  AM or PM
            %S  Seconds

    Methods:
        __init__
        add_format
        create_adhoc_hack
        create_hack
        get_hack

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the TimeFormat class.

        Arguments:

        """

        self.rdtg = datetime.datetime.now()
        self.msecs = str(self.rdtg.microsecond // 100)
        self.delimit = "."
        self.micro = False
        self.thacks = {}
        self.tformats = {
            "ymd": {"format": "%Y%m%d", "del": "", "micro": False},
            "dmy": {"format": "%d%m%Y", "del": "", "micro": False}}

    def add_format(self, tformat, texpr, **kwargs):

        """Method:  add_format

        Description:  Add a time format expression to the class.

        Arguments:
            (input) tformat -> Name of the time format for referencing
            (input) texpr -> Time format expression
            (input) **kwargs:
                micro -> True|False -> Include microseconds
                delimit -> Delimiter between time and microseconds

        """

        micro = kwargs.get("micro", self.micro)
        delimit = kwargs.get("delimit", self.delimit)
        self.tformats[tformat] = {
            "format": texpr, "del": delimit, "micro": micro}

    def create_adhoc_hack(self, tformat, texpr, **kwargs):

        """Method:  create_adhoc_hack

        Description:  Creates an adhoc time hack and stores in class.

        Arguments:
            (input) tformat -> Name of the time format for referencing
            (input) texpr -> Time format expression
            (input) **kwargs:
                micro -> True|False -> Include microseconds
                delimit -> Delimiter between time and microseconds

        """

        ext = kwargs.get("delimit", self.delimit) + self.msecs \
            if kwargs.get("micro", self.micro) else ""

        self.thacks[tformat] = datetime.datetime.strftime(
            self.rdtg, texpr) + ext

    def create_hack(self, tformat):

        """Method:  create_hack

        Description:  Lookup up the time format in the class and create a time
            hack on that format and store in class.

        Arguments:
            (input) tformat -> Name of the time format for referencing
            (input) **kwargs:
                micro -> True|False -> Include microseconds
                delimit -> Delimiter between time and microseconds
            (output) status -> True|False - Success of time hack

        """

        status = True

        if tformat in self.tformats:
            self.create_adhoc_hack(
                tformat, self.tformats[tformat]["format"],
                micro=self.tformats[tformat]["micro"],
                delimit=self.tformats[tformat]["del"])

        else:
            status = False

        return status

    def get_hack(self, tformat):

        """Method:  get_hack

        Description:  Lookup up the time reference and return the time hack.

        Arguments:
            (input) tformat -> Name of the time reference
            (output) Time hack or None if reference not found

        """

        return self.thacks[tformat] if tformat in self.thacks else None


class Logger(object):

    """Class:  Logger

    Description:  Class which is a representation of a log file instance.  A
        Logger object is used as a proxy to implement the creation, formatting,
        writing to, and closing of a log file.

    Methods:
        __init__
        log_debug
        log_info
        log_warn
        log_err
        log_crit
        log_close

    """

    def __init__(self, name, log_file, level="INFO", msg_fmt=None,
                 date_fmt=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Logger class.

        Arguments:
            (input) name -> Name of log handler.
            (input) log_file -> Name of log file to write to.
            (input) level -> Level of message to accept to the log file.
            (input) msg_fmt -> Format of a log file entry.
            (input) date_fmt -> Format of date and time for a log file entry.
            (input) **kwargs:
                mode -> a|w - Filemode to log file.

        """

        self.handler = logging.FileHandler(log_file,
                                           mode=kwargs.get("mode", "a"))

        if not msg_fmt:
            msg_fmt = "%(asctime)s %(levelname)s %(message)s"

        self.formatter = logging.Formatter(msg_fmt, date_fmt)
        self.handler.setFormatter(self.formatter)
        self.log = logging.getLogger(name)

        if level == "DEBUG":
            self.log.setLevel(logging.DEBUG)

        elif level == "WARNING":
            self.log.setLevel(logging.WARNING)

        elif level == "ERROR":
            self.log.setLevel(logging.ERROR)

        elif level == "CRITICAL":
            self.log.setLevel(logging.CRITICAL)

        else:
            self.log.setLevel(logging.INFO)

        self.log.addHandler(self.handler)

    def log_debug(self, msg):

        """Method:  log_debug

        Description:  Writes message to log file at DEBUG level.

        Arguments:
            (input) msg -> Message to be written to log.

        """

        self.log.debug(msg)

    def log_info(self, msg):

        """Method:  log_info

        Description:  Writes message to log file at INFO level.

        Arguments:
            (input) msg -> Message to be written to log.

        """

        self.log.info(msg)

    def log_warn(self, msg):

        """Method:  log_warn

        Description:  Writes message to log file at WARNING level.

        Arguments:
            (input) msg -> Message to be written to log.

        """

        self.log.warning(msg)

    def log_err(self, msg):

        """Method:  log_err

        Description:  Writes message to log file at ERROR level.

        Arguments:
            (input) msg -> Message to be written to log.

        """

        self.log.error(msg)

    def log_crit(self, msg):

        """Method:  log_crit

        Description:  Writes message to log file at CRITICAL level.

        Arguments:
            (input) msg -> Message to be written to log.

        """

        self.log.critical(msg)

    def log_close(self):

        """Method:  log_close

        Description:  Closes the log file and removes the log handler.

        Arguments:
            (input) msg -> Message to be written to log.

        """

        for handle in self.log.handlers:
            handle.close()
            self.log.removeHandler(handle)


# The package yum==3.4.3 only works with Python 2.7
if sys.version_info < (3, 0):
    class Yum(yum.YumBase):

        """Class:  Yum

        Description:  Class which is a representation for YumBase system class.
            A yum object is used as a proxy for using the yum command.

        Methods:
            __init__
            get_hostname
            get_os
            get_release
            get_distro
            fetch_repos
            fetch_install_pkgs
            fetch_update_pkgs

        """

        def __init__(self, host_name=None):

            """Method:  __init__

            Description:  Initialization of an instance of the Yum class.

            Arguments:
                (input) host_name -> Host name of server

            """

            yum.YumBase.__init__(self)

            if host_name:
                self.host_name = host_name

            else:
                self.host_name = socket.gethostname()

            self.os_name = platform.system()
            self.release = platform.release()
            self.distro = platform.linux_distribution()

        def get_distro(self):

            """Method:  get_distro

            Description:  Reuturn class' linux_distribution.

            Arguments:
                (output) self.distro -> Linux distribution tuple value

            """

            return self.distro

        def get_hostname(self):

            """Method:  get_hostname

            Description:  Return the class' hostname.

            Arguments:
                (output) self.host_name -> Server's host name

            """

            return self.host_name

        def get_os(self):

            """Method:  get_os

            Description:  Return the class' OS platform

            Arguments:
                (output) self.os_name -> Server's Operating system name.

            """

            return self.os_name

        def get_release(self):

            """Method:  get_release

            Description:  Return the class' OS release version.

            Arguments:
                (output) self.release -> Kernel release version

            """

            return self.release

        def fetch_repos(self):

            """Method:  fetch_repos

            Description:  Return a list of repos.

            Arguments:
                (output) List of repositories

            """

            self.doRepoSetup()

            return [repo.name for repo in self.repos.listEnabled()]

        def fetch_install_pkgs(self):

            """Method:  fetch_install_pkgs

            Description:  Return a dictionary of installed packages in a list.

            Arguments:
                (output) List of installed of packages in JSON format

            """

            return [{"package": pkg.name, "ver": pkg.version, "arch": pkg.arch}
                    for pkg in self.rpmdb]

        def fetch_update_pkgs(self):

            """Method:  fetch_update_pkgs

            Description:  Return a dictionary of packages to be updated in a
                list.

            Arguments:
                (output) List of packages for installation in JSON format

            """

            return [{"package": pkg.name, "ver": pkg.version, "arch": pkg.arch,
                     "repo": str(getattr(pkg, "repo"))}
                    for pkg in self.doPackageLists(pkgnarrow="updates",
                                                   patterns="",
                                                   ignore_case=True)]
