#!/bin/bash
# Unit test code coverage for gen_class module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=gen_class test/unit/gen_class/ProgramLock_del.py
coverage run -a --source=gen_class test/unit/gen_class/ProgramLock_init.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_calc_and_update.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_init.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_update.py
coverage run -a --source=gen_class test/unit/gen_class/SingleInstanceException.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_distro.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_os.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_release.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_init.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
