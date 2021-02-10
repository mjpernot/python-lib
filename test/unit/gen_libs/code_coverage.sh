#!/bin/bash
# Unit test code coverage for gen_libs module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=gen_libs test/unit/gen_libs/and_is_true.py
coverage run -a --source=gen_libs test/unit/gen_libs/bytes_2_readable.py
coverage run -a --source=gen_libs test/unit/gen_libs/chk_crt_dir.py
coverage run -a --source=gen_libs test/unit/gen_libs/chk_crt_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/chk_int.py
coverage run -a --source=gen_libs test/unit/gen_libs/clear_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/compress.py
coverage run -a --source=gen_libs test/unit/gen_libs/cp_dir.py
coverage run -a --source=gen_libs test/unit/gen_libs/cp_file2.py
coverage run -a --source=gen_libs test/unit/gen_libs/cp_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/crt_file_time.py
coverage run -a --source=gen_libs test/unit/gen_libs/date_range.py
coverage run -a --source=gen_libs test/unit/gen_libs/del_not_and_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/del_not_in_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/dict_2_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/dict_2_std.py
coverage run -a --source=gen_libs test/unit/gen_libs/dir_file_match.py
coverage run -a --source=gen_libs test/unit/gen_libs/disk_usage.py
coverage run -a --source=gen_libs test/unit/gen_libs/display_data.py
coverage run -a --source=gen_libs test/unit/gen_libs/file_2_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/file_cleanup.py
coverage run -a --source=gen_libs test/unit/gen_libs/file_search_cnt.py
coverage run -a --source=gen_libs test/unit/gen_libs/file_search.py
coverage run -a --source=gen_libs test/unit/gen_libs/filename_search.py
coverage run -a --source=gen_libs test/unit/gen_libs/float_div.py
coverage run -a --source=gen_libs test/unit/gen_libs/get_base_dir.py
coverage run -a --source=gen_libs test/unit/gen_libs/get_data.py
coverage run -a --source=gen_libs test/unit/gen_libs/get_date.py
coverage run -a --source=gen_libs test/unit/gen_libs/get_inst.py
coverage run -a --source=gen_libs test/unit/gen_libs/get_secs.py
coverage run -a --source=gen_libs test/unit/gen_libs/get_time.py
coverage run -a --source=gen_libs test/unit/gen_libs/has_whitespace.py
coverage run -a --source=gen_libs test/unit/gen_libs/help_func.py
coverage run -a --source=gen_libs test/unit/gen_libs/in_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/is_empty_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/is_file_text.py
coverage run -a --source=gen_libs test/unit/gen_libs/is_missing_lists.py
coverage run -a --source=gen_libs test/unit/gen_libs/is_pos_int.py
coverage run -a --source=gen_libs test/unit/gen_libs/is_true.py
coverage run -a --source=gen_libs test/unit/gen_libs/key_cleaner.py
coverage run -a --source=gen_libs test/unit/gen_libs/list_2_dict.py
coverage run -a --source=gen_libs test/unit/gen_libs/list_2_str.py
coverage run -a --source=gen_libs test/unit/gen_libs/list_dirs.py
coverage run -a --source=gen_libs test/unit/gen_libs/list_files.py
coverage run -a --source=gen_libs test/unit/gen_libs/list_filter_files.py
coverage run -a --source=gen_libs test/unit/gen_libs/load_module.py
coverage run -a --source=gen_libs test/unit/gen_libs/make_md5_hash.py
coverage run -a --source=gen_libs test/unit/gen_libs/make_zip.py
coverage run -a --source=gen_libs test/unit/gen_libs/merge_data_types.py
coverage run -a --source=gen_libs test/unit/gen_libs/merge_two_dicts.py
coverage run -a --source=gen_libs test/unit/gen_libs/milli_2_readadble.py
coverage run -a --source=gen_libs test/unit/gen_libs/month_days.py
coverage run -a --source=gen_libs test/unit/gen_libs/month_delta.py
coverage run -a --source=gen_libs test/unit/gen_libs/mv_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/mv_file2.py
coverage run -a --source=gen_libs test/unit/gen_libs/normalize.py
coverage run -a --source=gen_libs test/unit/gen_libs/not_in_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/no_std_out.py
coverage run -a --source=gen_libs test/unit/gen_libs/openfile.py
coverage run -a --source=gen_libs test/unit/gen_libs/pct_int.py
coverage run -a --source=gen_libs test/unit/gen_libs/perm_check.py
coverage run -a --source=gen_libs test/unit/gen_libs/print_data.py
coverage run -a --source=gen_libs test/unit/gen_libs/print_dict.py
coverage run -a --source=gen_libs test/unit/gen_libs/print_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/prt_dict.py
coverage run -a --source=gen_libs test/unit/gen_libs/prt_lvl.py
coverage run -a --source=gen_libs test/unit/gen_libs/prt_msg.py
coverage run -a --source=gen_libs test/unit/gen_libs/rename_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/rm_dup_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/rm_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/rm_key.py
coverage run -a --source=gen_libs test/unit/gen_libs/rm_newline_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/rm_whitespace.py
coverage run -a --source=gen_libs test/unit/gen_libs/root_run.py
coverage run -a --source=gen_libs test/unit/gen_libs/rotate_files.py
coverage run -a --source=gen_libs test/unit/gen_libs/sec_2_hr.py
coverage run -a --source=gen_libs test/unit/gen_libs/str_2_list.py
coverage run -a --source=gen_libs test/unit/gen_libs/str_2_type.py
coverage run -a --source=gen_libs test/unit/gen_libs/touch.py
coverage run -a --source=gen_libs test/unit/gen_libs/validate_date.py
coverage run -a --source=gen_libs test/unit/gen_libs/validate_int.py
coverage run -a --source=gen_libs test/unit/gen_libs/write_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/write_file2.py
coverage run -a --source=gen_libs test/unit/gen_libs/write_to_log.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
