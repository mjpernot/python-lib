#!/bin/bash
# Integration testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
test/integration/arg_parser/arg_dir_chk_crt.py
test/integration/arg_parser/arg_file_chk.py
test/integration/arg_parser/arg_parse2.py
test/integration/arg_parser/_file_create.py
test/integration/arg_parser/_parse_multi.py
test/integration/arg_parser/_parse_single.py

