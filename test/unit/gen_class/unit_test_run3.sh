#!/bin/bash
# Unit testing program for the gen_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: gen_class module"  
/usr/bin/python3 ./test/unit/gen_class/get_inst.py
/usr/bin/python3 ./test/unit/gen_class/setup_mail.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_add_def.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_cond_req.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_cond_req_or.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_default.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_dir_chk.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_dir_chk_crt.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_dir_crt.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_exist.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_file_chk.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_noreq_xor.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_parse2.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_require.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_req_or_lst.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_req_xor.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_set_path.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_validate.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_valid_val.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_wildcard.py
/usr/bin/python3 ./test/unit/gen_class/argparser_arg_xor_dict.py
/usr/bin/python3 ./test/unit/gen_class/argparser_delete_arg.py
/usr/bin/python3 ./test/unit/gen_class/argparser_get_args.py
/usr/bin/python3 ./test/unit/gen_class/argparser_get_args_keys.py
/usr/bin/python3 ./test/unit/gen_class/argparser_get_val.py
/usr/bin/python3 ./test/unit/gen_class/argparser_init.py
/usr/bin/python3 ./test/unit/gen_class/argparser_insert_arg.py
/usr/bin/python3 ./test/unit/gen_class/argparser_parse_multi.py
/usr/bin/python3 ./test/unit/gen_class/argparser_parse_single.py
/usr/bin/python3 ./test/unit/gen_class/argparser_update_arg.py
/usr/bin/python3 ./test/unit/gen_class/daemon_daemonize.py
/usr/bin/python3 ./test/unit/gen_class/daemon_delpid.py
/usr/bin/python3 ./test/unit/gen_class/daemon_init.py
/usr/bin/python3 ./test/unit/gen_class/daemon_restart.py
/usr/bin/python3 ./test/unit/gen_class/daemon_start.py
/usr/bin/python3 ./test/unit/gen_class/daemon_stop.py
/usr/bin/python3 ./test/unit/gen_class/daemon2_init.py
/usr/bin/python3 ./test/unit/gen_class/daemon2_daemonize.py
/usr/bin/python3 ./test/unit/gen_class/daemon2_del_pid.py
/usr/bin/python3 ./test/unit/gen_class/daemon2_restart.py
/usr/bin/python3 ./test/unit/gen_class/daemon2_start.py
/usr/bin/python3 ./test/unit/gen_class/daemon2_stop.py
/usr/bin/python3 ./test/unit/gen_class/dnf_init.py
/usr/bin/python3 ./test/unit/gen_class/dnf_capture_pkgs.py
/usr/bin/python3 ./test/unit/gen_class/dnf_capture_repos.py
/usr/bin/python3 ./test/unit/gen_class/dnf_get_all_repos.py
/usr/bin/python3 ./test/unit/gen_class/dnf_get_enabled_repos.py
/usr/bin/python3 ./test/unit/gen_class/dnf_get_installed.py
/usr/bin/python3 ./test/unit/gen_class/logfile_filter_ignore.py
/usr/bin/python3 ./test/unit/gen_class/logfile_filter_keyword.py
/usr/bin/python3 ./test/unit/gen_class/logfile_filter_regex.py
/usr/bin/python3 ./test/unit/gen_class/logfile_find_marker.py
/usr/bin/python3 ./test/unit/gen_class/logfile_get_marker.py
/usr/bin/python3 ./test/unit/gen_class/logfile_init.py
/usr/bin/python3 ./test/unit/gen_class/logfile_load_ignore.py
/usr/bin/python3 ./test/unit/gen_class/logfile_load_keyword.py
/usr/bin/python3 ./test/unit/gen_class/logfile_load_loglist.py
/usr/bin/python3 ./test/unit/gen_class/logfile_load_marker.py
/usr/bin/python3 ./test/unit/gen_class/logfile_load_regex.py
/usr/bin/python3 ./test/unit/gen_class/logfile_set_marker.py
/usr/bin/python3 ./test/unit/gen_class/logfile_set_predicate.py
/usr/bin/python3 ./test/unit/gen_class/logger_init.py
/usr/bin/python3 ./test/unit/gen_class/logger_log_close.py
/usr/bin/python3 ./test/unit/gen_class/logger_log_crit.py
/usr/bin/python3 ./test/unit/gen_class/logger_log_debug.py
/usr/bin/python3 ./test/unit/gen_class/logger_log_err.py
/usr/bin/python3 ./test/unit/gen_class/logger_log_info.py
/usr/bin/python3 ./test/unit/gen_class/logger_log_warn.py
/usr/bin/python3 ./test/unit/gen_class/mail2_init.py
/usr/bin/python3 ./test/unit/gen_class/mail2_add_attachment.py
/usr/bin/python3 ./test/unit/gen_class/mail2_add_text.py
/usr/bin/python3 ./test/unit/gen_class/mail2_send_mail.py
/usr/bin/python3 ./test/unit/gen_class/progressbar_init.py
/usr/bin/python3 ./test/unit/gen_class/progressbar_update.py
/usr/bin/python3 ./test/unit/gen_class/progressbar_calc_and_update.py
/usr/bin/python3 ./test/unit/gen_class/singleinstanceexception.py
/usr/bin/python3 ./test/unit/gen_class/programlock_init.py
/usr/bin/python3 ./test/unit/gen_class/programlock_del.py
/usr/bin/python3 ./test/unit/gen_class/system_init.py
/usr/bin/python3 ./test/unit/gen_class/system_set_host_name.py
/usr/bin/python3 ./test/unit/gen_class/timeformat_add_format.py
/usr/bin/python3 ./test/unit/gen_class/timeformat_create_adhoc_hack.py
/usr/bin/python3 ./test/unit/gen_class/timeformat_create_hack.py
/usr/bin/python3 ./test/unit/gen_class/timeformat_get_hack.py
/usr/bin/python3 ./test/unit/gen_class/timeformat_init.py
# The package yum==3.4.3 only works with Python 2.7
# /usr/bin/python3 ./test/unit/gen_class/yum_init.py
# /usr/bin/python3 ./test/unit/gen_class/yum_get_hostname.py
# /usr/bin/python3 ./test/unit/gen_class/yum_get_os.py
# /usr/bin/python3 ./test/unit/gen_class/yum_get_distro.py
# /usr/bin/python3 ./test/unit/gen_class/yum_get_release.py
# /usr/bin/python3 ./test/unit/gen_class/yum_fetch_install_pkgs.py
# /usr/bin/python3 ./test/unit/gen_class/yum_fetch_update_pkgs.py
/usr/bin/python3 ./test/unit/gen_class/mail_init.py
/usr/bin/python3 ./test/unit/gen_class/mail_add_2_msg.py
/usr/bin/python3 ./test/unit/gen_class/mail_create_body.py
/usr/bin/python3 ./test/unit/gen_class/mail_create_subject.py
/usr/bin/python3 ./test/unit/gen_class/mail_print_email.py
/usr/bin/python3 ./test/unit/gen_class/mail_read_stdin.py
/usr/bin/python3 ./test/unit/gen_class/mail_send_mail.py
/usr/bin/python3 ./test/unit/gen_class/mail_send_mailx.py

