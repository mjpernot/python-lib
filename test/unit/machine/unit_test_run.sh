#!/bin/bash
# Unit testing program for the errors.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test"
/usr/bin/python ./test/unit/machine/linux.py
/usr/bin/python ./test/unit/machine/amachine.py

