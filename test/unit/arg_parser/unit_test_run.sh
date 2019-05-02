#!/bin/bash
# Unit testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:  arg_add_def"
test/unit/arg_parser/arg_add_def.py

echo ""
echo "Unit test:  arg_file_chk"
test/unit/arg_parser/arg_file_chk.py

echo ""
echo "Unit test:  arg_parse2"
test/unit/arg_parser/arg_parse2.py

echo ""
echo "Unit test:  parse_multi"
test/unit/arg_parser/parse_multi.py

echo ""
echo "Unit test:  parse_single"
test/unit/arg_parser/parse_single.py

echo ""
echo "Unit test:  file_create"
test/unit/arg_parser/file_create.py

