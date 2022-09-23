#!/bin/bash
# Unit testing program for the cmds_gen.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test"
/usr/bin/python2 ./test/unit/cmds_gen/add_cmd.py
/usr/bin/python2 ./test/unit/cmds_gen/is_add_cmd.py

