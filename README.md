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
 * LogFile => Class that stores and manipulates log entries from files or standard in.  Stores log entries that allows for selective searching of log entries based on regex, keyword, and ignore.

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

# Unit test runs:
  * Replace **{Python_Project}** with the baseline path of the python program.

### All unit and code coverage testing for gen_libs.py:
```
cd {Python_Project}/python-lib
test/unit/gen_libs/unit_test_run.sh
test/unit/gen_libs/code_coverage.sh
```

### All unit and code coverage testing for arg_parser.py:
```
cd {Python_Project}/python-lib
test/unit/arg_parser/unit_test_run.sh
test/unit/arg_parser/code_coverage.sh
```

### All unit and code coverage testing for gen_class.py:
```
cd {Python_Project}/python-lib
test/unit/gen_class/unit_test_run.sh
test/unit/gen_class/code_coverage.sh
```

### All unit and code coverage testing for cmds_gen.py:
```
cd {Python_Project}/python-lib
test/unit/cmds_gen/unit_test_run.sh
test/unit/cmds_gen/code_coverage.sh
```

### All unit and code coverage testing for errors.py:
```
cd {Python_Project}/python-lib
test/unit/errors/unit_test_run.sh
test/unit/errors/code_coverage.sh
```

### All unit and code coverage testing for machine.py:
```
cd {Python_Project}/python-lib
test/unit/machine/unit_test_run.sh
test/unit/machine/code_coverage.sh
```

# Integration Testing:

### Description: Testing consists of integration testing for the functions in the library modules and methods in the classes.

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

# Integration test runs:
  * Replace **{Python_Project}** with the baseline path of the python program.

### All integration testing for arg_parser.py:
```
cd {Python_Project}/python-lib
test/unit/arg_parser/integration_test_run.sh
```

### All integration testing for gen_libs.py:
```
cd {Python_Project}/python-lib
test/unit/gen_libs/integration_test_run.sh
```

