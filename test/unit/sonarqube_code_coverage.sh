#!/bin/bash
# Unit test code coverage for SonarQube to cover all library modules in python-lib.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=arg_parser test/unit/arg_parser/_make_dir.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_add_def.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_cond_req.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_cond_req_or.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_default.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_dir_chk_crt.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_file_chk.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_noreq_xor.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_parse2.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_require.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_req_or_lst.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_req_xor.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_set_path.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_validate.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_valid_val.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_wildcard.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_xor_dict.py
coverage run -a --source=arg_parser test/unit/arg_parser/parse_multi.py
coverage run -a --source=arg_parser test/unit/arg_parser/parse_single.py
coverage run -a --source=arg_parser test/unit/arg_parser/file_create.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/add_cmd.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/create_cfg_array.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/disconnect.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/get_inst.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/is_add_cmd.py
coverage run -a --source=cmds_gen test/unit/cmds_gen/run_prog.py
coverage run -a --source=errors test/unit/errors/emptyrowerror.py
coverage run -a --source=errors test/unit/errors/error.py
coverage run -a --source=errors test/unit/errors/nooptionerror.py
coverage run -a --source=errors test/unit/errors/notmastererror.py
coverage run -a --source=errors test/unit/errors/notslaveerror.py
coverage run -a --source=errors test/unit/errors/notyetimplementederror.py
coverage run -a --source=errors test/unit/errors/slavenotrunningerror.py
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
coverage run -a --source=gen_libs test/unit/gen_libs/write_file2.py
coverage run -a --source=gen_libs test/unit/gen_libs/write_file.py
coverage run -a --source=gen_libs test/unit/gen_libs/write_to_log.py
coverage run -a --source=gen_class test/unit/gen_class/get_inst.py
coverage run -a --source=gen_class test/unit/gen_class/setup_mail.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_delpid.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_init.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_restart.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_start.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_filter_ignore.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_filter_keyword.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_filter_regex.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_find_marker.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_get_marker.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_init.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_load_ignore.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_load_keyword.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_load_loglist.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_load_marker.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_load_regex.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_set_marker.py
coverage run -a --source=gen_class test/unit/gen_class/logfile_set_predicate.py
coverage run -a --source=gen_class test/unit/gen_class/logger_init.py
coverage run -a --source=gen_class test/unit/gen_class/logger_log_close.py
coverage run -a --source=gen_class test/unit/gen_class/logger_log_crit.py
coverage run -a --source=gen_class test/unit/gen_class/logger_log_debug.py
coverage run -a --source=gen_class test/unit/gen_class/logger_log_err.py
coverage run -a --source=gen_class test/unit/gen_class/logger_log_info.py
coverage run -a --source=gen_class test/unit/gen_class/logger_log_warn.py
coverage run -a --source=gen_class test/unit/gen_class/programlock_del.py
coverage run -a --source=gen_class test/unit/gen_class/programlock_init.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_calc_and_update.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_init.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_update.py
coverage run -a --source=gen_class test/unit/gen_class/singleinstanceexception.py
coverage run -a --source=gen_class test/unit/gen_class/system_init.py
coverage run -a --source=gen_class test/unit/gen_class/system_set_host_name.py
coverage run -a --source=gen_class test/unit/gen_class/yum_fetch_update_pkgs.py
coverage run -a --source=gen_class test/unit/gen_class/yum_fetch_install_pkgs.py
coverage run -a --source=gen_class test/unit/gen_class/yum_get_distro.py
coverage run -a --source=gen_class test/unit/gen_class/yum_get_hostname.py
coverage run -a --source=gen_class test/unit/gen_class/yum_get_os.py
coverage run -a --source=gen_class test/unit/gen_class/yum_get_release.py
coverage run -a --source=gen_class test/unit/gen_class/yum_init.py
coverage run -a --source=gen_class test/unit/gen_class/mail_init.py
coverage run -a --source=gen_class test/unit/gen_class/mail_add_2_msg.py
coverage run -a --source=gen_class test/unit/gen_class/mail_create_body.py
coverage run -a --source=gen_class test/unit/gen_class/mail_create_subject.py
coverage run -a --source=gen_class test/unit/gen_class/mail_print_email.py
coverage run -a --source=gen_class test/unit/gen_class/mail_read_stdin.py
coverage run -a --source=gen_class test/unit/gen_class/mail_send_mail.py
coverage run -a --source=gen_class test/unit/gen_class/mail_send_mailx.py
coverage run -a --source=machine test/unit/machine/linux.py
coverage run -a --source=machine test/unit/machine/amachine.py
coverage run -a --source=machine test/unit/machine/solaris.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

