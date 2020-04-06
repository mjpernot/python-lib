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
test/unit/errors/NotMasterError.py
test/unit/errors/NotSlaveError.py
test/unit/errors/NotYetImplementedError.py
test/unit/errors/SlaveNotRunningError.py

