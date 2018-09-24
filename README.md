# Python project that contains common libraries and classes for python programs.
# Classification (U)

# Description:
  This project consists of a number of common local Python library, functions, and classes that are available for python programs to utilize.


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
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README and CHANGELOG files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

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


### Program:  gen_libs.py
##### Description:  A library program that contains a number of modules for general use.


### Program:  system.py
##### Description:  Class holding server system definitions.
##### Classes:
 * System => Class which is a representation of a Linux server.  A server object is used as a proxy for operating with the system.  The basic methods and attributes to contain information about the physical server.

 * Mail => Class which is a representation of an email.  An email object is used as a proxy for creating an email.  The basic methods and attributes include reading in the message, creating the message body, and sending the email.

 * Yum => Class which is a representation for YumBase system class.  A yum object is used as a proxy for using the yum command.  The basic methods and attributes include listing current repos, display current list of installed packages.

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
```

### Unit:  month_delta
```
test/unit/gen_libs/month_delta.py
```

### Unit:  file_search_cnt
```
test/unit/gen_libs/file_search_cnt.py
```

### Unit:  get_base_dir
```
test/unit/gen_libs/get_base_dir.py
```

### Unit:  no_std_out
```
test/unit/gen_libs/no_std_out.py
```

### Unit:  merge_two_dicts
```
test/unit/gen_libs/merge_two_dicts.py
```

### Unit:  merge_data_types
```
test/unit/gen_libs/merge_data_types.py
```

### Unit:  write_file
```
test/unit/gen_libs/write_file.py
```

### Unit:  display_data
```
test/unit/gen_libs/display_data.py
```

### Unit:  get_data
```
test/unit/gen_libs/get_data.py
```

### Unit:  clear_file
```
test/unit/gen_libs/clear_file.py
```

### Unit:  chk_crt_dir
```
test/unit/gen_libs/chk_crt_dir.py
```

### Unit:  chk_crt_file
```
test/unit/gen_libs/chk_crt_file.py
```

### Unit:  data_multi_out
```
test/unit/gen_libs/data_multi_out.py
```

### Unit:  file_search
```
test/unit/gen_libs/file_search.py
```

### Unit:  file_2_list
```
test/unit/gen_libs/file_2_list.py
```

### Unit:  is_empty_file
```
test/unit/gen_libs/is_empty_file.py
```

### Unit:  touch
```
test/unit/gen_libs/touch.py
```

### Unit:  list_dirs
```
test/unit/gen_libs/list_dirs.py
```

### Unit:  cp_file
```
test/unit/gen_libs/cp_file.py
```

### All unit testing for gen_libs.py:
```
test/unit/gen_libs/unit_test_run.sh
```


# Unit test runs for gen_class.py:

### Unit:  ProgressBar.__init__
```
test/unit/gen_class/ProgressBar_init.py
```

### Unit:  ProgressBar.update
```
test/unit/gen_class/ProgressBar_update.py
```

### Unit:  ProgressBar.calc_and_update
```
test/unit/gen_class/ProgressBar_calc_and_update.py
```

### Unit:  SingleInstanceException
```
test/unit/gen_class/SingleInstanceException.py
```

### Unit:  ProgramLock.__init__
```
test/unit/gen_class/ProgramLock_init.py
```

### Unit:  Yum.__init__
```
test/unit/gen_class/Yum_init.py
```

### Unit:  Yum.get_os
```
test/unit/gen_class/Yum_get_os.py
```

### Unit:  Yum.get_release
```
test/unit/gen_class/Yum_get_release.py
```

### Unit:  Yum.get_distro
```
test/unit/gen_class/Yum_get_distro.py
```

### All unit testing for gen_class.py:
```
test/unit/gen_class/unit_test_run.sh
```

