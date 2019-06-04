# Python project that contains common libraries and classes for python programs.
# Classification (U)

# Description:
  This project consists of a number of common local python functions and classes that are available for use.


### This README file is broken down into the following sections:
 *  Prerequisites
 *  Installation
 *  Program Descriptions
 *  Testing
    - Unit


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip


# Installation
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README.md and CHANGELOG.md files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirements-python-lib.txt file in another program's project.

```
echo "git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git#egg=python-lib" >> {Other_Python_Project}/requirements-python-lib.txt
```

Place the following command into the another program's README.md file under the "Install supporting classes and libraries" section.
   pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the general Python library requirements.txt to the another program's requirements.txt file and remove any duplicates.

```
cat requirements.txt >> {Other_Python_Project}/requirements.txt
vim {Other_Python_Project}/requirements.txt
```

### Git Installation:

Install general Python libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/python-lib.git
```

Install/upgrade system modules.

```
cd python-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


# Program Descriptions:
### Program:  gen_class.py
##### Description:  Class that has class definitions for general use.
##### Classes:
 * ProgressBar => Class that displays and updates a progress bar for an ongoing operation.

 * ProgramLock => Class that creates a file lock instance and in which other programs using the same parameters will detect the lock as already present and prevent a second program instance from starting.

 * SingleInstanceException => Class for detecting when a ProgramLock has been previously created.

 * Logger => Class which is a representation of a log file instance.  A Logger object is used as a proxy to implement the creation, formatting, writing to, and closing of a log file.

 * System => Class which is a representation of a Linux server.  A server object is used as a proxy for operating with the system.  The basic methods and attributes to contain information about the physical server.

 * Mail => Class which is a representation of an email.  An email object is used as a proxy for creating an email.  The basic methods and attributes include reading in the message, creating the message body, and sending the email.

 * Yum => Class which is a representation for YumBase system class.  A yum object is used as a proxy for using the yum command.  The basic methods and attributes include listing current repos, display current list of installed packages.

 * Daemon =>  Class that creates and runs a Python program as a daemon program in include starting, stopping and restarting the process.


### Program:  gen_libs.py
##### Description:  A library program that contains a number of modules for general use.


### Program:  system.py
##### Description:  Class holding server system definitions.
##### Classes:
 * System => Class which is a representation of a Linux server.  A server object is used as a proxy for operating with the system.  The basic methods and attributes to contain information about the physical server.

 * Graph => Class which is a representation of a graph plot process.  A graph plot object is used as a proxy for processing graph plots.  The basic methods and attributes include file and directory information and settings.

 * F_Graph => Class which is a representation of a file in the graph plot process.  A file graph object is used as a proxy for file name graph plots.  The basic methods and attributes include processing file names, parsing file names, setting target names, add, delete, and update file names and directories, and file processing status.


### Program:  arg_parser.py
##### Description:  A library program that contains a number of modules that parse the argument list on the command line.


### Program:  cmds_gen.py
##### Description:  Library of general function calls that can be used by different classes.  These methods are general use and can be used by a variety of classes as long as  they follow the same standard.


### Program:  errors.py
##### Description:  Base class for the server class exception errors.


### Program:  machine.py
##### Description:  Base class for all machines.  This class has the methods for accomplishing tasks on different o/s platforms.


# Testing

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the library modules and methods in the classes.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/python-lib.git
```

Install/upgrade system modules.

```
cd python-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

# Unit test runs for gen_libs.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/python-lib
test/unit/gen_libs/month_delta.py
test/unit/gen_libs/file_search_cnt.py
test/unit/gen_libs/get_base_dir.py
test/unit/gen_libs/no_std_out.py
test/unit/gen_libs/merge_two_dicts.py
test/unit/gen_libs/merge_data_types.py
test/unit/gen_libs/write_file.py
test/unit/gen_libs/display_data.py
test/unit/gen_libs/get_data.py
test/unit/gen_libs/clear_file.py
test/unit/gen_libs/chk_crt_dir.py
test/unit/gen_libs/chk_crt_file.py
test/unit/gen_libs/data_multi_out.py
test/unit/gen_libs/file_search.py
test/unit/gen_libs/file_2_list.py
test/unit/gen_libs/is_empty_file.py
test/unit/gen_libs/touch.py
test/unit/gen_libs/list_dirs.py
test/unit/gen_libs/cp_file.py
test/unit/gen_libs/rotate_files.py
test/unit/gen_libs/bytes_2_readable.py
test/unit/gen_libs/chk_int.py
test/unit/gen_libs/del_not_in_list.py
test/unit/gen_libs/pct_int.py
test/unit/gen_libs/print_data.py
test/unit/gen_libs/print_dict.py
test/unit/gen_libs/prt_dict.py
test/unit/gen_libs/prt_lvl.py
test/unit/gen_libs/prt_msg.py
test/unit/gen_libs/rename_file.py
test/unit/gen_libs/rm_dup_list.py
test/unit/gen_libs/rm_file.py
test/unit/gen_libs/rm_newline_list.py
test/unit/gen_libs/root_run.py
test/unit/gen_libs/str_2_list.py
test/unit/gen_libs/str_2_type.py
test/unit/gen_libs/validate_date.py
test/unit/gen_libs/validate_int.py
test/unit/gen_libs/write_file2.py
test/unit/gen_libs/write_to_log.py
```

### All unit testing for gen_libs.py:
```
cd {Python_Project}/python-lib
test/unit/gen_libs/unit_test_run.sh
```


# Unit test runs for arg_parser.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/python-lib
test/unit/arg_parser/arg_add_def.py
test/unit/arg_parser/arg_cond_req.py
test/unit/arg_parser/arg_cond_req_or.py
test/unit/arg_parser/arg_default.py
test/unit/arg_parser/arg_dir_chk_crt.py
test/unit/arg_parser/arg_file_chk.py
test/unit/arg_parser/arg_noreq_xor.py
test/unit/arg_parser/arg_parse2.py
test/unit/arg_parser/arg_require.py
test/unit/arg_parser/arg_req_or_lst.py
test/unit/arg_parser/arg_req_xor.py
test/unit/arg_parser/arg_set_path.py
test/unit/arg_parser/arg_validate.py
test/unit/arg_parser/arg_valid_val.py
test/unit/arg_parser/arg_wildcard.py
test/unit/arg_parser/arg_xor_dict.py
test/unit/arg_parser/parse_multi.py
test/unit/arg_parser/parse_single.py
test/unit/arg_parser/file_create.py
```

### All unit testing for arg_parser.py:
```
cd {Python_Project}/python-lib
test/unit/arg_parser/unit_test_run.sh
```


# Unit test runs for gen_class.py:

```
cd {Python_Project}/python-lib
test/unit/gen_class/ProgressBar_init.py
test/unit/gen_class/ProgressBar_update.py
test/unit/gen_class/ProgressBar_calc_and_update.py
test/unit/gen_class/SingleInstanceException.py
test/unit/gen_class/ProgramLock_init.py
test/unit/gen_class/Yum_init.py
test/unit/gen_class/Yum_get_os.py
test/unit/gen_class/Yum_get_release.py
test/unit/gen_class/Yum_get_distro.py
test/unit/gen_class/Yum_fetch_install_pkgs.py
test/unit/gen_class/Yum_fetch_update_pkgs.py
```

### All unit testing for gen_class.py:
```
cd {Python_Project}/python-lib
test/unit/gen_class/unit_test_run.sh
```

