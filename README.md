# Python project that contains common libraries and classes for python programs.
# Classification (U)

# Description:
  Local python functions and classes that are available for general python use.


### This README file is broken down into the following sections:
 *  Installation
    - Pip Installation
 *  Testing
    - Unit
    - Integration


# Installation

### Pip Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python lib project and any reference to **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install python-lib as a library module.

Create requirements-python-lib.txt file.  This will require access to a clone of the python-lib project.

```
cp {Python_Project}/python-lib/requirements-python-lib.txt {Other_Python_Project}/requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file:

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general python-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

```
simplejson==2.0.9
```


# Testing

# Unit Testing:

### Installation:

Install the project using git.

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

### Testing:

```
cd {Python_Project}/python-lib
test/unit/gen_libs/unit_test_run.sh
test/unit/arg_parser/unit_test_run.sh
test/unit/gen_class/unit_test_run.sh
test/unit/cmds_gen/unit_test_run.sh
test/unit/errors/unit_test_run.sh
test/unit/machine/unit_test_run.sh
```

### Code Coverage:

```
cd {Python_Project}/python-lib
test/unit/gen_libs/code_coverage.sh
test/unit/arg_parser/code_coverage.sh
test/unit/gen_class/code_coverage.sh
test/unit/cmds_gen/code_coverage.sh
test/unit/errors/code_coverage.sh
test/unit/machine/code_coverage.sh
```

# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section under Unit Testing.

### Testing:
```
cd {Python_Project}/python-lib
test/unit/arg_parser/integration_test_run.sh
test/unit/gen_libs/integration_test_run.sh
```

