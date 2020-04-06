#!/bin/bash
# Unit test code coverage for cmds_gen module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=cmds_gen test/unit/cmds_gen/add_cmd.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/create_cfg_array.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/disconnect.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/get_inst.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/is_add_cmd.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/run_prog.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
