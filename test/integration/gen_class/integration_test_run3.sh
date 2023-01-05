#!/bin/bash
# Integration testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Integration test:"
python3 test/integration/gen_class/argparser_init.py
python3 test/integration/gen_class/argparser_arg_dir_chk.py
python3 test/integration/gen_class/argparser_arg_dir_chk_crt.py
python3 test/integration/gen_class/argparser_arg_dir_crt.py
python3 test/integration/gen_class/argparser_arg_file_chk.py
python3 test/integration/gen_class/argparser_arg_parse2.py
python3 test/integration/gen_class/argparser_parse_multi.py
python3 test/integration/gen_class/argparser_parse_single.py
