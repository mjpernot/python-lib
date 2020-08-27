#!/bin/bash
# Unit test code coverage for errors module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=errors test/unit/errors/emptyrowerror.py
coverage run -a --source=errors test/unit/errors/error.py
coverage run -a --source=errors test/unit/errors/nooptionerror.py
coverage run -a --source=errors test/unit/errors/notmastererror.py
coverage run -a --source=errors test/unit/errors/notslaveerror.py
coverage run -a --source=errors test/unit/errors/notyetimplementederror.py
coverage run -a --source=errors test/unit/errors/slavenotrunningerror.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
