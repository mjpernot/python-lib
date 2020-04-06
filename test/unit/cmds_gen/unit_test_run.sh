#!/bin/bash
# Unit testing program for the cmds_gen.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test"
test/unit/cmds_gen/add_cmd.py
test/unit/cmds_gen/create_cfg_array.py
test/unit/cmds_gen/disconnect.py
test/unit/cmds_gen/get_inst.py
test/unit/cmds_gen/is_add_cmd.py
test/unit/cmds_gen/run_prog.py

