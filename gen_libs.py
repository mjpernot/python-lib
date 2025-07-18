# Classification (U)

"""Program:  gen_libs.py

    Description:  A library program that contains a number of modules for
        general use.

    Functions:
        add_cmd
        and_is_true
        binary_string
        bytes_2_readable
        chk_crt_dir
        chk_crt_file
        chk_int
        chk_perm
        clear_file
        compress
        cp_dir
        cp_file
        cp_file2
        create_cfg_array
        crt_file_time
        date_range
        del_not_and_list
        del_not_in_list
        dict_2_list
        dict_2_std
        dict_out
        dir_file_match
        disk_usage
        display_data
        file_cleanup
        file_search
        file_search_cnt
        file_2_list
        filename_search
        find_email_addr
        float_div
        get_base_dir
        get_data
        get_date
        get_secs
        get_time
        has_whitespace
        help_func
        in_list
        is_add_cmd
        is_base64
        is_empty_file
        is_file_deletable
        is_file_text
        is_missing_lists
        is_pos_int
        is_true
        key_cleaner
        list_dirs
        list_files
        list_filter_files
        list_2_dict
        list_2_str
        load_module
        make_dir
        make_md5_hash
        make_zip
        merge_data_types
        merge_two_dicts
        milli_2_readadble
        month_days
        month_delta
        mv_file
        mv_file2
        normalize
        not_in_list
        no_std_out
        octal_to_str
        openfile
        pascalize
        pct_int
        perm_check
        print_data
        print_dict
        print_list
        prt_dict
        prt_lvl
        prt_msg
        rename_file
        rm_dup_list
        rm_file
        rm_key
        rm_newline_list
        rm_whitespace
        root_run
        rotate_files
        sec_2_hr
        str_2_list
        str_2_type
        touch
        transpose_dict
        validate_date
        validate_int
        write_file
        write_file2
        write_to_log

    Tuple:
        NTupleDiskUsage

"""

# Libraries and Global Variables

# Standard
import subprocess
import os
import time
import shutil
import datetime
import sys
import zipfile
import glob
import re
import collections
import contextlib
import io
import string

try:
    import simplejson as json
except ImportError:
    import json

import ast
import gzip
import calendar
import base64
import binascii
import errno
import pprint
import chardet

# Local
try:
    from . import version

except (ValueError, ImportError) as err:
    import version

__version__ = version.__version__


# Tuples
NTupleDiskUsage = collections.namedtuple("usage", "total used free")


def add_cmd(cmd, **kwargs):

    """Function:  add_cmd

    Description:  Append name of argument and possibly value for the argument
        to the command line list.

    Arguments:
        (input) cmd -> List containing the program command line.
        (input) **kwargs:
            arg -> Name of argument being added.
            val -> Value for argument being added.
        (output) cmd -> List containing the program command line.

    """

    cmd = list(cmd)

    # Append before returning, appending on return does not make the change.
    if "val" in kwargs:
        cmd.append(kwargs["arg"] + kwargs["val"])

    else:
        cmd.append(kwargs["arg"])

    return cmd


def and_is_true(itemx, itemy):

    """Function:  and_is_true

    Description:  Uses a truth table to do an AND check between two values of
        {Yes (True) / No (False)}.

    Arguments:
        (input) itemx -> Yes or No value.
        (input) itemy -> Yes or No value.
        (output) Return True | False based on AND comparsion.

    """

    truth_tbl = {"Yes": True, "No": False}

    return truth_tbl[itemx] and truth_tbl[itemy]


def binary_string():

    """Function:  binary_string

    Description:  Returns lamdba as a function to check if data is binary.

    Arguments:
        (output) lamdba function

    """

    textchars = bytearray(
        {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})

    return lambda bytes: bool(bytes.translate(None, textchars))


def bytes_2_readable(size, precision=2):

    """Function:  bytes_2_readable

    Description:  Converts a size (in bytes) in the appropriate readable size
        with post-tag symbol.

    Arguments:
        (input) size -> Size in bytes to convert.
        (input) precision -> Percision after decimal.

    """

    suffix = ["B", "KB", "MB", "GB", "TB"]
    suf_index = 0

    while size > 1024 and suf_index < 4:
        suf_index += 1
        size = size / 1024.0

    return f"{size:.{precision}f}" + f"{suffix[suf_index]}"


def chk_crt_dir(dir_name=None, create=False, write=False, read=False,
                f_hdlr=sys.stdout, **kwargs):

    """Function:  chk_crt_dir

    Description:  Check for the existence of a directory and whether to create
        one if not present.  Also checks the read and write permissions
        on the directory as determined by the arguments.

    Arguments:
        (input) dir_name -> Directory name.
        (input) create -> True|False - Create directory if not present.
        (input) write -> True|False - Is Writeable on directory.
        (input) read -> True|False - Is Readable on directory.
        (input) f_hdlr -> File handler to write messages to or stdout.
        (input) **kwargs:
            no_print -> True|False - Suppress printing of error messages.
            exe -> True|False - Is Executable on file.
        (output) status -> True|False - False if one of the checks fails.
        (output) err_msg -> None|Error message of check that fails.

    """

    no_print = kwargs.get("no_print", False)
    exe = kwargs.get("exe", False)
    status = True
    err_msg = ""

    # Redirect print to /dev/null.
    if no_print:
        f_hdlr = open(                              # pylint:disable=R1732
            os.devnull, mode="w", encoding="UTF-8")

    if not dir_name.strip():
        err_msg = "Error:  No value passed for directory name"
        print(err_msg, file=f_hdlr)
        status = False

    else:
        # Create directory if requested.
        if create and not os.path.isdir(dir_name):
            try:
                os.makedirs(dir_name)

            except OSError:
                err_msg = f"Error: Unable to create directory {dir_name}"
                print(err_msg, file=f_hdlr)
                status = False

        # Directory does not exist.
        elif not os.path.isdir(dir_name):
            err_msg = f"Error: Directory: {dir_name} does not exist."
            print(err_msg, file=f_hdlr)
            status = False

        status, err_msg = perm_check(
            dir_name, "Directory", f_hdlr, status=status, err_msg=err_msg,
            read=read, write=write, exe=exe)

    if no_print:
        f_hdlr.close()

    if err_msg:
        err_msg = err_msg.strip("\n")

    else:
        err_msg = None

    return status, err_msg


def chk_crt_file(f_name=None, create=False, write=False, read=False,
                 f_hdlr=sys.stdout, **kwargs):

    """Function:  chk_crt_file

    Description:  Check for the existence of a file and whether to create one
        if not present.  Also checks the read, write, and execute permissions
        on the file as determined by the arguments.

    Arguments:
        (input) f_name -> File name with directory path.
        (input) create -> True|False - Create file if not present.
        (input) write -> True|False - Is Writeable on file.
        (input) read -> True|False - Is Readable on file.
        (input) f_hdlr -> File handler to write messages to or stdout.
        (input) **kwargs:
            no_print -> True|False - Suppress printing of error messages.
            exe -> True|False - Is Executable on file.
        (output) status -> True|False - False if one of the checks fails.
        (output) err_msg -> None|Error message of check that fails.

    """

    no_print = kwargs.get("no_print", False)
    exe = kwargs.get("exe", False)
    status = True
    err_msg = ""

    # Redirect print to /dev/null
    if no_print:
        f_hdlr = open(                              # pylint:disable=R1732
            os.devnull, mode="w", encoding="UTF-8")

    if not f_name.strip():
        err_msg = "Error:  No value passed for filename."
        print(err_msg, file=f_hdlr)
        status = False

    else:
        if create and not os.path.isfile(f_name):
            touch(f_name)

        elif not os.path.isfile(f_name):
            err_msg = f"Error:  File {f_name} does not exist."
            print(err_msg, file=f_hdlr)
            status = False

        status, err_msg = perm_check(
            f_name, "File", f_hdlr, status=status, err_msg=err_msg,
            read=read, write=write, exe=exe)

    if no_print:
        f_hdlr.close()

    if err_msg:
        err_msg = err_msg.strip("\n")

    else:
        err_msg = None

    return status, err_msg


def chk_int(line):

    """Function:  chk_int

    Description:  Checks to see if the string is an integer.
        NOTE:   Does not work for floats.

    Arguments:
        (input) line -> String containing an integer.
        (output) True|False -> Whether the string is an integer.

    """

    # Remove positive/negative sign if present.
    if line[0] in ("-", "+"):
        return line[1:].isdigit()

    return line.isdigit()


def chk_perm(item, oct_perm):

    """Method:  chk_perm

    Description:  Checks to see a permission is turned on for an object based
        on an octal argument.

    Note:  This will only check the owner of the object and only checks to see
        if the permission is on, does not check for permissions set to off.

    Arguments:
        (input) item -> Path and name of object to be checked
        (input) oct_perm -> Permission of object in octal format: 7 (rwx),
            6 (rw-), 5 (r-x), 4 (r--), 3 (-wx), 2 (-w-), 1 (--x), 0 (---)
        (output) status -> True|False - If object has correct permissions

    """

    status = True

    if octal_to_str(oct_perm)[2] == "x" and not os.access(item, os.X_OK):
        print(f"Error: {item} is not executable.")
        status = False

    if octal_to_str(oct_perm)[0] == "r" and not os.access(item, os.R_OK):
        print(f"Error: {item} is not readable.")
        status = False

    if octal_to_str(oct_perm)[1] == "w" and not os.access(item, os.W_OK):
        print(f"Error: {item} is not writable.")
        status = False

    return status


def clear_file(f_name):

    """Function:  clear_file

    Description:  Clear contents of an existing file or create a new file.

    Arguments:
        (input) f_name -> File name along with directory path.

    """

    open(f_name, mode="w", encoding="UTF-8").close()    # pylint:disable=R1732


def compress(fname):

    """Function:  compress

    Description:  Compress a file using gzip with a process call and wait until
        it completes.

    Arguments:
        (input) fname -> File name

    """

    proc1 = subprocess.Popen(["gzip", fname])           # pylint:disable=R1732
    proc1.wait()


def cp_dir(src_dir, dest_dir):

    """Function:  cp_dir

    Description:  Copies a directory from source to destination.

    Arguments:
        (input) src_dir -> Source directory
        (input) dest_dir -> Destination directory
        (output) status -> True|False - True if copy was successful
        (output) err_msg -> Error message from copytree exception or None

    """

    status = True
    err_msg = None

    try:
        shutil.copytree(src_dir, dest_dir)

    # Directory permission error.
    except shutil.Error as err:
        err_msg = f"Directory not copied.  Perms Error Message: {err}"
        status = False

    # Directory does not exist.
    except OSError as err:
        err_msg = f"Directory not copied.  Exist Error Message: {err}"
        status = False

    return status, err_msg


def cp_file(fname, src_dir, dest_dir, new_fname=None):

    """Function:  cp_file

    Description:  Copies a file from source directory to destination directory,
        permissions are copied as well (e.g. cp -p).  Allows for the file to be
        renamed in the process.
        NOTE:  Same as cp_file2 function, but this has exception handling for
            shutil.copy2 errors.

    Arguments:
        (input) fname -> File name
        (input) src_dir -> Source directory
        (input) dest_dir -> Destination directory
        (input) new_fname -> New file name or None if staying the same
        (output) status -> True|False - True if copy was successful
        (output) err_msg -> Error message from shutil.copy2 exception or None

    """

    status = True
    err_msg = None

    if new_fname:
        new_fname = os.path.join(dest_dir, new_fname)

    else:
        new_fname = dest_dir

    try:
        shutil.copy2(os.path.join(src_dir, fname), new_fname)

    except IOError as err:
        errmsg = err.args[1]
        status = False

        if errmsg == "No such file or directory":
            if not os.path.isdir(src_dir):
                err_msg = errmsg + ": " + src_dir

            elif not os.path.isdir(dest_dir):
                err_msg = errmsg + ": " + dest_dir

            elif not os.path.isfile(os.path.join(src_dir, fname)):
                err_msg = errmsg + ": " + os.path.join(src_dir, fname)

            else:
                err_msg = errmsg

        else:
            err_msg = errmsg

    return status, err_msg


def cp_file2(fname, src_dir, dest_dir, new_fname=None):

    """Function:  cp_file2

    Description:  Copies a file from source directory to destination directory,
        but the permissions are copied as well (e.g. cp -p).  Allows for the
        file to be renamed in the process.
        NOTE:  This function does not deal with errors from shutil.copy2.  Use
            the cp_file function if error handling is required.

    Arguments:
        (input) fname -> File name
        (input) src_dir -> Source directory
        (input) dest_dir -> Destination directory
        (input) new_fname -> New file name or None if staying the same

    """

    if new_fname:
        dest_dir = os.path.join(dest_dir, new_fname)

    shutil.copy2(os.path.join(src_dir, fname), dest_dir)


def create_cfg_array(cfg_file, **kwargs):

    """Function:  create_cfg_array

    Description:  Parses a configuration file which can contain multiple
        configuration connections & creates an array of configurations.  This
        is for general class use and will require the first line of the
        configuration file to be the "user" entry and the key and the value
        will be delimited by "=" (equal sign).

    Arguments:
        (input) cfg_file -> Configuration file
        (input) **kwargs:
            cfg_path - Configuration directory path
        (output) cfg_array -> Array of configurations

    """

    cfg_array = []
    cfg_dict = {}
    cfg_path = kwargs.get("cfg_path", "./")

    # Does config file exists in current location.
    if os.path.isfile(cfg_file):
        fname = open(cfg_file, mode="r", encoding="UTF-8")

    else:
        fname = open(                                   # pylint:disable=R1732
            os.path.join(cfg_path, cfg_file), mode="r", encoding="UTF-8")

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
        # Add last dict to config array.                # pylint:disable=W0120
        cfg_array.append(cfg_dict)

    fname.close()

    return cfg_array


def crt_file_time(fname, path, ext="", **kwargs):

    """Function:  crt_file_time

    Description:  Creates a file name with timestamp along with directory path.

    Arguments:
        (input) fname -> File name
        (input) path -> Directory path
        (input) ext -> Extension of file
        (input) kwargs:
            secs -> True|False - Add seconds to timestamp
        (output) -> Directory path/file_name.time.extension

    """

    if ext and "." not in ext[0]:
        ext = "." + ext

    if kwargs.get("secs", False):
        time_fmt = "%Y%m%d_%H%M%S"

    else:
        time_fmt = "%Y%m%d_%H%M"

    return os.path.join(path, fname + "." + time.strftime(time_fmt) + ext)


def date_range(start_dt, end_dt):

    """Function:  date_range

    Description:  Generators a list of year-month-01 combinations between two
        dates.
        NOTE:  The day will be included in the datetime instance, but all days
            will be set to the beginning of each month (e.g. YYYY-MM-01).

    Arguments:
        (input) start_dt -> Start date - datetime class instance.
        (input) end_dt -> End date - datetime class instance.
        (output) Generator list of datetime instances.

    """

    start_dt = start_dt.replace(day=1)
    end_dt = end_dt.replace(day=1)
    forward = end_dt >= start_dt
    finish = False
    sdt = start_dt

    while not finish:
        yield sdt.date()

        if forward:
            days = month_days(sdt)
            sdt = sdt + datetime.timedelta(days=days)
            finish = sdt > end_dt

        else:
            _tmp_dt = sdt.replace(day=1) - datetime.timedelta(days=1)
            sdt = _tmp_dt.replace(day=sdt.day)
            finish = sdt < end_dt


def del_not_and_list(list1, list2):

    """Function:  del_not_and_list

    Description:  Remove any items in list 1 that are present in list 2.

    Arguments:
        (input) list1 -> List array 1.
        (input) list2 -> List array 2 - items to be removed.
        (output) list1 -> List array 1 minus items from list array 2.

    """

    list1 = list(list1)
    list2 = list(list2)

    for item in list(set(list1) & set(list2)):
        list1.remove(item)

    return list1


def del_not_in_list(list1, list2):

    """Function:  del_not_in_list

    Description:  Compares the first list with the second list and removes any
        items in the first list that are not in the second list. Intersects
        list 1 and list 2.

    Arguments:
        (input) list1 -> List one.
        (input) list2 -> List two.
        (output) list1 -> List one minus items not in list two.

    """

    list1 = list(list1)
    list2 = list(list2)

    for item in list(set(list1) - set(list2)):
        list1.remove(item)

    return list1


def dict_2_list(dict_list, key_val):

    """Function:  dict_2_list

    Description:  Converts a dictionary array list to a array list, based on a
        key value passed to the function.  Only those values for the key value
        will be put into the list.

    Arguments:
        (input) dict_list -> Dictionary array list.
        (input) key_val -> Key value in the dictionary key.
        (output) arry_list -> Array list of values for key value.

    """

    return [row[key_val] for row in list(dict_list) if key_val in row]


def dict_2_std(data, ofile=False, mode="w", **kwargs):

    """Function:  dict_2_std

    Description:  Convert Dict document to standard format and print to
        standard out or file.

    Arguments:
        (input) data -> Dict document.
        (input) ofile -> Name of file to print to.
        (input) mode -> w|a => Write or append mode.

    """

    data = dict(data)

    if ofile:
        outfile = open(                                 # pylint:disable=R1732
            ofile, mode=mode, encoding="UTF-8")

    else:
        outfile = sys.stdout

    prt_dict(data, outfile, **kwargs)

    if ofile:
        outfile.close()


def dict_out(data, **kwargs):

    """Function:  dict_out

    Description:  Print dictionary to a file, standard out, and/or an email
        instance either in expanded or flatten JSON format.

    Arguments:
        (input) data -> Dictionary document
        (input) kwargs:
            expand -> True|False - Expand JSON format
            mail -> Mail instance
            ofile -> Name of output file name
            mode -> w|a => Write or append mode for file
            no_std -> True|False - Do not print to standard out
        (output) err_flag -> True|False - If error has occurred
        (output) err_msg -> Error message

    """

    err_flag = False
    err_msg = None
    mail = kwargs.get("mail", None)
    indent = 4 if kwargs.get("expand", False) else None
    ofile = kwargs.get("ofile", None)

    if isinstance(data, dict):
        if ofile:
            print_data(
                json.dumps(data, indent=indent), ofile=ofile,
                mode=kwargs.get("mode", "w"))

        if not kwargs.get("no_std", False):
            print_data(json.dumps(data, indent=indent))

        if mail:
            mail.add_2_msg(json.dumps(data, indent=indent))

    else:
        err_flag = True
        err_msg = f"Error: Is not a dictionary: {data}"

    return err_flag, err_msg


def dir_file_match(dir_path, file_str, add_path=False):

    """Function:  dir_file_match

    Description:  Return a list of file names from a directory, but only those
        that match a search string.

    NOTE:  Match works starting at the beginning of the file name.

    Arguments:
        (input) dir_path -> Directory path to search in.
        (input) file_str -> Name of search string.
        (input) add_path -> True|False - Add path name to file name.
        (output) Return a list of (path/)file names matching the search string.

    """

    if add_path:
        return [os.path.join(dir_path, item)
                for item in list_files(dir_path) if re.match(file_str, item)]

    return [item for item in list_files(dir_path)
            if re.match(file_str, item)]


def disk_usage(path):

    """Function:  disk_usage

    Description:  Return in bytes a partition's total, used, and free space.

    Arguments:
        (input) path -> Directory path of the partition
        (output) NTupleDiskUsage (named tuple):
            total -> Total space in bytes
            used -> Used space in bytes
            free -> Free space in bytes

    """

    stv = os.statvfs(path)
    free = stv.f_bavail * stv.f_frsize
    total = stv.f_blocks * stv.f_frsize
    used = (stv.f_blocks - stv.f_bfree) * stv.f_frsize

    return NTupleDiskUsage(total, used, free)


def display_data(data, level=0, f_hdlr=sys.stdout):

    """Function:  display_data

    Description:  Breaks out a dictionary data structure into a readable
        format, prints to a file handler.

    Arguments:
        (input) data -> Data object
        (input) level -> Number of tabs to print
        (input) f_hdlr -> File handler (e.g. file or standard out)

    """

    def print_level(level, f_hdlr):

        """Function:  print_level

        Description:  Print the number of levels (i.e. tabs) required for line.

        Arguments:
            (input)  level -> Number of tabs to print
            (input) f_hdlr -> File handler (e.g. file or standard out)

        """

        cnt = 0

        while cnt < level:
            print("\t", end="", file=f_hdlr)
            cnt += 1

    if isinstance(data, dict):
        data = dict(data)

        for item in data:

            # Recursive call for specific data types.
            if isinstance(data[item], (dict, list)):
                print_level(level, f_hdlr)

                print(f"{item} =>", file=f_hdlr)

                display_data(data[item], level + 1, f_hdlr=f_hdlr)

            else:
                print_level(level, f_hdlr)

                print(f"{item} :  {data[item]}", file=f_hdlr)

    # Recursive call for specific data types.
    elif isinstance(data, list):
        data = list(data)

        for item in data:
            display_data(item, level, f_hdlr=f_hdlr)

    else:
        print_level(level, f_hdlr)

        print(f"{data}", file=f_hdlr)


def file_cleanup(dir_path, days):

    """Function:  file_cleanup

    Description:  Removes all files in a directory over a specified number of
        days old.  Check is based on the last modified date for the file.

    Arguments:
        (input) dir_path -> Directory path
        (input) days -> Number of days to be retained for

    """

    today = time.time()

    for fname in os.listdir(dir_path):
        fullname = os.path.join(dir_path, fname)

        # Is it a file and over N days old.
        if os.path.isfile(fullname) \
           and os.stat(fullname).st_mtime < today - days * 86400:
            os.remove(fullname)


def file_search(f_name, data_str):

    """Function:  file_search

    Description:  Search for a string in a file and return the line it was
        found in a line.

    NOTE:  Returns only the first instance found in the file.

    Arguments:
        (input) f_name -> File name searching
        (input) data_str -> Search string
        (output) line - > Full line string was found in or None, if not found

    """

    line = None

    with open(f_name, mode="r", encoding="UTF-8") as s_file:
        for item in s_file:
            if data_str in item:
                line = item
                break

    return line


def file_search_cnt(f_name, pattern):

    """Function:  file_search_cnt

    Description:  Search for a pattern in a file and count the number of lines
        the pattern is found in.

    Arguments:
        (input) f_name -> File name
        (input) pattern -> Pattern searching for
        (output) cnt -> Number of lines found with the pattern in it

    """

    with open(f_name, mode="r", encoding="UTF-8") as f_hdlr:
        cnt = f_hdlr.read().count(pattern)

    return cnt


def file_2_list(filename):

    """Function:  file_2_list

    Description:  Reads in each line of a file and inserts into a list.
        NOTE: Will remove any newlines "\n" at the end of each line.

    Arguments:
        (input) filename -> File name to be read
        (output) lines -> The file lines in a list

    """

    with open(filename, mode="r", encoding="UTF-8") as f_hdlr:
        lines = [item.rstrip("\n") for item in f_hdlr.readlines()]

    return lines


def filename_search(dir_path, file_str, add_path=False):

    """Function:  filename_search

    Description:  Return a list of file names from a directory that contain
        the search string somewhere in the file name.

    NOTE:  file_str argument will be able to handle regular expressions.

    Arguments:
        (input) dir_path -> Directory path to search in.
        (input) file_str -> Name of search string (can be regular expression).
        (input) add_path -> True|False - Add path name to file name.
        (output) Return a list of (path/)file names found with search string.

    """

    if add_path:
        return [os.path.join(dir_path, item)
                for item in list_files(dir_path)
                if re.search(file_str, item)]

    return [item for item in list_files(dir_path)
            if re.search(file_str, item)]


def find_email_addr(data):

    """Function:  find_email_addr

    Description:  Finds all email addresses in a data string.

    Known Issue:  If a period (.) is at the end of the email address in the
        data string the function will return the ending period as part of the
        email address.

    Arguments:
        (input) data -> Data string with email addresses.
        (output) -> List of email addresses.

    """

    return re.findall(r"[\w\.-]+@[\w\.-]+", data)


def float_div(num1, num2):

    """Function:  float_div

    Description:  Takes two numbers and does floating division.  Returns zero
        if the divisor is zero.

    Arguments:
        (input) num1 number -> First number.
        (input) num2 number -> Second number.
        (output) Return results of division or 0.

    """

    try:
        return float(num1) / num2

    except ZeroDivisionError:
        return 0


def get_base_dir(f_name):

    """Function:  get_base_dir

    Description:  Return the base directory path of the file name.

    Arguments:
        (input) f_name -> File name.
        (output) Base directory path.

    """

    return os.path.dirname(os.path.realpath(f_name))


def get_data(f_hdlr):

    """Function:  get_data

    Description:  Reads a file into a list and strips off ending spaces/tabs.

    Arguments:
        (input) f_hdlr -> File handler.
        (output) List of all file entries.

    """

    return [item.rstrip() for item in f_hdlr]


def get_date():

    """Function:  get_date

    Description:  Return the current date in the YYYY-MM-DD format.

    Arguments:
        (output) Current system date.

    """

    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")


def get_secs(tdd):

    """Function:  get_secs

    Description:  Converts a datetime delta value to total number of seconds.

    Arguments:
        (input) tdd -> Datetime Delta.
        (output) -> Returns total number of seconds for datetime delta.

    """

    return (tdd.seconds + tdd.days * 24 * 3600) * 10**6 // 10**6


def get_time():

    """Function:  get_time

    Description:  Return the current time in the HH:MM:SS format.

    Arguments:
        (output) Current system time.

    """

    return datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")


def has_whitespace(data):

    """Function:  has_whitespace

    Description:  Returns True|False on whether a string has a white space.

    Arguments:
        (input) data -> Data string
        (output) True|False - Has a white space

    """

    for item in data:
        if item in string.whitespace:
            return True

    return False


def help_func(args, ver, func_name=None):

    """Function:  help_func

    Description:  Checks for help arguments and calls the docstring of the
        passed function or print out the version.  Current options checked:
        -v (version) and -h (help)
        An exit flag (True) is passed to the calling program if one of the
        options is detected.

    Arguments:
        (input) args -> A gen_class.ArgParser class instance
        (input) ver -> Version information on the calling program
        (input) func_name -> Function that will contain help message
        (output) status -> Returns success of operation

    """

    status = False

    if args.arg_exist("-h"):
        func_name()
        status = True

    if args.arg_exist("-v"):
        print(ver)
        status = True

    return status


def in_list(name, array_list):

    """Function:  in_list

    Description:  Checks to see if the a value is in a list and either returns
        the value or an empty list.

    Arguments:
        (input) name -> Value
        (input) array_list -> Array List
        (output) Return name in a list or empty list

    """

    array_list = list(array_list)

    if name in array_list:
        return [name]

    return []


def is_add_cmd(args, cmd, opt_arg_list):

    """Function:  is_add_cmd

    Description:  Determine if any additional options need to be added to the
        command line.

    Arguments:
        (input) args -> A gen_class.ArgParser class instance
        (input) cmd -> List array containing the program arguments
        (input) opt_arg_list -> Dictionary of additional options
        (output) cmd -> List array containing the program arguments

    """

    cmd = list(cmd)
    opt_arg_list = dict(opt_arg_list)

    for opt in opt_arg_list:

        # Is option in array and is set to True
        if args.arg_exist(opt) and args.get_val(opt) \
           and isinstance(args.get_val(opt), bool):

            if isinstance(opt_arg_list[opt], list):

                for item in opt_arg_list[opt]:
                    cmd = add_cmd(cmd, arg=item)

            else:
                cmd = add_cmd(cmd, arg=opt_arg_list[opt])

        elif args.arg_exist(opt):
            cmd = add_cmd(cmd, arg=opt_arg_list[opt], val=args.get_val(opt))

    return cmd


def is_base64(data):

    """Function:  is_base64

    Description:  Determines if the data is base64 encoded.

    Warning:  Unicode strings in Python 3 will not be detected as a string.

    Note: Python 3:  If data string has unicode in it, an exception will be
        thrown and the function will return false.

    Arguments:
        (input) data -> Data string to be checked
        (output) status -> True|False - Is base64 encoded

    """

    try:
        if isinstance(data, str):
            data_bytes = bytes(data, 'ascii')

        elif isinstance(data, bytes):
            data_bytes = data

        else:
            raise binascii.Error

        status = base64.b64encode(
            base64.b64decode(data_bytes))[1:70] == data_bytes[1:70]

    except binascii.Error:
        status = False

    return status


def is_empty_file(f_name):

    """Function:  is_empty_file

    Description:  Checks to see if a file is empty.
        NOTE:  Returns None if file does not exist.

    Arguments:
        (input) f_name -> File being checked
        (output) status -> True|False|None -> True if file is empty

    """

    status = None

    if os.path.isfile(f_name):
        status = os.stat(f_name).st_size == 0

    return status


def is_file_deletable(fname):

    """Function:  is_file_deletable

    Description:  Determine if a file can be removed.

    Arguments:
        (input) fname -> Filename and full path
        (output) status -> True|False - File can be removed

    """

    status = False
    f_dirname = os.path.dirname(fname)

    # Ensure object is a file and writable and the directory has correct perms
    if os.path.isfile(fname):
        if os.access(fname, os.W_OK):
            if os.access(f_dirname, os.W_OK | os.X_OK):
                status = True

    return status


def is_file_text(f_name):

    """Function:  is_file_text

    Description:  Returns True or False on whether the file is a text file.

    Note:  If a BOM (Byte-Order Mark) UTF-16 LE (Little Endian) set is used in
        a text file, this function will detect it as a binary file.

    Arguments:
        (input) f_name -> File being checked
        (output) True|False -> Is the file a text file

    """

    with io.open(f_name, "rb") as f_hldr:               # pylint:disable=R1732
        f_head = f_hldr.read(512)

    is_binary_string = binary_string()

    return not is_binary_string(f_head)


def is_missing_lists(list1, list2):

    """Function:  is_missing_lists

    Description:  Compares two lists and returns a list of missing values from
        list1 not found in list2.

    Arguments:
        (input) list1 -> List 1
        (input) list2 -> List 2
        (output) Return list of missing values

    """

    list1 = list(list1)
    list2 = list(list2)

    return [item for item in list1 if item not in list2]


def is_pos_int(num):

    """Function:  is_pos_int

    Description:  Returns True|False if number is an integer and positive.

    Arguments:
        (input) num -> Integer value.
        (output) True|False -> Number is an integer and positive.

    """

    return isinstance(num, int) and num > 0


def is_true(item):

    """Function:  is_true

    Description:  Returns True or False for a Yes|No or ON|OFF value.  Uses a
        dictionary to determine the return value.

    Arguments:
        (input) x -> Yes or No value.
        (output) Return True | False based on truth_tbl.

    """

    truth_tbl = {"Yes": True, "No": False, "ON": True, "OFF": False}

    return truth_tbl[item]


def key_cleaner(data, char, repl):

    """Function: key_cleaner

    Description: Replace one or more characters in a dictionary key with one
        or more other characters.  Recursive function call to parse through all
        levels of dictionary.

    Warning: Duplicate keys will be removed during the replacement process.

    Arguments:
        (input) data -> A data object
        (input) char -> One or more characters to search for
        (input) repl -> One or more characters to replace with
        (output) data -> Modified data object

    """

    if isinstance(data, dict):
        data = dict(data)

        for key, value in list(data.items()):

            # Recursive call on dictionary's value
            data[key] = key_cleaner(value, char, repl)

            if char in key:
                tvalue = data[key]
                # Change key name and add new value
                data[key.replace(char, repl)] = tvalue
                del data[key]

        return data

    if isinstance(data, list):
        data = list(data)
        tdata = []

        for item in data:
            tdata.append(key_cleaner(item, char, repl))

        return tdata

    return data


def list_dirs(dir_path):

    """Function:  list_dirs

    Description:  Returns a list of directories within a directory.

    Arguments:
        (input) dir_path -> Directory path.
        (output) dir_list -> List of directory names.

    """

    if os.path.isdir(dir_path):
        dir_list = [item for item in os.listdir(dir_path)
                    if os.path.isdir(os.path.join(dir_path, item))]

    else:
        dir_list = []

    return dir_list


def list_files(dir_path, include_path=False):

    """Function:  list_files

    Description:  Get a list of file names in a directory and return as a list.

    Arguments:
        (input) dir_path -> Directory path.
        (input) include_path -> True|False - include dir path with file name.
        (output) List of file names.

    """

    if include_path:
        return [os.path.join(dir_path, item) for item in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, item))]

    return [item for item in os.listdir(dir_path)
            if os.path.isfile(os.path.join(dir_path, item))]


def list_filter_files(dir_path, file_filter):

    """Function:  list_filter_files

    Description:  Return a list of files from a directory folder with a file
        filter that will contain a file name or wildcard expansion file name.

    Arguments:
        (input) dir_path -> Directory path.
        (input) file_filter -> File name or wildcard expansion file name.
        (output) List of files that meet the criteria.

    """

    if not dir_path.endswith(os.path.sep):
        dir_path = dir_path + os.path.sep

    return glob.glob(dir_path + file_filter)


def list_2_dict(kv_list, fld_del="."):

    """Function:  list_2_dict

    Description:  Change a key.value list into a dictionary list.  The
        key_value is a list of keys and values delimited.  Values for the same
        key will be appended to the list for that key.

    Arguments:
        (input) kv_list -> Key_Value list.
        (input) fld_del -> Field delimiter for the split.
        (output) dict_list -> Dictionary list.

    """

    kv_list = list(kv_list)
    dict_list = {}

    for item in kv_list:
        dbs, tbl = item.split(fld_del)

        if dbs not in dict_list:
            dict_list[dbs] = [tbl]

        else:
            dict_list[dbs].append(tbl)

    return dict_list


def list_2_str(data_list, join_del=""):

    """Function:  list_2_str

    Description:  Convert a list to a string.  Will be joined together with a
        join delimiter.  The list can consist of strings or integers.

    Arguments:
        (input) data_list -> List to join.
        (input) join_del -> Join delimiter for the string.
        (output) join_str -> Join together string.

    """

    return join_del.join(str(item) for item in list(data_list))


def load_module(mod_name, mod_path):

    """Function:  load_module

    Description:  Load a Python module dynamically.

    Arguments:
        (input) mod_name -> Name of the module to load
        (input) mod_path -> Directory path to the module to load
        (output) Returns the module handler

    """

    sys.path.append(mod_path)
    return __import__(mod_name)


def make_dir(dirname):

    """Function:  make_dir

    Description:  Tries to create a directory and capture any exceptions.

    Arguments:
        (input) dirname -> Directory name
        (output) status -> True|False - If directory creation is succesful

    """

    status = False

    try:
        os.makedirs(dirname)
        status = True

    except OSError as err:
        if err.errno in (errno.EEXIST, errno.EACCES):
            print(f"Error:  {err.args[1]} for {dirname}")

        else:
            print(
                f"Error {err.args[0]}:  Message:  {err.args[1]} for {dirname}")

    return status


def make_md5_hash(file_path, to_file=True):

    """Function:  make_md5_hash

    Description:  Create a MD5 hash for a specify file and either return the
        hash of the file or write the hash to a file and return hash file name.

    Note:  The file the hash will be written to will be file_name.md5.txt.

    Arguments:
        (input) file_path -> Full path and file name being hashed
        (input) to_file -> True|False -> To write hash to a file
        (output) hash_results | hash_file -> Hash of the file/Hash file name

    """

    proc1 = subprocess.Popen(                           # pylint:disable=R1732
        ["/usr/bin/md5sum", file_path], stdout=subprocess.PIPE)
    hash_results, _ = proc1.communicate()
    encoding = chardet.detect(hash_results)["encoding"]
    hash_results = hash_results.decode(encoding)
    hash_results = hash_results.split("  ", maxsplit=1)[0]

    if to_file:
        hash_file = file_path + ".md5.txt"
        write_file(hash_file, "w", hash_results)

        return hash_file

    return hash_results


def make_zip(zip_file_path, cur_file_dir, files_to_zip, is_rel_path=False):

    """Function:  make_zip

    Description:  Zip up multiple files using absolute or relative paths.

    Arguments:
        (input) zip_file_path -> Destination zip file and path.
        (input) cur_file_dir -> Directory path to the source files.
        (input) files_to_zip -> List of files to be zipped.
        (input) is_rel_path -> True|False - Use relative paths in zip file.

    """

    files_to_zip = list(files_to_zip)
    newzip = None

    if not cur_file_dir.endswith(os.path.sep):
        cur_file_dir = cur_file_dir + os.path.sep

    try:
        newzip = zipfile.ZipFile(                   # pylint:disable=R1732
            zip_file_path, "w", zipfile.ZIP_DEFLATED)

        if is_rel_path:
            for fname in files_to_zip:
                newzip.write(cur_file_dir + fname, fname)

        else:
            for fname in files_to_zip:
                newzip.write(cur_file_dir + fname)

    finally:
        newzip.close()


def merge_data_types(data1, data2):

    """Function:  merge_data_types

    Description:  Merges two similar data type together.  The data types that
        can be merged are:  strings, dictionaries, lists, and tuples.

    Warning:  Unicode strings in Python 2.7 will not be detected as a string.

    Note:  Any duplicate keys between the two dictionaries will be overwritten
        by data_2 keys.

    Arguments:
        (input) data1 -> Data item.
        (input) data2 -> Data item.
        (output) data -> Merged data.
        (output) status -> True|False - Status of the merge.
        (output) err_msg -> Error message if merge fails.

    """

    status = True
    err_msg = ""
    data = None

    if isinstance(data1, str) \
       and (isinstance(data1, str) == isinstance(data2, str)):
        data = data1 + data2

    elif isinstance(data1, list) and (
       isinstance(data1, list) == isinstance(data2, list)):
        data = list(data1) + list(data2)

    elif isinstance(data1, tuple) and (
       isinstance(data1, tuple) == isinstance(data2, tuple)):
        data = data1 + data2

    elif isinstance(data1, dict) and (
       isinstance(data1, dict) == isinstance(data2, dict)):
        data, _, _ = merge_two_dicts(dict(data1), dict(data2))

    else:
        status = False
        err_msg = "Inconsistent data types or not correct data type"

    return data, status, err_msg


def merge_two_dicts(data_1, data_2):

    """Function:  merge_two_dicts

    Description:  Merges two dictionaries.

    Note:  Any duplicate keys between the two dictionaries will be overwritten
        by data_2 keys.

    Arguments:
        (input) data_1 -> Dictionary.
        (input) data_2 -> Dictionary.
        (output) data -> Merged dictionary.
        (output) status -> True|False - Status of the merge.
        (output) err_msg -> Error message if merge fails.

    """

    status = True
    err_msg = ""
    data = None

    if isinstance(data_1, dict) and isinstance(data_2, dict):
        data_1 = dict(data_1)
        data_2 = dict(data_2)
        data = data_1.copy()
        data.update(data_2)

    else:
        status = False
        err_msg = "One item isn't a dictionary or inconsistent data types"

    return data, status, err_msg


def milli_2_readadble(msecs):

    """Function:  milli_2_readadble

    Description:  Converts milliseconds into days, hours, minutes and seconds.
        Returns values with appropriate tags.

    Arguments:
        (input) msecs -> Milliseconds.

    """

    data = msecs // 1000
    seconds = data % 60
    data //= 60
    minutes = data % 60
    data //= 60
    hours = data % 24
    data //= 24
    days = data

    return f"{days} days {hours} hours {minutes} minutes {seconds} seconds"


def month_days(dtg):

    """Function:  month_days

    Description:  Return the number of days in the month for the date.

    Arguments:
        (input) dtg -> Is a datetime class instance.
        (output) -> Number of days in the month for the date.

    """

    return calendar.monthrange(dtg.year, dtg.month)[1]


def month_delta(date, delta):

    """Function:  month_delta

    Description:  Produces a month delta based on date passed to function.

    Arguments:
        (input) date -> Date time.
        (input) delta -> Delta on date time (i.e. -n...0...n).
        (output) month = Numeric month of the year.
        (outout) year = Numeric year in 4-digit format.

    """

    month, year = \
        (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12

    if not month:
        month = 12

    return month, year


def mv_file(fname, src_dir, dest_dir, new_fname=None):

    """Function:  mv_file

    Description:  Moves a file from a source directory to a destination
        directory and allows for the file to be renamed during the move.

        Note:  To rename a file or overwrite an existing file; pass in the
            new file name argument or add the file name to the destination
            path argument.

    Arguments:
        (input) fname -> File name.
        (input) src_dir -> Source directory.
        (input) dest_dir -> Destination directory.
        (input) new_fname -> New file name or None if staying the same.

    """

    if new_fname:
        dest_dir = os.path.join(dest_dir, new_fname)

    shutil.move(os.path.join(src_dir, fname), dest_dir)


def mv_file2(src_file_path, des_path, new_fname=None):

    """Function:  mv_file2

    Description:  Move a file from current location to a new location.  Also
        allows for file to be renamed during move and overwrite an existing
        file.

        Note:  To rename a file or overwrite an existing file; pass in the
            new file name argument or add the file name to the destination
            path argument.

    Arguments:
        (input) src_file_path -> Source directory path and file name.
        (input) des_path -> Destination directory path.
        (input) new_fname -> New file name/existing file name, if overwriting.

    """

    if new_fname:
        des_path = os.path.join(des_path, new_fname)

    shutil.move(src_file_path, des_path)


def normalize(rngs):

    """Function:  normalize

    Description:  Normalizes a list of ranges by merging ranges, if possible,
        and turning single-position ranges into tuples.  The normalization
        process is to sort the ranges first on the tuples, which makes
        comparsions easy when merging range sets.

    Arguments:
        (input) rng -> List of range sets.
        (output) result -> List of ordered range sets.

    """

    result = []
    last = None

    for rng in sorted(rngs):
        if len(rng) == 1:
            rng = (rng[0], rng[0])

        if last is None:
            last = rng

        elif rng[1] <= last[1]:
            continue

        elif rng[0] <= last[1] or last[1] + 1 >= rng[0]:
            last = (last[0], max(rng[1], last[1]))

        else:
            result.append(last)
            last = rng

    result.append(last)

    return result


def not_in_list(name, array_list):

    """Function:  not_in_list

    Description:  Checks to see if the a value is not in a list and either
        returns the value or an empty list.

    Arguments:
        (input) name -> Value
        (input) array_list -> Array List
        (output) Return name in a list or empty list

    """

    array_list = list(array_list)

    if name not in array_list:
        return [name]

    return []


@contextlib.contextmanager
def no_std_out():

    """Function Decorator:  no_std_out

    Description:  Suppresses standard output of a function.

    Arguments:  Function name passed to decorator using "with" statement

    Example:
        with no_std_out():
            function_name()

    """

    save_stdout = sys.stdout
    sys.stdout = io.StringIO()

    yield
    sys.stdout = save_stdout


def octal_to_str(octal):

    """Function:  octal_to_stropenfile

    Description:  Convert an octal number to a string representation of Linux
        file permissions.

    Arguments:
        (input) octal -> Octal number (i.e. 755, 644)
        (output) result -> String representation (i.e. rwxr-xr-x)

    """

    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]

    for digit in [int(n) for n in str(octal)]:

        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value

            else:
                result += '-'

    return result


def openfile(filename, mode="r"):

    """Function:  openfile

    Description:  Opens a normal file or compressed file and returns a file
        handler.

    Arguments:
        (input) filename -> Directory path and file name.
        (input) mode -> Type of operation allowed on the file (e.g. a, r, w).
        (output) File handler.

    """

    if filename.endswith(".gz"):
        return gzip.open(filename, mode)

    return open(filename, mode, encoding="UTF-8")


def pascalize(data_str):

    """Function:  pascalize

    Description:  Pascal cases a string.

    Arguments:
        (input) data_str -> String to be pascal cased.
        (output) Pascal cased string.

    """

    return "".join(item.capitalize() for item in re.split("([^a-zA-Z0-9])",
                                                          data_str)
                   if item.isalnum())


def pct_int(num1, num2, **kwargs):

    """Function:  pct_int

    Description:  Returns the precentage of two integers, will use floating
        division to allow the integers to given a proper return.

    Arguments:
        (input) num1 number -> First number.
        (input) num2 number -> Second number.
        (output) Return percentage.

    """

    return int(float_div(num1, num2, **kwargs) * 100)


def perm_check(item, item_type, f_hdlr=sys.stdout, **kwargs):

    """Function:  perm_check

    Description:  Checks for the permission settings (e.g. read, write,
        execute) on an object (e.g. file, directory, etc).  Results are
        returned via the f_hdlr setting and are also returned to the calling
        function.

    Arguments:
        (input) item -> Name of item to be checked, include full path
        (input) item_type -> What is the item (e.g. file, directory, etc)
        (input) f_hdlr -> File handler to write messages to or stdout
        (input) **kwargs:
            status -> Current status from calling function
            err_msg -> Current error messages from calling function
            read -> True|False - Is Readable on file
            write -> True|False - Is Writeable on file
            exe -> True|False - Is Executable on file
        (output) status -> True|False - False if one of the checks fails
        (output) err_msg -> Error message of check(s) that fail

    """

    status = kwargs.get("status", True)
    err_msg = kwargs.get("err_msg", "")
    read = kwargs.get("read", False)
    write = kwargs.get("write", False)
    exe = kwargs.get("exe", False)

    # Object writeable
    if write and not os.access(item, os.W_OK):
        tmp_msg = f"Error: {item_type} {item} is not writeable."
        print(tmp_msg, file=f_hdlr)
        err_msg = "\n".join([err_msg, tmp_msg])
        status = False

    # Object readable
    if read and not os.access(item, os.R_OK):
        tmp_msg = f"Error: {item_type} {item} is not readable."
        print(tmp_msg, file=f_hdlr)
        err_msg = "\n".join([err_msg, tmp_msg])
        status = False

    # Object executable
    if exe and not os.access(item, os.X_OK):
        tmp_msg = f"Error: {item_type} {item} is not executable."
        print(tmp_msg, file=f_hdlr)
        err_msg = "\n".join([err_msg, tmp_msg])
        status = False

    return status, err_msg


def print_data(data, mode="w", **kwargs):

    """Function:  print_data

    Description:  Opens a file to print or print to standard output
        (i.e. screen).

    Arguments:
        (input) data -> Data to be printed
        (input) mode -> w|a => Write or append mode
        (input) **kwargs:
            ofile -> Name of file to print to
            use_pprint -> True|False - Use Pretty Print instead of print

    """

    if "ofile" in kwargs and kwargs["ofile"]:
        outfile = open(                                 # pylint:disable=R1732
            kwargs.get("ofile"), mode, encoding="UTF-8")

    else:
        outfile = sys.stdout

    if kwargs.get("use_pprint", False):
        pprint.pprint(data, stream=outfile)

    else:
        print(data, file=outfile)

    if "ofile" in kwargs and kwargs["ofile"]:
        outfile.close()


def print_dict(data, ofile=None, json_fmt=False, no_std=False, mode="w",
               **kwargs):

    """Function:  print_dict

    Description:  Print dictionary to a file, standard out, and/or an email
        instance and in either JSON or standard format.

    Arguments:
        (input) data -> Dictionary document
        (input) ofile -> Name of output file name
        (input) json_fmt -> True|False - Print in JSON format
        (input) no_std -> True|False - Do not print to standard out
        (input) mode -> w|a => Write or append mode
        (input) kwargs:
            mail -> Mail instance
        (output) err_flag -> True|False - If error has occurred
        (output) err_msg -> None or error message

    """

    err_flag = False
    err_msg = None
    mail = kwargs.get("mail", None)

    if isinstance(data, dict):
        if ofile and json_fmt:
            print_data(json.dumps(data, indent=4), ofile=ofile, mode=mode,
                       **kwargs)

        elif ofile:
            dict_2_std(data, ofile=ofile, mode=mode, **kwargs)

        if not no_std and json_fmt:
            print_data(json.dumps(data, indent=4), **kwargs)

        elif not no_std:
            dict_2_std(data, ofile=False, **kwargs)

        if mail and json_fmt:
            mail.add_2_msg(json.dumps(data, indent=4))

        elif mail:
            mail.add_2_msg(data)

    else:
        err_flag = True
        err_msg = f"Error: {data} -> Is not a dictionary"

    return err_flag, err_msg


def print_list(data, **kwargs):

    """Function:  print_list

    Description:  Prints each item in a list on a seperate line to either a
        file or standard out.

    Arguments:
        (input) data -> List of data strings.
        (input) **kwargs:
            ofile -> Path and name of file to write to.
            mode -> a|w - File write mode.

    """

    data = list(data)
    mode = kwargs.get("mode", "w")
    ofile = kwargs.get("ofile", False)
    outfile = sys.stdout

    if ofile:
        outfile = open(ofile, mode, encoding="UTF-8")   # pylint:disable=R1732

    for line in data:
        print(line, file=outfile)

    if ofile:
        outfile.close()


def prt_dict(data, fhandler=sys.stdout, **kwargs):

    """Function:  prt_dict

    Description:  Convert Dict document to standard format and print to
        standard out or to a file.

    Arguments:
        (input) data -> JSON document.
        (input) outhldr -> File handler to standard out or a file.
        (input) kwargs:
            indent -> Level of indentation for printing.

    """

    data = dict(data)
    indent = kwargs.get("indent", 0)
    spc = " "

    for key, val in list(data.items()):

        if isinstance(val, dict):
            print(f"{spc * indent}{key}:", file=fhandler)
            prt_dict(val, fhandler, indent=indent + 4)

        else:
            print(f"{spc * indent}{key}:  {val}", file=fhandler)


def prt_lvl(lvl=1):

    """Function:  prt_lvl

    Description:  Setup a print command to start printing at a specified tab
        level.

    Arguments:
        (input) lvl -> Tab level to print to.

    """

    cnt = 0

    while cnt < lvl:
        print("\t", end="")
        cnt += 1


def prt_msg(hdr, msg, lvl=0):

    """Function:  prt_msg

    Description:  Prints a message with a Header followed by the Message.  Will
        also start printing at a certain printing level.

    Arguments:
        (input) hdr -> Header to print.
        (input) msg -> Message to print.
        (input) lvl -> Integer - Tab level to start printing at.

    """

    prt_lvl(lvl)
    print(f"{hdr}:  {msg}")


def rename_file(fname, new_fname, dir_path):

    """Function:  rename_file

    Description:  Rename a file name to new file name within a directory.

    Arguments:
        (input) fname -> Current file name.
        (input) new_fname -> New file name.
        (input) dir_path -> Directory path.

    """

    os.rename(os.path.join(dir_path, fname), os.path.join(dir_path, new_fname))


def rm_dup_list(orig_list):

    """Function:  rm_dup_list

    Description:  Remove duplicate entries in a list.

    Arguments:
        (input) orig_list -> List of elements to be processed
        (output) Returns an unique list

    """

    orig_list = list(orig_list)

    return list(set(orig_list))


def rm_file(file_path):

    """Function:  rm_file

    Description:  Remove a file, return error code and message, if necessary.

    Arguments:
        (input) file_path -> Full path and file name being hashed
        (output) err_flag -> True|False - An error has occurred during remove
        (output) err_msg -> Error message if an error has occurred

    """

    err_flag = False
    err_msg = None

    try:
        os.remove(file_path)

    except OSError as err:
        err_flag = True
        err_msg = f"Error: {err.filename} - {err.strerror}"

    return err_flag, err_msg


def rm_key(data, key):

    """Function:  rm_key

    Description:  Remove a key from a dictionary if it exists and return a
        copy of the modified dictionary.

    Arguments:
        (input) data -> Original dictionary
        (input) key -> Name of key to be removed
        (output) mod_data -> Modified dictionary of original dictionary

    """

    mod_data = dict(data)

    if key in mod_data:
        del mod_data[key]

    return mod_data


def rm_newline_list(orig_list):

    """Function:  rm_newline_list

    Description:  Remove newline at the end of each element in a list.

    Arguments:
        (input) orig_list -> List of elements to be processed.
        (output) Returns a list minus any newlines.

    """

    return [x.strip("\n") for x in orig_list]


def rm_whitespace(data):

    """Function:  rm_whitespace

    Description:  Remove white space from a data string.

    Arguments:
        (input) data -> Data string.
        (output) Data string minus any white spaces.

    """

    return data.replace(" ", "")


def root_run():

    """Function:  root_run

    Description:  Checks to see if the program is being run as root.  Using the
        effective user id for the check.

    Arguments:
        (output) True|False -> Returns True if running as root.

    """

    if os.geteuid() == 0:
        return True

    return False


def rotate_files(fname, cnt=0, max_cnt=5):

    """Function:  rotate_files

    Description:  Move a set of files up a sequence of backup files
        (e.g. file.0, file.1, file.2, etc).  It is a recursive function as it
        will find the largest sequence file or opening in the sequence and then
        rename the files appropriately.

    Arguments:
        (input) fname -> File name.
        (input) cnt -> Current sequence count.
        (input) max_cnt -> Largest sequence of files to use.

    """

    if cnt < max_cnt and os.path.isfile(fname + "." + str(cnt)):
        rotate_files(fname, cnt + 1, max_cnt)

        # Rename file to +1
        os.rename(fname + "." + str(cnt), fname + "." + str(cnt + 1))


def sec_2_hr(sec):

    """Function:  sec_2_hr

    Description:  Change seconds to hours.

    Arguments:
        (input) sec -> Number of seconds.
        (output) Number of hours out to 2 decimal points.

    """

    return (sec // 36) / float(100)


def str_2_list(del_str, fld_del):

    """Function:  str_2_list

    Description:  Converts a string delimited field to a list.

    Arguments:
        (input) del_str -> Delimited string.
        (input) fld_del -> Field delimiter.
        (output) List of values from the string.

    """

    return del_str.split(fld_del)


def str_2_type(lit_str):

    """Function:  str_2_type

    Description:  Converts a string to the container displayed in the literal.
        The only literal structures that can be converted to are: strings,
        numbers, tuples, lists, dicts, booleans, and None.

    Arguments:
        (input) lit_str -> Literal string to be converted
        (output) new_struct -> Structure the string was converted to

    """

    return ast.literal_eval(lit_str)


def touch(f_name):

    """Function:  touch

    Description:  Implements the Linux "touch" command.

    Arguments:
        (input) f_name -> File name, can include path name
        (output) status -> True|False -> True if successful
        (output) err_msg -> Error message or None

    """

    status = True
    err_msg = None
    base_dir = os.path.dirname(f_name)

    if not os.path.exists(base_dir):
        try:
            os.makedirs(base_dir)

        except OSError as err:
            status = False
            err_msg = f"ERROR: Directory create failure. Reason: {err.args[1]}"

    if status:
        try:
            with open(f_name, "a", encoding="UTF-8"):
                os.utime(f_name, None)

        except IOError as err:
            status = False
            err_msg = f"ERROR: File create failure. Reason: {err.args[1]}"

    return status, err_msg


def transpose_dict(data, data_key):

    """Function:  transpose_dict

    Description:  Transpose specified keys in a list of dictionaries
        to specified data types or None.

    Arguments:
        (input) data -> Initial list of dictionaries
        (input) data_key -> Dictionary of keys and data types
        (output) mod_data -> Modified list of dictionaries

    """

    data = list(data)
    data_key = dict(data_key)
    mod_data = []
    literal_list = ["bool", "list"]

    for list_item in data:
        list_item = dict(list_item)

        for item in set(list_item.keys()) & set(data_key.keys()):
            if not list_item[item] or list_item[item] == "None":
                list_item[item] = None

            elif data_key[item] == "int":
                list_item[item] = int(list_item[item])

            elif data_key[item] in literal_list:
                list_item[item] = ast.literal_eval(list_item[item])

        mod_data.append(list_item)

    return mod_data


def validate_date(dtg, **kwargs):

    """Function:  validate_date

    Description:  Check datetime value against format passed to the function or
        the default format.

    Arguments:
        (input) dtg -> Datetime group.
        (input) **kwargs:
            dtg_format -> Datetime format.
        (output) Return True|False.  False if time does not meet format.

    """

    dt_format = kwargs.get("dtg_format", "%Y-%m-%d %H:%M:%S")

    try:
        datetime.datetime.strptime(dtg, dt_format)
        return True

    except ValueError:
        return False


def validate_int(num):

    """Function:  validate_int

    Description:  Converts value to int and then check to see if it is an int.

    Arguments:
        (input) num -> Integer value for testing.
        (output) Return True|False.  False if value is not an integer.

    """

    try:
        isinstance(int(num), int)
        return True

    except ValueError:
        return False


def write_file(fname=None, mode="a", data=None):

    """Function:  write_file

    Description:  Write/append data to a file.

    Arguments:
        (input) fname -> File name.
        (input) mode -> w|a => Write or append mode.
        (input) data -> Data to be written.

    """

    if data and fname:
        with open(fname, mode, encoding="UTF-8") as f_hdlr:
            print(data, file=f_hdlr)


def write_file2(f_handle=None, line=None):

    """Function:  write_file2

    Description:  Write a string to a file handler.

    Arguments:
        (input) f_handle -> Name of file handler.
        (input) line -> Data to be written to file.

    """

    if line and f_handle:
        print(line, file=f_handle)


def write_to_log(f_hldr, text):

    """Function:  write_to_log

    Description:  Write a message to a log file with the following format:
        YYYY-MM-DDTHH:MM:SSZText
        NOTE:  There is no space between date and text unless added to text.

    Arguments:
        (input) f_hldr -> File handler.
        (input) text -> Message text to write to log.

    """

    write_file2(f_hldr, get_date() + "T" + get_time() + "Z" + text)
