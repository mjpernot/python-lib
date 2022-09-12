#!/bin/bash
# Unit testing program for the errors.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test"
python test/unit/errors/emptyrowerror.py
python test/unit/errors/error.py
python test/unit/errors/nooptionerror.py
python test/unit/errors/notmastererror.py
python test/unit/errors/notslaveerror.py
python test/unit/errors/notyetimplementederror.py
python test/unit/errors/slavenotrunningerror.py

