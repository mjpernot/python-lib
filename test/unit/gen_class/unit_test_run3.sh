#!/bin/bash
# Unit testing program for the gen_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: gen_class module"  
python3 test/unit/gen_class/get_inst.py
python3 test/unit/gen_class/setup_mail.py
python3 test/unit/gen_class/argparser_arg_add_def.py
python3 test/unit/gen_class/argparser_arg_cond_req.py
python3 test/unit/gen_class/argparser_arg_cond_req_or.py
python3 test/unit/gen_class/argparser_arg_default.py
python3 test/unit/gen_class/argparser_arg_dir_chk.py
python3 test/unit/gen_class/argparser_arg_dir_chk_crt.py
python3 test/unit/gen_class/argparser_arg_dir_crt.py
python3 test/unit/gen_class/argparser_arg_exist.py
python3 test/unit/gen_class/argparser_arg_file_chk.py
python3 test/unit/gen_class/argparser_arg_noreq_xor.py
python3 test/unit/gen_class/argparser_arg_parse2.py
python3 test/unit/gen_class/argparser_arg_require.py
python3 test/unit/gen_class/argparser_arg_req_or_lst.py
python3 test/unit/gen_class/argparser_arg_req_xor.py
python3 test/unit/gen_class/argparser_arg_set_path.py
python3 test/unit/gen_class/argparser_arg_validate.py
python3 test/unit/gen_class/argparser_arg_valid_val.py
python3 test/unit/gen_class/argparser_arg_wildcard.py
python3 test/unit/gen_class/argparser_arg_xor_dict.py
python3 test/unit/gen_class/argparser_delete_arg.py
python3 test/unit/gen_class/argparser_get_args.py
python3 test/unit/gen_class/argparser_get_args_keys.py
python3 test/unit/gen_class/argparser_get_val.py
python3 test/unit/gen_class/argparser_init.py
python3 test/unit/gen_class/argparser_insert_arg.py
python3 test/unit/gen_class/argparser_parse_multi.py
python3 test/unit/gen_class/argparser_parse_single.py
python3 test/unit/gen_class/argparser_update_arg.py
python3 test/unit/gen_class/daemon_delpid.py
python3 test/unit/gen_class/daemon_init.py
python3 test/unit/gen_class/daemon_restart.py
python3 test/unit/gen_class/daemon_start.py
python3 test/unit/gen_class/logfile_filter_ignore.py
python3 test/unit/gen_class/logfile_filter_keyword.py
python3 test/unit/gen_class/logfile_filter_regex.py
python3 test/unit/gen_class/logfile_find_marker.py
python3 test/unit/gen_class/logfile_get_marker.py
python3 test/unit/gen_class/logfile_init.py
python3 test/unit/gen_class/logfile_load_ignore.py
python3 test/unit/gen_class/logfile_load_keyword.py
python3 test/unit/gen_class/logfile_load_loglist.py
python3 test/unit/gen_class/logfile_load_marker.py
python3 test/unit/gen_class/logfile_load_regex.py
python3 test/unit/gen_class/logfile_set_marker.py
python3 test/unit/gen_class/logfile_set_predicate.py
python3 test/unit/gen_class/logger_init.py
python3 test/unit/gen_class/logger_log_close.py
python3 test/unit/gen_class/logger_log_crit.py
python3 test/unit/gen_class/logger_log_debug.py
python3 test/unit/gen_class/logger_log_err.py
python3 test/unit/gen_class/logger_log_info.py
python3 test/unit/gen_class/logger_log_warn.py
python3 test/unit/gen_class/progressbar_init.py
python3 test/unit/gen_class/progressbar_update.py
python3 test/unit/gen_class/progressbar_calc_and_update.py
python3 test/unit/gen_class/singleinstanceexception.py
python3 test/unit/gen_class/programlock_init.py
python3 test/unit/gen_class/programlock_del.py
python3 test/unit/gen_class/system_init.py
python3 test/unit/gen_class/system_set_host_name.py
python3 test/unit/gen_class/timeformat_add_format.py
python3 test/unit/gen_class/timeformat_create_adhoc_hack.py
python3 test/unit/gen_class/timeformat_create_hack.py
python3 test/unit/gen_class/timeformat_get_hack.py
python3 test/unit/gen_class/timeformat_init.py
# The package yum==3.4.3 only works with Python 2.7
# python3 test/unit/gen_class/yum_init.py
# python3 test/unit/gen_class/yum_get_hostname.py
# python3 test/unit/gen_class/yum_get_os.py
# python3 test/unit/gen_class/yum_get_distro.py
# python3 test/unit/gen_class/yum_get_release.py
# python3 test/unit/gen_class/yum_fetch_install_pkgs.py
# python3 test/unit/gen_class/yum_fetch_update_pkgs.py
python3 test/unit/gen_class/mail_init.py
python3 test/unit/gen_class/mail_add_2_msg.py
python3 test/unit/gen_class/mail_create_body.py
python3 test/unit/gen_class/mail_create_subject.py
python3 test/unit/gen_class/mail_print_email.py
python3 test/unit/gen_class/mail_read_stdin.py
python3 test/unit/gen_class/mail_send_mail.py
python3 test/unit/gen_class/mail_send_mailx.py

