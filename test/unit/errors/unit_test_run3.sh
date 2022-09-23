#!/bin/bash
# Unit testing program for the errors.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test"
/usr/bin/python3 ./test/unit/errors/emptyrowerror.py
/usr/bin/python3 ./test/unit/errors/error.py
/usr/bin/python3 ./test/unit/errors/nooptionerror.py
/usr/bin/python3 ./test/unit/errors/notmastererror.py
/usr/bin/python3 ./test/unit/errors/notslaveerror.py
/usr/bin/python3 ./test/unit/errors/notyetimplementederror.py
/usr/bin/python3 ./test/unit/errors/slavenotrunningerror.py

