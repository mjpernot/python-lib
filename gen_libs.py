# Classification (U)

###############################################################################
#
# Filename:     gen_libs.py
#
# Class Dependencies:
#               None
#
# Library Dependenices:
#               None
#
###############################################################################

"""Program:  gen_libs.py

    Description:  A library program that contains a number of modules for
        general use.

    Functions:
        and_is_true
        bytes_2_readable
        chk_crt_dir
        chk_crt_file
        chk_int
        clear_file
        compress
        copy_tree
        cp_file
        cp_file2
        crt_file_time
        data_multi_out
        del_not_and_list
        del_not_in_list
        dict_2_list
        dict_2_std
        dir_file_match
        disk_usage
        display_data
        file_cleanup
        file_search
        file_search_cnt
        file_2_list
        float_div
        get_base_dir
        get_data
        get_date
        get_secs
        get_time
        help_func
        in_list
        is_empty_file
        is_missing_lists
        is_true
        key_cleaner
        list_dirs
        list_files
        list_filter_files
        list_2_dict
        load_module
        make_md5_hash
        make_zip
        merge_data_types
        merge_two_dicts
        milli_2_readadble
        month_delta
        mv_file
        mv_file2
        normalize
        not_in_list
        no_std_out
        pct_int
        print_data
        print_dict
        prt_dict
        prt_lvl
        prt_msg
        rename_file
        rm_dup_list
        rm_file
        rm_newline_list
        root_run
        rotate_files
        str_2_list
        str_2_type
        touch
        validate_date
        validate_int
        write_file
        write_file2
        write_to_log

        Chk_Crt_Dir (Deprecated)
        Chk_Crt_File (Deprecated)
        Close_File (deprecated)
        List_Filter_Files (deprecated)
        Load_Module (deprecated)
        Open_File (deprecated)
        Print_Data (deprecated)
        Prt_Lvl (deprecated)
        Prt_Msg (deprecated)

    Tuple:
        _ntuple_diskusage

"""

###############################################################################
# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import subprocess
import os
import time
import shutil
import datetime
import sys
import zipfile
import glob
import errno
import re
import collections
import contextlib
import io

# Third party
import json
import ast

# Local
import version

# Version Information
__version__ = version.__version__


# Tuples
_ntuple_diskusage = collections.namedtuple("usage", "total used free")


def and_is_true(x, y, **kwargs):

    """Function:  and_is_true

    Description:  Uses a truth table to do an AND check between two values of
        {Yes (True) / No (False)}.

    Arguments:
        (input) x -> Yes or No value.
        (input) y -> Yes or No value.
        (input) **kwargs:
            None
        (output) Return True | False based on AND comparsion.

    """

    truth_tbl = {"Yes": True, "No": False}

    return truth_tbl[x] and truth_tbl[y]


def bytes_2_readable(size, precision=2, **kwargs):

    """Function:  bytes_2_readable

    Description:  Converts a size (in bytes) in the appropriate readable size
        with post-tag symbol.

    Arguments:
        (input) size -> Size in bytes to convert.
        (input) precision -> Percision after decimal.
        (input) **kwargs:
            None

    """

    suffix = ["B", "KB", "MB", "GB", "TB"]
    suf_index = 0

    while size > 1024 and suf_index < 4:
        suf_index += 1
        size = size / 1024.0

    return "%.*f%s" % (precision, size, suffix[suf_index])


def chk_crt_dir(dir_name=None, create=False, write=False, read=False,
                f_hdlr=sys.stdout, **kwargs):

    """Function:  chk_crt_dir

    Description:  Check for the existence of a directory and whether to create
        one if not present.  Also checks the read and write permissions
        on the directory as determined by the arguments.

    Arguments:
        (input) dir_name -> Directory name.
        (input) create -> True|False - Create directory if not present.
        (input) write -> True|False - Is Writable on directory.
        (input) read -> True|False - Is Readable on directory.
        (input) f_hdlr -> File handler to write messages to or stdout.
        (input) **kwargs:
            no_print -> True|False - Suppress printing of error messages.
        (output) status -> True|False - False if one of the checks fails.
        (output) err_msg -> None|Error message of check that fails.

    """

    no_print = kwargs.get("no_print", False)
    status = True
    err_msg = None

    # Redirect print to /dev/null.
    if no_print:
        f_hdlr = open(os.devnull, "w")

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
                err_msg = "Error: Unable to create directory %s" % (dir_name)
                print(err_msg, file=f_hdlr)
                status = False

        # Directory does not exist.
        elif not os.path.isdir(dir_name):
            err_msg = "Error: Directory: %s does not exist." % (dir_name)
            print(err_msg, file=f_hdlr)
            status = False

        # Directory not writeable.
        elif write and not os.access(dir_name, os.W_OK):
            err_msg = "Error: Directory: %s is not writeable." % (dir_name)
            print(err_msg, file=f_hdlr)
            status = False

        # Directory not readable.
        elif read and not os.access(dir_name, os.R_OK):
            err_msg = "Error: Directory: %s is not readable." % (dir_name)
            print(err_msg, file=f_hdlr)
            status = False

    return status, err_msg


def chk_crt_file(f_name=None, create=False, write=False, read=False,
                 f_hdlr=sys.stdout, **kwargs):

    """Function:  chk_crt_file

    Description:  Check for the existence of a file and whether to create one
        if not present.  Also checks the read and write permissions on the file
        as determined by the arguments.

    Arguments:
        (input) f_name -> File name with directory path.
        (input) create -> True|False - Create file if not present.
        (input) write -> True|False - Is Writable on file.
        (input) read -> True|False - Is Readable on file.
        (input) f_hdlr -> File handler to write messages to or stdout.
        (input) **kwargs:
            no_print -> True|False - Suppress printing of error messages.
        (output) status -> True|False - False if one of the checks fails.
        (output) err_msg -> None|Error message of check that fails.

    """

    no_print = kwargs.get("no_print", False)
    status = True
    err_msg = None

    # Redirect print to /dev/null.
    if no_print:
        f_hdlr = open(os.devnull, "w")

    if not f_name.strip():
        err_msg = "Error:  No value passed for filename."
        print(err_msg, file=f_hdlr)
        status = False

    else:
        # Create empty file if requested.
        if create and not os.path.isfile(f_name):
            touch(f_name)

        # File does not exist.
        elif not os.path.isfile(f_name):
            err_msg = "Error:  File %s does not exist." % (f_name)
            print(err_msg, file=f_hdlr)
            status = False

        # File not writeable.
        if write and not os.access(f_name, os.W_OK):
            err_msg = "Error: File %s is not writable." % (f_name)
            print(err_msg, file=f_hdlr)
            status = False

        # File not readable.
        if read and not os.access(f_name, os.R_OK):
            err_msg = "Error: File %s is not readable." % (f_name)
            print(err_msg, file=f_hdlr)
            status = False

    if no_print:
        f_hdlr.close()

    return status, err_msg


def chk_int(x, **kwargs):

    """Function:  chk_int

    Description:  Checks to see if the string is an integer.
        NOTE:   Does not work for floats.

    Arguments:
        (input) x -> String containing an integer.
        (input) **kwargs:
            None
        (output) True|False -> Whether the string is an integer.

    """

    # Remove positive/negative sign if present.
    if x[0] in ("-", "+"):
        return x[1:].isdigit()

    return x.isdigit()


def clear_file(f_name, **kwargs):

    """Function:  clear_file

    Description:  Clear contents of an existing file or create a new file.

    Arguments:
        (input) f_name -> File name along with directory path.
        (input) **kwargs:
            None

    """

    open(f_name, "w").close()


def compress(fname, **kwargs):

    """Function:  compress

    Description:  Compress a file using gzip with a process call and wait until
        it completes.

    Arguments:
        (input) fname -> File name.
        (input) **kwargs:
            None

    """

    P1 = subprocess.Popen(["gzip", fname])
    P1.wait()


def copy_tree(src, dst, symlinks=False, ignore=None, **kwargs):

    """Function:  copy_tree

    Description:  Copies a directory tree recursively.  Will create the
        destination directory if not present.

    Arguments:
        (input) src -> Source directory.
        (input) dst -> Destination directory.
        (input) symlinks -> True|False is symbolic links are included.
        (input) ignore -> Function call with entries to be ignored.
        (input) **kwargs:
            None

    """

    # Source directory files.
    names = os.listdir(src)

    # Create ignore list if exists.
    if ignore is not None:
        ignored_names = ignore(src, names)

    else:
        ignored_names = set()

    if not os.path.isdir(dst):
        os.makedirs(dst)

    errors = []

    # Process items in directory.
    for name in names:

        if name in ignored_names:
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)

        try:
            # Symlink set and source name is link.
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)

            # Source is directory.
            elif os.path.isdir(srcname):
                copy_tree(srcname, dstname, symlinks, ignore)

            else:
                shutil.copy2(srcname, dstname)

        except (IOError, os.error) as msg:
            errors.append((srcname, dstname, str(msg)))

        except EnvironmentError as err:
            errors.append((srcname, dstname, str(err)))

        try:
            # File's statistics.
            shutil.copystat(src, dst)

        except OSError as msg:
            errors.append((src, dst, str(msg)))

        if errors:
            print(errors)


def cp_file(fname, src_dir, dest_dir, new_fname=None, **kwargs):

    """Function:  cp_file

    Description:  Copies a file from source directory to destination directory,
        permissions are copied as well (e.g. cp -p).  Allows for the file to be
        renamed in the process.
        NOTE:  Same as cp_file2 function, but this has exception handling for
            shutil.copy2 errors.

    Arguments:
        (input) fname -> File name.
        (input) src_dir -> Source directory.
        (input) dest_dir -> Destination directory.
        (input) new_fname -> New file name or None if staying the same.
        (input) **kwargs:
            None
        (output) status -> True|False - True if copy was successful.
        (output) err_msg -> Error message from shutil.copy2 exception or None.

    """

    status = True
    err_msg = None

    if new_fname:
        new_fname = os.path.join(dest_dir, new_fname)

    else:
        new_fname = dest_dir

    try:
        shutil.copy2(os.path.join(src_dir, fname), new_fname)

    except IOError as (errno, errmsg):
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


def cp_file2(fname, src_dir, dest_dir, new_fname=None, **kwargs):

    """Function:  cp_file2

    Description:  Copies a file from source directory to destination directory,
        but the permissions are copied as well (e.g. cp -p).  Allows for the
        file to be renamed in the process.
        NOTE:  This function does not deal with errors from shutil.copy2.  Use
            the cp_file function if error handling is required.

    Arguments:
        (input) fname -> File name.
        (input) src_dir -> Source directory.
        (input) dest_dir -> Destination directory.
        (input) new_fname -> New file name or None if staying the same.
        (input) **kwargs:
            None

    """

    if new_fname:
        dest_dir = os.path.join(dest_dir, new_fname)

    shutil.copy2(os.path.join(src_dir, fname), dest_dir)


def crt_file_time(fname, path, ext, **kwargs):

    """Function:  crt_file_time

    Description:  Creates a file name with timestamp along with directory path.

    Arguments:
        (input) fname -> File name.
        (input) path -> Directory path.
        (input) ext -> Extension of file.
        (input) **kwargs:
            None
        (output) -> Directory path/file_name.time.extension.

    """

    return path + fname + "." + time.strftime("%Y%m%d_%I%M") + ext


def data_multi_out(data, o_file=None, json_fmt=False, sup_std=False, MAIL=None,
                   **kwargs):

    """Function:  data_multi_out

    Description:  Send data to multiple outputs (e.g. file, mail,
        standard out).  Will also the ability to convert dictionaries to JSON
        format.

    Arguments:
        (input) data -> Data document.
        (input) o_file -> Directory_path/File_name|None: File name to write to.
        (input) json_fmt -> True|False - Convert data to JSON format.
        (input) sup_std -> True|False - Suppress printing to standard out.
        (input) MAIL -> Mail_class|None - Mail class instance.
        (input) **kwargs:
            None
        (output) err_flag -> True|False - Status of process.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None

    if json_fmt and isinstance(data, dict):
        data = json.dumps(data, indent=4)

    elif json_fmt:
        err_flag = True
        err_msg = "Error:  Unable to convert to JSON format, not a dictionary"

    if MAIL and isinstance(data, dict):
        MAIL.add_2_msg(json.dumps(data, indent=4) + '\n')

    elif MAIL:
        MAIL.add_2_msg(data)

    if o_file and not err_flag:
        write_file(o_file, "w", data)

    if not sup_std:
        print(data)

    return err_flag, err_msg


def del_not_and_list(list1, list2, **kwargs):

    """Function:  del_not_and_list

    Description:  Remove any items in list 1 that are present in list 2.

    Arguments:
        (input) list1 -> List array 1.
        (input) list2 -> List array 2 - items to be removed.
        (input) **kwargs:
            None
        (output) list1 -> List array 1 minus items from list array 2.

    """

    for x in list2:
        try:
            list1.remove(x)

        except ValueError:
            pass

    return list1


def del_not_in_list(list1, list2, **kwargs):

    """Function:  del_not_in_list

    Description:  Compares the first list with the second list and removes any
        items in the first list that are not in the second list. Intersects
        list 1 and list 2.

    Arguments:
        (input) list1 -> List 1.
        (input) list2 -> List 2.
        (input) **kwargs:
            None
        (output) list1 -> List 1 minus items not in list 2.

    """

    for x in list(set(list1) - set(list2)):
        list1.remove(x)

    return list1


def dict_2_list(dict_list, key_val, **kwargs):

    """Function:  dict_2_list

    Description:  Converts a dictionary array list to a array list, based on a
        key value passed to the function.  Only those values for the key value
        will be put into the list.

    Arguments:
        (input) dict_list -> Dictionary array list.
        (input) key_val -> Key value in the dictionary key.
        (input) **kwargs:
            None
        (output) arry_list -> Array list of values for key value.

    """

    return [row[key_val] for row in dict_list]


def dict_2_std(data, ofile=False, **kwargs):

    """Function:  dict_2_std

    Description:  Convert Dict document to standard format and print to
        standard out or file.

    Arguments:
        (input) data -> Dict document.
        (input) ofile -> Name of file to print to.
        (input) **kwargs:
            None.

    """

    if ofile:
        outfile = open(ofile, "w")

    else:
        outfile = sys.stdout

    prt_dict(data, outfile, **kwargs)

    if ofile:
        outfile.close()


def dir_file_match(dir_path, file_str, **kwargs):

    """Function:  dir_file_match

    Description:  Return a list of file names from a directory, but only those
        that match a search string.

    Arguments:
        (input) dir_path -> Directory path to search in.
        (input) file_str -> Name of search string.
        (input) **kwargs:
            None
        (output) Return a list of file names matching search string.

    """

    return [x for x in list_files(dir_path) if re.match(file_str, x)]


def disk_usage(path, **kwargs):

    """Function:  disk_usage

    Description:  Return in bytes a partition's total, used, and free space.

    Arguments:
        (input) path -> Directory path of the partition
        (input) **kwargs:
            None
        (output) _ntuple_diskusage (named tuple):
            total -> Total space in bytes
            used -> Used space in bytes
            free -> Free space in bytes

    """

    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize

    return _ntuple_diskusage(total, used, free)


def display_data(data, level=0, f_hdlr=sys.stdout, **kwargs):

    """Function:  display_data

    Description:  Breaks out a dictionary data structure into a readable
        format, prints to a file handler.

    Arguments:
        (input) data -> Dictionary data document.
        (input) level -> Number of tabs to print.
        (input) f_hdlr -> File handler (e.g. file or standard out).
        (input) **kwargs:
            None

    """

    if isinstance(data, dict):

        for item in data:

            # Recursive call for specific data types.
            if isinstance(data[item], (dict, list)):
                cnt = 0

                # Tab out.
                while (cnt < level):
                    print("\t", end="", file=f_hdlr)
                    cnt += 1

                print("%s =>" % item, file=f_hdlr)

                display_data(data[item], level + 1, f_hdlr=f_hdlr)

            else:
                cnt = 0

                # Tab out.
                while (cnt < level):
                    print("\t", end="", file=f_hdlr)
                    cnt += 1

                print("%s :  %s" % (item, data[item]), file=f_hdlr)

    # Recursive call for specific data types.
    elif isinstance(data, list):

        for item in data:
            display_data(item, level, f_hdlr=f_hdlr)

    else:
        cnt = 0

        # Tab out.
        while (cnt < level):
            print("\t", end="", file=f_hdlr)
            cnt += 1

        print("%s" % data, file=f_hdlr)


def file_cleanup(dir_path, days, **kwargs):

    """Function:  file_cleanup

    Description:  Removes all files in a directory over a specified number of
        days old.  Check is based on the last modified date for the file.

    Arguments:
        (input) dir_path -> Directory path.
        (input) days -> Number of days to be retained for.
        (input) **kwargs:
            None

    """

    today = time.time()

    for fname in os.listdir(dir_path):
        fullname = os.path.join(dir_path, fname)

        # Is it a file and over N days old.
        if os.path.isfile(fullname) \
           and os.stat(fullname).st_mtime < today - days * 86400:
            os.remove(fullname)


def file_search(f_name, string, **kwargs):

    """Function:  file_search

    Description:  Search for a string in a file and return the line it was
        found in a line.
        NOTE:  Returns only the first instance found in the file.

    Arguments:
        (input) f_name -> File name searching.
        (input) string -> Search string.
        (input) **kwargs:
            None
        (output) line - > Full line string was found in or None, if not found.

    """

    line = None

    with open(f_name, "r") as s_file:
        for x in s_file:
            if string in x:
                line = x
                break

    return line


def file_search_cnt(f_name, pattern, **kwargs):

    """Function:  file_search_cnt

    Description:  Search for a pattern in a file and count the number of lines
        the pattern is found in.

    Arguments:
        (input) f_name -> File name.
        (input) pattern -> Pattern searching for.
        (input) **kwargs:
            None
        (output) Number of lines found with the pattern in it.

    """

    return open(f_name, "r").read().count(pattern)


def file_2_list(filename, **kwargs):

    """Function:  file_2_list

    Description:  Reads in each line of a file and inserts into a list.
        NOTE: Will remove any newlines "\n" at the end of each line.

    Arguments:
        (input) filename -> File name to be read.
        (input) **kwargs:
            None
        (output) lines -> The file lines in a list.

    """

    with open(filename, "r") as f_hdlr:
        lines = [x.rstrip("\n") for x in f_hdlr.readlines()]

    return lines


def float_div(num1, num2, **kwargs):

    """Function:  float_div

    Description:  Takes two numbers and does floating division.  Returns zero
        if the divisor is zero.

    Arguments:
        (input) num1 number -> First number.
        (input) num2 number -> Second number.
        (input) **kwargs:
            None
        (output) Return results of division or 0.

    """

    try:
        return float(num1) / num2

    except ZeroDivisionError:
        return 0


def get_base_dir(f_name, **kwargs):

    """Function:  get_base_dir

    Description:  Return the base directory path of the file name.

    Arguments:
        (input) f_name -> File name.
        (input) **kwargs:
            None
        (output) Base directory path.

    """

    return os.path.dirname(os.path.realpath(f_name))


def get_data(f_hdlr, **kwargs):

    """Function:  get_data

    Description:  Reads a file into a list and strips off ending spaces/tabs.

    Arguments:
        (input) f_hdlr -> File handler.
        (input) **kwargs:
            None
        (output) List of all file entries.

    """

    return [x.rstrip() for x in f_hdlr]


def get_date(**kwargs):

    """Function:  get_date

    Description:  Return the current date in the YYYY-MM-DD format.

    Arguments:
        (input) **kwargs:
            None
        (output) Current system date.

    """

    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")


def get_secs(td, **kwargs):

    """Function:  get_secs

    Description:  Converts a datetime delta value to total number of seconds.

    Arguments:
        (input) td -> Datetime Delta.
        (input) **kwargs:
            None
        (output) -> Returns total number of seconds for datetime delta.

    """

    return (td.seconds + td.days * 24 * 3600) * 10**6 / 10**6


def get_time(**kwargs):

    """Function:  get_time

    Description:  Return the current time in the HH:MM:SS format.

    Arguments:
        (input) **kwargs:
            None
        (output) Current system time.

    """

    return datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")


def help_func(args_array, version, func_name=None, **kwargs):

    """Function:  help_func

    Description:  Checks for help arguments and calls the docstring of the
        passed function or print out the version.  Current options checked:
        -v (version) and -h (help)
        An exit flag (True) is passed to the calling program if one of the
        options is detected.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) version -> Version information on the calling program.
        (input) func_name -> Function that will contain help message.
        (input) **kwargs:
            None
        (output) Return True or False whether an option is detected.

    """

    exit_flag = False

    if "-h" in args_array:
        func_name()
        exit_flag = True

    if "-v" in args_array:
        print(version)
        exit_flag = True

    return exit_flag


def in_list(name, array_list, **kwargs):

    """Function:  in_list

    Description:  Checks to see if the a value is in a list and either returns
        the value or an empty list.

    Arguments:
        (input) name -> Value.
        (input) array_list -> Array List.
        (input) **kwargs:
            None
        (output) Return name in a list or empty list.

    """

    if name in array_list:
        return [name]

    else:
        return []


def is_empty_file(f_name, **kwargs):

    """Function:  is_empty_file

    Description:  Checks to see if a file is empty.
        NOTE:  Returns None if file does not exist.

    Arguments:
        (input) f_name -> File being checked.
        (input) **kwargs:
            None
        (output) status -> True|False|None -> True if file is empty.

    """

    if os.path.isfile(f_name):
        status = True if os.stat(f_name).st_size == 0 else False

    else:
        status = None

    return status


def is_missing_lists(list1, list2, **kwargs):

    """Function:  is_missing_lists

    Description:  Compares two lists and returns a list of missing values from
        list1 not found in list2.

    Arguments:
        (input) list1 -> List 1.
        (input) list2 -> List 2.
        (input) **kwargs:
            None
        (output) Return list of missing values.

    """

    return [x for x in list1 if x not in list2]


def is_true(x, **kwargs):

    """Function:  is_true

    Description:  Returns True or False for a Yes|No or ON|OFF value.  Uses a
        dictionary to determine the return value.

    Arguments:
        (input) x -> Yes or No value.
        (input) **kwargs:
            None
        (output) Return True | False based on truth_tbl.

    """

    truth_tbl = {"Yes": True, "No": False, "ON": True, "OFF": False}

    return truth_tbl[x]


def key_cleaner(data, char, repl, **kwargs):

    """Function:     key_cleaner

    Description:  Replace single character in dictionary key with a different
        character.  Recursive func call to parse through all levels of
        dictionary.

    Note:  Use for Mongodb as it does not allow . (periods) or $ (dollar signs)
        in the key of a document.

    Arguments:
        (input) data -> A dictionary object.
        (input) char -> Character to be replaced.
        (input) repl -> Replacement character.
        (input) **kwargs:
            None
        (output) data -> Modified dictionary object.

    """

    if type(data) is dict:

        for key, value in data.iteritems():

            # Recursive call on dictionary's value.
            data[key] = key_cleaner(value, char, repl)

            if "." in key:
                # Change key name and add new value.
                data[key.replace(char, repl)] = value
                del(data[key])

            return data

    if type(data) is list:
        return map(key_cleaner, data, char, repl)

    if type(data) is tuple:
        return tuple(map(key_cleaner, data, char, repl))

    return data


def list_dirs(dir_path, **kwargs):

    """Function:  list_dirs

    Description:  Returns a list of directories within a directory.

    Arguments:
        (input) dir_path -> Directory path.
        (input) **kwargs:
            None
        (output) dir_list -> List of directory names.

    """

    if os.path.isdir(dir_path):
        dir_list = [x for x in os.listdir(dir_path)
                    if os.path.isdir(os.path.join(dir_path, x))]

    else:
        dir_list = []

    return dir_list


def list_files(dir_path, **kwargs):

    """Function:  list_files

    Description:  Get a list of file names in a directory and return as a list.
        List will be returned as directory_path/file_name.

    Arguments:
        (input) dir_path -> Directory path.
        (input) **kwargs:
            None
        (output) file_names -> List of file names.

    """

    # Loop on directory and if an entry is a file then add to list.
    file_names = [x for x in os.listdir(dir_path)
                  if os.path.isfile(os.path.join(dir_path, x))]

    return file_names


def list_filter_files(dir_path, file_filter, **kwargs):

    """Function:  list_filter_files

    Description:  Return a list of files from a directory folder with a file
        filter that will contain a file name or wildcard expansion file name.

    Arguments:
        (input) dir_path -> Directory path.
        (input) file_filter -> File name or wildcard expansion file name.
        (input) **kwargs:
            None
        (output) List of files that meet the criteria.

    """

    if not dir_path.endswith(os.path.sep):
        dir_path = dir_path + os.path.sep

    return glob.glob(dir_path + file_filter)


def list_2_dict(kv_list, fld_del=".", **kwargs):

    """Function:  list_2_dict

    Description:  Change a key.value list into a dictionary list.  The
        key_value is a list of keys and values delimited.  Values for the same
        key will be appended to the list for that key.

    Arguments:
        (input) kv_list -> Key_Value list.
        (input) fld_del -> Field delimiter for the split.
        (input) **kwargs:
            None
        (output) dict_list -> Dictionary list.

    """

    dict_list = {}

    for x in kv_list:
        db, tbl = x.split(fld_del)

        if db not in dict_list:
            dict_list[db] = [tbl]

        else:
            dict_list[db].append(tbl)

    return dict_list


def load_module(mod_name, mod_path, **kwargs):

    """Function:  load_module

    Description:  Load a Python module dynamically.

    Arguments:
        (input) mod_name -> Name of the module to load.
        (input) mod_path -> Directory path to the module to load.
        (input) **kwargs:
            None
        (output) Returns the module handler.

    """

    sys.path.append(mod_path)
    return __import__(mod_name)


def make_md5_hash(file_path, to_file=True, **kwargs):

    """Function:  make_md5_hash

    Description:  Create a MD5 hash for a specify file and either return the
        hash of the file or write the hash to a file and return hash file name.

    Note:  The file the hash will be written to will be file_name.md5.txt.

    Arguments:
        (input) file_path -> Full path and file name being hashed.
        (input) to_file -> True|False -> To write hash to a file?
        (input) **kwargs:
            None
        (output) hash_results | hash_file -> Hash of the file/Hash file name.

    """

    P1 = subprocess.Popen(["/usr/bin/md5sum", file_path],
                          stdout=subprocess.PIPE)
    hash_results, status = P1.communicate()
    hash_results = hash_results.split("  ")[0]

    if to_file:
        hash_file = file_path + ".md5.txt"
        write_file(hash_file, "w", hash_results)

        return hash_file

    else:
        return hash_results


def make_zip(zip_file_path, cur_file_dir, files_to_zip, is_rel_path=False,
             **kwargs):

    """Function:  make_zip

    Description:  Zip up multiple files using absolute or relative paths.

    Arguments:
        (input) zip_file_path -> Destination zip file and path.
        (input) cur_file_dir -> Directory path to the source files.
        (input) files_to_zip -> List of files to be zipped.
        (input) is_rel_path -> True|False - Use relative paths in zip file.
        (input) **kwargs:
            None

    """

    newzip = None

    if not cur_file_dir.endswith(os.path.sep):
        cur_file_dir = cur_file_dir + os.path.sep

    try:
        newzip = zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED)

        if is_rel_path:
            for fname in files_to_zip:
                newzip.write(cur_file_dir + fname, fname)

        else:
            for fname in files_to_zip:
                newzip.write(cur_file_dir + fname)

    finally:
        newzip.close()


def merge_data_types(data_1, data_2, **kwargs):

    """Function:  merge_data_types

    Description:  Merges two similar data type together.  The data types that
        can be merged are:  strings, dictionaries, lists, and tuples.

    Note:  Any duplicate keys between the two dictionaries will be overwritten
        by data_2 keys.

    Arguments:
        (input) data_1 -> Data item.
        (input) data_2 -> Data item.
        (input) **kwargs:
            None
        (output) data -> Merged data.
        (output) status -> True|False - Status of the merge.
        (output) err_msg -> Error message if merge fails.

    """

    status = True
    err_msg = ""
    data = None

    if type(data_1) == type(data_2):

        if isinstance(data_1, (basestring, list, tuple)):
            data = data_1 + data_2

        elif isinstance(data_1, dict):
            data, _, _ = merge_two_dicts(data_1, data_2)

        else:
            status = False
            err_msg = "Not string, dictionary, list, or tuple data type"

    else:
        status = False
        err_msg = "Inconsistent data types"

    return data, status, err_msg


def merge_two_dicts(data_1, data_2, **kwargs):

    """Function:  merge_two_dicts

    Description:  Merges two dictionaries.

    Note:  Any duplicate keys between the two dictionaries will be overwritten
        by data_2 keys.

    Arguments:
        (input) data_1 -> Dictionary.
        (input) data_2 -> Dictionary.
        (input) **kwargs:
            None
        (output) data -> Merged dictionary.
        (output) status -> True|False - Status of the merge.
        (output) err_msg -> Error message if merge fails.

    """

    status = True
    err_msg = ""
    data = None

    if isinstance(data_1, dict) and type(data_1) == type(data_2):
        data = data_1.copy()
        data.update(data_2)

    else:
        status = False
        err_msg = "One item isn't a dictionary or inconsistent data types"

    return data, status, err_msg


def milli_2_readadble(ms, **kwargs):

    """Function:  milli_2_readadble

    Description:  Converts milliseconds into days, hours, minutes and seconds.
        Returns values with appropriate tags.

    Arguments:
        (input) ms -> Milliseconds.
        (input) **kwargs:
            None

    """

    x = ms / 1000
    seconds = x % 60
    x /= 60
    minutes = x % 60
    x /= 60
    hours = x % 24
    x /= 24
    days = x

    return "%d days %d hours %d minutes %d seconds" \
           % (days, hours, minutes, seconds)


def month_delta(date, delta, **kwargs):

    """Function:  month_delta

    Description:  Produces a month delta based on date passed to function.

    Arguments:
        (input) date -> Date time.
        (input) delta -> Delta on date time (i.e. -n...0...n).
        (input) **kwargs:
            None
        (output) month = Numeric month of the year.
        (outout) year = Numeric year in 4-digit format.

    """

    month, year = \
        (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12

    if not month:
        month = 12

    return month, year


def mv_file(fname, src_dir, dest_dir, new_fname=None, **kwargs):

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
        (input) **kwargs:
            None

    """

    if new_fname:
        dest_dir = os.path.join(dest_dir, new_fname)

    shutil.move(os.path.join(src_dir, fname), dest_dir)


def mv_file2(src_file_path, des_path, new_fname=None, **kwargs):

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
        (input) **kwargs:
            None

    """

    if new_fname:
        des_path = os.path.join(des_path, new_fname)

    shutil.move(src_file_path, des_path)


def normalize(rngs, **kwargs):

    """Function:  normalize

    Description:  Normalizes a list of ranges by merging ranges, if possible,
        and turning single-position ranges into tuples.  The normalization
        process is to sort the ranges first on the tuples, which makes
        comparsions easy when merging range sets.

    Arguments:
        (input) rng -> List of range sets.
        (input) **kwargs:
            None
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
            pass

        elif rng[0] <= last[1] or last[1] + 1 >= rng[0]:
            last = (last[0], max(rng[1], last[1]))

        else:
            result.append(last)
            last = rng

    result.append(last)

    return result


def not_in_list(name, array_list, **kwargs):

    """Function:  not_in_list

    Description:  Checks to see if the a value is not in a list and either
        returns the value or an empty list.

    Arguments:
        (input) name -> Value.
        (input) array_list -> Array List.
        (input) **kwargs:
            None
        (output) Return name in a list or empty list.

    """

    if name not in array_list:
        return [name]

    else:
        return []


@contextlib.contextmanager
def no_std_out():

    """Function Decorator:  no_std_out

    Description:  Suppresses standard output of a function.

    Arguments:  Function name passed to decorator using "with" statement.

    Example:
        with no_std_out():
            function_name()

    """

    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout


def pct_int(num1, num2, **kwargs):

    """Function:  pct_int

    Description:  Returns the precentage of two integers, will use floating
        division to allow the integers to given a proper return.

    Arguments:
        (input) num1 number -> First number.
        (input) num2 number -> Second number.
        (input) **kwargs:
            None
        (output) Return percentage.

    """

    return int(float_div(num1, num2, **kwargs) * 100)


def print_data(data, **kwargs):

    """Function:  print_data

    Description:  Opens a file to print or print to standard output
        (i.e. screen).

    Arguments:
        (input) data -> Data to be printed.
        (input) **kwargs:
            ofile -> Name of file to print to.

    """

    if "ofile" in kwargs and kwargs["ofile"]:
        outfile = open(kwargs.get("ofile"), "w")

    else:
        outfile = sys.stdout

    print(data, file=outfile)

    if "ofile" in kwargs and kwargs["ofile"]:
        outfile.close()


def print_dict(data, ofile=None, json_fmt=False, no_std=False, **kwargs):

    """Function:  print_dict

    Description:  Print dictionary to a file and/or standard out and in either
        JSON or standard format.

    Arguments:
        (input) data -> Dictionary document.
        (input) ofile -> Name of output file name.
        (input) json_fmt -> True|False - Print in JSON format.
        (input) no_std -> True|False - Do not print to standard out.
        (input) **kwargs:
            None
        (output) err_flag -> True|False - If error has occurred.
        (output) err_msg -> None or error message.

    """

    err_flag = False
    err_msg = None

    if isinstance(data, dict):
        if ofile and json_fmt:
            print_data(json.dumps(data, indent=4), ofile=ofile, **kwargs)

        elif ofile:
            dict_2_std(data, ofile=ofile, **kwargs)

        if not no_std and json_fmt:
            print_data(json.dumps(data, indent=4), **kwargs)

        elif not no_std:
            dict_2_std(data, ofile=False, **kwargs)

    else:
        err_flag = True
        err_msg = "Error: %s -> Is not a dictionary" % (data)

    return err_flag, err_msg


def prt_dict(data, fhandler=sys.stdout, **kwargs):

    """Function:  prt_dict

    Description:  Convert Dict document to standard format and print to
        standard out or to a file.

    Arguments:
        (input) data -> JSON document.
        (input) outhldr -> File handler to standard out or a file.
        (input) **kwargs:
            None.

    """

    for x, y in data.iteritems():

        if isinstance(y, dict):
            prt_dict(y, fhandler, **kwargs)

        else:
            print("{0}:  {1}".format(x, y), file=fhandler)


def prt_lvl(lvl=1, **kwargs):

    """Function:  prt_lvl

    Description:  Setup a print command to start printing at a specified tab
        level.

    Arguments:
        (input) lvl -> Tab level to print to.
        (input) **kwargs:
            None

    """

    cnt = 0

    while (cnt < lvl):
        print("\t", end="")
        cnt += 1


def prt_msg(hdr, msg, prt_lvl=0, **kwargs):

    """Function:  prt_msg

    Description:  Prints a message with a Header followed by the Message.  Will
        also start printing at a certain printing level.

    Arguments:
        (input) hdr -> Header to print.
        (input) msg -> Message to print.
        (input) prt_lvl -> Integer - Tab level to start printing at.
        (input) **kwargs:
            None

    """

    prt_lvl(prt_lvl)
    print("{0}:  {1}".format(hdr, msg))


def rename_file(fname, new_fname, dir_path, **kwargs):

    """Function:  rename_file

    Description:  Rename a file name to new file name within a directory.

    Arguments:
        (input) fname -> Current file name.
        (input) new_fname -> New file name.
        (input) dir_path -> Directory path.
        (input) **kwargs:
            None

    """

    os.rename(os.path.join(dir_path, fname), os.path.join(dir_path, new_fname))


def rm_dup_list(orig_list, **kwargs):

    """Function:  rm_dup_list

    Description:  Remove duplicate entries in a list.

    Arguments:
        (input) orig_list -> List of elements to be processed.
        (input) **kwargs:
            None
        (output) Returns an unique list.

    """

    return list(set(orig_list))


def rm_file(file_path, **kwargs):

    """Function:  rm_file

    Description:  Remove a file, return error code and message, if necessary.

    Arguments:
        (input) file_path -> Full path and file name being hashed.
        (input) **kwargs:
            None
        (output) err_flag -> True|False - An error has occurred during remove.
        (output) err_msg -> Error message if an error has occurred.

    """

    err_flag = False
    err_msg = None

    try:
        os.remove(file_path)

    except OSError as err:
        err_flag = True
        err_msg = "Error: %s - %s" % (err.filename, err.strerror)

    return err_flag, err_msg


def rm_newline_list(orig_list, **kwargs):

    """Function:  rm_newline_list

    Description:  Remove newline at the end of each element in a list.

    Arguments:
        (input) orig_list -> List of elements to be processed.
        (input) **kwargs:
            None
        (output) Returns a list minus any newlines.

    """

    return [x.strip("\n") for x in orig_list]


def root_run(**kwargs):

    """Function:  root_run

    Description:  Checks to see if the program is being run as root.  Using the
        effective user id for the check.

    Arguments:
        (input) **kwargs:
            None
        (output) True|False -> Returns True if running as root.

    """

    if os.geteuid() == 0:
        return True

    else:
        return False


def rotate_files(fname, cnt=0, max_cnt=5, **kwargs):

    """Function:  rotate_files

    Description:  Move a set of files up a sequence of backup files
        (e.g. file.0, file.1, file.2, etc).  It is a recursive function as it
        will find the largest sequence file or opening in the sequence and then
        rename the files appropriately.

    Arguments:
        (input) fname -> File name.
        (input) cnt -> Current sequence count.
        (input) max_cnt -> Largest sequence of files to use.
        (input) **kwargs:
            None

    """

    if cnt < max_cnt:

        if os.path.isfile(fname + "." + str(cnt)):
            rotate_files(fname, cnt + 1, max_cnt)

            # Rename file to + 1.
            os.rename(fname + "." + str(cnt), fname + "." + str(cnt + 1))


def str_2_list(del_str, fld_del, **kwargs):

    """Function:  str_2_list

    Description:  Converts a string delimited field to a list.

    Arguments:
        (input) del_str -> Delimited string.
        (input) fld_del -> Field delimiter.
        (input) **kwargs:
            None
        (output) new_list -> List of values from the string.

    """

    new_list = del_str.split(fld_del)

    return new_list


def str_2_type(lit_str, **kwargs):

    """Function:  str_2_type

    Description:  Converts a string to the container displayed in the literal.
        The only literal structures that can be converted to are: strings,
        numbers, tuples, lists, dicts, booleans, and None.

    Arguments:
        (input) lit_str -> Literal string to be converted.
        (input) **kwargs:
            None
        (output) new_struct -> Structure the string was converted to.

    """

    return ast.literal_eval(lit_str)


def touch(f_name, **kwargs):

    """Function:  touch

    Description:  Implements the Linux "touch" command.

    Arguments:
        (input) f_name -> File name, can include path name.
        (input) **kwargs:
            None
        (output) status -> True|False -> True if successful.
        (output) err_msg -> Error message or None.

    """

    status = True
    err_msg = None
    base_dir = os.path.dirname(f_name)

    # Create directory path.
    if not os.path.exists(base_dir):
        try:
            os.makedirs(base_dir)

        except OSError as (errno, strerror):
            status = False
            err_msg = "ERROR: Directory create failure. Reason: %s" \
                      % (strerror)

    if status:
        try:
            # Do not overwrite if it exists.
            with open(f_name, "a"):
                os.utime(f_name, None)

        except IOError as (errno, strerror):
            status = False
            err_msg = "ERROR: File create failure. Reason: %s" % (strerror)

    return status, err_msg


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


def validate_int(num, **kwargs):

    """Function:  validate_int

    Description:  Converts value to int and then check to see if it is an int.

    Arguments:
        (input) num -> Integer value for testing.
        (input) **kwargs:
            None
        (output) Return True|False.  False if value is not an integer.

    """

    try:
        isinstance(int(num), int)
        return True

    except ValueError:
        return False


def write_file(fname=None, mode="a", data=None, **kwargs):

    """Function:  write_file

    Description:  Write/append data to a file.

    Arguments:
        (input) fname -> File name.
        (input) mode -> w|a => Write or append mode.
        (input) data -> Data to be written.
        (input) **kwargs:
            None

    """

    if data and fname:
        with open(fname, mode) as f_hdlr:
            print(data, file=f_hdlr)


def write_file2(f_handle=None, line=None, **kwargs):

    """Function:  write_file2

    Description:  Write a string to a file handler.

    Arguments:
        (input) f_handle -> Name of file handler.
        (input) line -> Data to be written to file.
        (input) **kwargs:
            None

    """

    if line and f_handle:
        print(line, file=f_handle)


def write_to_log(f_hldr, text, **kwargs):

    """Function:  write_to_log

    Description:  Write a message to a log file with the following format:
        YYYY-MM-DDTHH:MM:SSZText
        NOTE:  There is no space between date and text unless added to text.

    Arguments:
        (input) f_hldr -> File handler.
        (input) text -> Message text to write to log.
        (input) **kwargs:
            None

    """

    write_file2(f_hldr, get_date() + "T" + get_time() + "Z" + text)


def Load_Module(mod_name, mod_path):

    """Function:  Load_Module (deprecated)

    Description:  Load a Python module dynamically.

    Arguments:
        (input) mod_name -> Name of the module to load.
        (input) mod_path -> Directory path to the module to load.
        (output) Returns the module handler.

    """

    sys.path.append(mod_path)
    return __import__(mod_name)


def Prt_Lvl(lvl=1):

    """Function:  Prt_Lvl (deprecated)

    Description:  Setup a print command to start printing at a specified tab
        level.

    Arguments:
        (input) lvl -> Tab level to print to.

    """

    cnt = 0

    while (cnt < lvl):
        print("\t", end="")
        cnt += 1


def Prt_Msg(hdr, msg, prt_lvl=0):

    """Function:  Prt_Msg (deprecated)

    Description:  Prints a message with a Header followed by the Message.  Will
        also start printing at a certain printing level.

    Arguments:
        (input) hdr -> Header to print.
        (input) msg -> Message to print.
        (input) prt_lvl -> Integer - Tab level to start printing at.

    """

    Prt_Lvl(prt_lvl)
    print("{0}:  {1}".format(hdr, msg))


def Print_Data(data, **kwargs):

    """Function:  Print_Data (deprecated)

    Description:  Opens a file to print or print to standard output
        (i.e. screen).

    Arguments:
        (input) data -> Data to be printed.
        (input) **kwargs:
            ofile -> Name of file to print to.

    """

    if "ofile" in kwargs and kwargs["ofile"]:
        outfile = open(kwargs.get("ofile"), "w")

    else:
        outfile = sys.stdout

    print(data, file=outfile)

    if "ofile" in kwargs and kwargs["ofile"]:
        outfile.close()


def Chk_Crt_Dir(dir_name=None, create=False, write=False, read=False,
                log_hldr=sys.stdout, **kwargs):

    """Function:  Chk_Crt_Dir

    Warning:  Function has been deprecated, replaced by gen_libs.chk_crt_dir.

    Description:  Check for the existence of a directory and whether to create
        one if not present.  If present, checks the read and write permissions
        on the directory as determined by the arguments.

    Arguments:
        (input) dir_name -> Directory name.
        (input) create -> True|False - Create directory if not present.
        (input) write -> True|False - Is Writable on directory.
        (input) read -> True|False - Is Readable on directory.
        (input) log_hldr -> File handler to write messages to or stdout.
        (input) **kwargs:
            None
        (output) d_flag -> True|False - False if one of the checks fails.

    """

    d_flag = True

    if not dir_name.strip():
        print("Error:  No value passed for filename.", file=log_hldr)
        d_flag = False

    else:
        # Directory not exist and create flag set.
        if not os.path.isdir(dir_name) and create:
            try:
                os.makedirs(dir_name)

            except:
                print("Error: Unable to create directory {0}".format(dir_name),
                      file=log_hldr)
                d_flag = False

        # Directory not exist.
        elif not os.path.isdir(dir_name):
            print("Error: Directory {0} does not exist.".format(dir_name),
                  file=log_hldr)
            d_flag = False

        # Write flag set and directory not writeable.
        elif write and not os.access(dir_name, os.W_OK):
            print("Error: Directory {0} is not writeable.".format(dir_name),
                  file=log_hldr)
            d_flag = False

        # Read flag set and directory not readable.
        elif read and not os.access(dir_name, os.R_OK):
            print("Error: Directory {0} is not readable.".format(dir_name),
                  file=log_hldr)
            d_flag = False

    return d_flag


def Chk_Crt_File(f_name=None, create=False, write=False, read=False,
                 log_hldr=sys.stdout, **kwargs):

    """Function:  Chk_Crt_File

    Warning:  Function has been deprecated, replaced by gen_libs.chk_crt_file.

    Description:  Check for the existence of a file and see if the file is
        writeable and/or readable depending on the arguments passed.  Will
        create the file if the file does not exist and has the 'create' option
        turned on.

    Arguments:
        (input) f_name -> File name with directory path.
        (input) create -> True|False - Create file if not present.
        (input) write -> True|False - Is Writable on file.
        (input) read -> True|False - Is Readable on file.
        (input) log_hldr -> File handler to write messages to or stdout.
        (input) **kwargs:
            None
        (output) f_flag -> True|False - False if one of the checks fails.

    """

    f_flag = True

    if not f_name.strip():
        print("Error:  No value passed for filename.", file=log_hldr)
        f_flag = False

    else:
        # Create flag set and file not exist.
        if create and not os.path.isfile(f_name):
            f_hdlr = Open_File(f_name, "w")
            Close_File(f_hdlr)

        # File not exist.
        elif not os.path.isfile(f_name):
            print("Error:  File {0} does not exist.".format(f_name),
                  file=log_hldr)
            f_flag = False

        # Write flag set and file not writeable.
        if write and not os.access(f_name, os.W_OK):
            print("Error: File {0} is not writable.".format(f_name),
                  file=log_hldr)
            f_flag = False

        # Read flag set and file not readable.
        if read and not os.access(f_name, os.R_OK):
            print("Error: File {0} is not readable.".format(f_name),
                  file=log_hldr)
            f_flag = False

    return f_flag


def Open_File(fname, mode, **kwargs):

    """Function:  Open_File (deprecated)

    Description:  Open a file in read, write, or append mode.

    Arguments:
        (input) fname -> Full directory path and file name.
        (input) mode -> r|w|a: Read, write, or append mode.
        (input) **kwargs:
            None
        (output) Return file handler.

    """

    return open(fname, mode)


def Close_File(f_handle, **kwargs):

    """Function:  Close_File (deprecated)

    Description:  Close a file handler.

    Arguments:
        (input) f_handle -> Name of file handler.
        (input) **kwargs:
            None.

    """

    f_handle.close()


def List_Filter_Files(dir_path, file_filter, **kwargs):

    """Function:  List_Filter_Files (deprecated)

    Description:  Return a list of files from a directory folder with a file
        filter that will contain a file name or wildcard expansion file name.

    Arguments:
        (input) dir_path -> Directory path.
        (input) file_filter -> File name or wildcard expansion file name.
        (input) **kwargs:
            None
        (output) List of files that meet the criteria.

    """

    if not dir_path.endswith(os.path.sep):
        dir_path = dir_path + os.path.sep

    return glob.glob(dir_path + file_filter)