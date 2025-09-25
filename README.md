# Python project that contains common libraries and classes for python programs.
# Classification (U)

# Description:
  Local python functions and classes that are available for general python use.


### This README file is broken down into the following sections:
 *  Prerequisites
 *  Installation
    - Pip Installation
 *  Testing
    - Unit
    - Integration


# Prerequisites

  * List of Linux packages that need to be installed on the server.
    - python3-pip
    - dnf


# Installation

### Pip Installation:

###### Create requirements file in another program's project to install python-lib as a library module.

  * Create requirements-python-lib.txt file.  Replace N.N.N with the version of the library needed.

```
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git@N.N.N#egg=python-lib' > requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file and the following lines to install the library modules:

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general python-lib requirements (requirements3.txt) to the other program's requirements3.txt file.


# Testing

### Git Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/python-lib.git
```

Install/upgrade system modules.
NOTE: Install as the user that will use the package.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
test/unit/gen_libs/unit_test_run.sh
test/unit/gen_class/unit_test_run.sh
test/unit/errors/unit_test_run.sh
test/unit/machine/unit_test_run.sh
test/unit/gen_libs/code_coverage.sh
test/unit/gen_class/code_coverage.sh
test/unit/errors/code_coverage.sh
test/unit/machine/code_coverage.sh
```

# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section under Unit Testing.

### Testing:

```
test/integration/gen_libs/integration_test_run.sh
```

