#!/bin/bash
# Unit testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:  arg_file_chk"
test/unit/arg_parser/arg_file_chk.py

echo ""
echo "Unit test:  arg_parse2"
test/unit/arg_parser/arg_parse2.py

