#!/bin/bash
# Unit testing program for the gen_libs.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:  gen_libs.py"
/usr/bin/python2 ./test/unit/gen_libs/add_cmd.py
/usr/bin/python2 ./test/unit/gen_libs/and_is_true.py
/usr/bin/python2 ./test/unit/gen_libs/bytes_2_readable.py
/usr/bin/python2 ./test/unit/gen_libs/chk_crt_dir.py
/usr/bin/python2 ./test/unit/gen_libs/chk_crt_file.py
/usr/bin/python2 ./test/unit/gen_libs/chk_int.py
/usr/bin/python2 ./test/unit/gen_libs/chk_perm.py
/usr/bin/python2 ./test/unit/gen_libs/clear_file.py
/usr/bin/python2 ./test/unit/gen_libs/compress.py
/usr/bin/python2 ./test/unit/gen_libs/cp_dir.py
/usr/bin/python2 ./test/unit/gen_libs/cp_file2.py
/usr/bin/python2 ./test/unit/gen_libs/cp_file.py
/usr/bin/python2 ./test/unit/gen_libs/create_cfg_array.py
/usr/bin/python2 ./test/unit/gen_libs/crt_file_time.py
/usr/bin/python2 ./test/unit/gen_libs/date_range.py
/usr/bin/python2 ./test/unit/gen_libs/del_not_and_list.py
/usr/bin/python2 ./test/unit/gen_libs/del_not_in_list.py
/usr/bin/python2 ./test/unit/gen_libs/dict_2_list.py
/usr/bin/python2 ./test/unit/gen_libs/dict_2_std.py
/usr/bin/python2 ./test/unit/gen_libs/dict_out.py
/usr/bin/python2 ./test/unit/gen_libs/dir_file_match.py
/usr/bin/python2 ./test/unit/gen_libs/disk_usage.py
/usr/bin/python2 ./test/unit/gen_libs/display_data.py
/usr/bin/python2 ./test/unit/gen_libs/file_2_list.py
/usr/bin/python2 ./test/unit/gen_libs/file_cleanup.py
/usr/bin/python2 ./test/unit/gen_libs/file_search_cnt.py
/usr/bin/python2 ./test/unit/gen_libs/file_search.py
/usr/bin/python2 ./test/unit/gen_libs/filename_search.py
/usr/bin/python2 ./test/unit/gen_libs/find_email_addr.py
/usr/bin/python2 ./test/unit/gen_libs/float_div.py
/usr/bin/python2 ./test/unit/gen_libs/get_base_dir.py
/usr/bin/python2 ./test/unit/gen_libs/get_data.py
/usr/bin/python2 ./test/unit/gen_libs/get_date.py
/usr/bin/python2 ./test/unit/gen_libs/get_secs.py
/usr/bin/python2 ./test/unit/gen_libs/get_time.py
/usr/bin/python2 ./test/unit/gen_libs/has_whitespace.py
/usr/bin/python2 ./test/unit/gen_libs/help_func.py
/usr/bin/python2 ./test/unit/gen_libs/in_list.py
/usr/bin/python2 ./test/unit/gen_libs/is_add_cmd.py
/usr/bin/python2 ./test/unit/gen_libs/is_base64.py
/usr/bin/python2 ./test/unit/gen_libs/is_empty_file.py
/usr/bin/python2 ./test/unit/gen_libs/is_file_text.py
/usr/bin/python2 ./test/unit/gen_libs/is_missing_lists.py
/usr/bin/python2 ./test/unit/gen_libs/is_pos_int.py
/usr/bin/python2 ./test/unit/gen_libs/is_true.py
/usr/bin/python2 ./test/unit/gen_libs/key_cleaner.py
/usr/bin/python2 ./test/unit/gen_libs/list_2_dict.py
/usr/bin/python2 ./test/unit/gen_libs/list_2_str.py
/usr/bin/python2 ./test/unit/gen_libs/list_dirs.py
/usr/bin/python2 ./test/unit/gen_libs/list_files.py
/usr/bin/python2 ./test/unit/gen_libs/list_filter_files.py
/usr/bin/python2 ./test/unit/gen_libs/load_module.py
/usr/bin/python2 ./test/unit/gen_libs/make_dir.py
/usr/bin/python2 ./test/unit/gen_libs/make_md5_hash.py
/usr/bin/python2 ./test/unit/gen_libs/make_zip.py
/usr/bin/python2 ./test/unit/gen_libs/merge_data_types.py
/usr/bin/python2 ./test/unit/gen_libs/merge_two_dicts.py
/usr/bin/python2 ./test/unit/gen_libs/milli_2_readadble.py
/usr/bin/python2 ./test/unit/gen_libs/month_days.py
/usr/bin/python2 ./test/unit/gen_libs/month_delta.py
/usr/bin/python2 ./test/unit/gen_libs/mv_file.py
/usr/bin/python2 ./test/unit/gen_libs/mv_file2.py
/usr/bin/python2 ./test/unit/gen_libs/normalize.py
/usr/bin/python2 ./test/unit/gen_libs/not_in_list.py
/usr/bin/python2 ./test/unit/gen_libs/no_std_out.py
/usr/bin/python2 ./test/unit/gen_libs/octal_to_str.py
/usr/bin/python2 ./test/unit/gen_libs/openfile.py
/usr/bin/python2 ./test/unit/gen_libs/pascalize.py
/usr/bin/python2 ./test/unit/gen_libs/pct_int.py
/usr/bin/python2 ./test/unit/gen_libs/perm_check.py
/usr/bin/python2 ./test/unit/gen_libs/print_data.py
/usr/bin/python2 ./test/unit/gen_libs/print_dict.py
/usr/bin/python2 ./test/unit/gen_libs/print_list.py
/usr/bin/python2 ./test/unit/gen_libs/prt_dict.py
/usr/bin/python2 ./test/unit/gen_libs/prt_lvl.py
/usr/bin/python2 ./test/unit/gen_libs/prt_msg.py
/usr/bin/python2 ./test/unit/gen_libs/rename_file.py
/usr/bin/python2 ./test/unit/gen_libs/rm_dup_list.py
/usr/bin/python2 ./test/unit/gen_libs/rm_file.py
/usr/bin/python2 ./test/unit/gen_libs/rm_key.py
/usr/bin/python2 ./test/unit/gen_libs/rm_newline_list.py
/usr/bin/python2 ./test/unit/gen_libs/rm_whitespace.py
/usr/bin/python2 ./test/unit/gen_libs/root_run.py
/usr/bin/python2 ./test/unit/gen_libs/rotate_files.py
/usr/bin/python2 ./test/unit/gen_libs/sec_2_hr.py
/usr/bin/python2 ./test/unit/gen_libs/str_type.py
/usr/bin/python2 ./test/unit/gen_libs/str_2_list.py
/usr/bin/python2 ./test/unit/gen_libs/str_2_type.py
/usr/bin/python2 ./test/unit/gen_libs/touch.py
/usr/bin/python2 ./test/unit/gen_libs/transpose_dict.py
/usr/bin/python2 ./test/unit/gen_libs/validate_date.py
/usr/bin/python2 ./test/unit/gen_libs/validate_int.py
/usr/bin/python2 ./test/unit/gen_libs/write_file.py
/usr/bin/python2 ./test/unit/gen_libs/write_file2.py
/usr/bin/python2 ./test/unit/gen_libs/write_to_log.py

