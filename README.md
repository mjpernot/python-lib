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
 *  If the platform is Redhat 8 and above, list of Linux packages that need to be installed on the server.
    - dnf==4.7.0


# Installation

### Pip Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python lib project and any reference to **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install python-lib as a library module.

Create requirements-python-lib.txt file.  This will require access to a clone of the python-lib project.

```
cp {Python_Project}/python-lib/requirements-python-lib.txt {Other_Python_Project}/requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Centos 7 (Running Python 2.7):
Modify the {Other_Python_Project}/README.md file:

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
Modify the {Other_Python_Project}/README.md file:

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general python-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Centos 7 (Running Python 2.7):
Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

```
chardet==3.0.4
distro==1.6.0
email==4.0.3
simplejson==2.0.9
```

Redhat 8 (Running Python 3.6):
Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

```
chardet==3.0.4
distro==1.6.0
simplejson==3.12.0
```


### Git Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/python-lib.git
```

Install/upgrade system modules.

Centos 7 (Running Python 2.7):

```
sudo pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
NOTE: Install as the user that will use the package.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Testing

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

Centos 7 (Running Python 2.7):

```
cd python-lib
test/unit/gen_libs/unit_test_run.sh
test/unit/arg_parser/unit_test_run.sh
test/unit/gen_class/unit_test_run.sh
test/unit/errors/unit_test_run.sh
test/unit/machine/unit_test_run.sh
```

Redhat 8 (Running Python 3.6):

```
cd python-lib
test/unit/gen_libs/unit_test_run3.sh
test/unit/arg_parser/unit_test_run3.sh
test/unit/gen_class/unit_test_run3.sh
test/unit/errors/unit_test_run3.sh
test/unit/machine/unit_test_run3.sh
```

### Code Coverage:

```
cd python-lib
test/unit/gen_libs/code_coverage.sh
test/unit/arg_parser/code_coverage.sh
test/unit/gen_class/code_coverage.sh
test/unit/errors/code_coverage.sh
test/unit/machine/code_coverage.sh
```

# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section under Unit Testing.

### Testing:

Centos 7 (Running Python 2.7):

```
cd python-lib
test/unit/arg_parser/integration_test_run.sh
test/unit/gen_libs/integration_test_run.sh
```

Redhat 8 (Running Python 3.6):

```
cd python-lib
test/unit/arg_parser/integration_test_run3.sh
test/unit/gen_libs/integration_test_run3.sh
```

