#!/bin/bash
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Integration test:"
python test/integration/gen_class/argparser_init.py
python test/integration/gen_class/argparser_arg_dir_chk.py
python test/integration/gen_class/argparser_arg_dir_crt.py
python test/integration/gen_class/argparser_arg_file_chk.py
python test/integration/gen_class/argparser_arg_parse2.py
python test/integration/gen_class/argparser_parse_multi.py
python test/integration/gen_class/argparser_parse_single.py
