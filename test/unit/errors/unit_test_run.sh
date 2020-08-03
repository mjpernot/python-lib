#!/bin/bash
# Unit testing program for the errors.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test"
test/unit/errors/EmptyRowError.py
test/unit/errors/Error.py
test/unit/errors/NoOptionError.py
test/unit/errors/notmastererror.py
test/unit/errors/notslaveerror.py
test/unit/errors/notyetimplementederror.py
test/unit/errors/slavenotrunningerror.py

