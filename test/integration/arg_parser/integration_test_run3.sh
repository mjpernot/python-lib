#!/bin/bash
# Integration testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
python3 test/integration/arg_parser/arg_dir_chk.py
python3 test/integration/arg_parser/arg_dir_chk_crt.py
python3 test/integration/arg_parser/arg_file_chk.py
python3 test/integration/arg_parser/arg_parse2.py
python3 test/integration/arg_parser/_file_create.py
python3 test/integration/arg_parser/_parse_multi.py
python3 test/integration/arg_parser/_parse_single.py

