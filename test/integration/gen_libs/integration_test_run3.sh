#!/bin/bash
# Integration testing program for the gen_libs.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:  gen_libs.py"
python3 test/integration/gen_libs/chk_crt_dir.py
python3 test/integration/gen_libs/chk_crt_file.py
python3 test/integration/gen_libs/chk_perm.py
python3 test/integration/gen_libs/dict_2_std.py
python3 test/integration/gen_libs/dir_file_match.py
python3 test/integration/gen_libs/display_data.py
python3 test/integration/gen_libs/filename_search.py
python3 test/integration/gen_libs/make_dir.py
python3 test/integration/gen_libs/make_md5_hash.py
python3 test/integration/gen_libs/merge_data_types.py
python3 test/integration/gen_libs/print_dict.py
python3 test/integration/gen_libs/prt_dict.py

