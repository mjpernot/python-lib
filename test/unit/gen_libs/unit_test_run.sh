#!/bin/bash
# Unit testing program for the gen_libs.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:  chk_crt_dir"
test/unit/gen_libs/chk_crt_dir.py

echo ""
echo "Unit test:  chk_crt_file"
test/unit/gen_libs/chk_crt_file.py

echo ""
echo "Unit test:  clear_file"
test/unit/gen_libs/clear_file.py

echo ""
echo "Unit test:  cp_file"
test/unit/gen_libs/cp_file.py

echo ""
echo "Unit test:  data_multi_out"
test/unit/gen_libs/data_multi_out.py

echo ""
echo "Unit test:  display_data"
test/unit/gen_libs/display_data.py

echo ""
echo "Unit test:  file_2_list"
test/unit/gen_libs/file_2_list.py

echo ""
echo "Unit test:  file_search_cnt"
test/unit/gen_libs/file_search_cnt.py

echo ""
echo "Unit test:  file_search"
test/unit/gen_libs/file_search.py

echo ""
echo "Unit test:  get_base_dir"
test/unit/gen_libs/get_base_dir.py

echo ""
echo "Unit test:  get_data"
test/unit/gen_libs/get_data.py

echo ""
echo "Unit test:  is_empty_file"
test/unit/gen_libs/is_empty_file.py

echo ""
echo "Unit test:  list_dirs"
test/unit/gen_libs/list_dirs.py

echo ""
echo "Unit test:  merge_data_types"
test/unit/gen_libs/merge_data_types.py

echo ""
echo "Unit test:  merge_two_dicts"
test/unit/gen_libs/merge_two_dicts.py

echo ""
echo "Unit test:  month_delta"
test/unit/gen_libs/month_delta.py

echo ""
echo "Unit test:  no_std_out"
test/unit/gen_libs/no_std_out.py

echo ""
echo "Unit test:  touch"
test/unit/gen_libs/touch.py

echo ""
echo "Unit test:  write_file"
test/unit/gen_libs/write_file.py

