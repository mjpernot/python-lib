#!/bin/bash
# Unit test code coverage for gen_class module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=gen_class test/unit/gen_class/get_inst.py
coverage run -a --source=gen_class test/unit/gen_class/setup_mail.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_add_def.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_cond_req.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_cond_req_or.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_default.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_dir_chk.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_dir_crt.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_exist.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_file_chk.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_noreq_xor.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_parse2.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_require.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_req_or_lst.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_req_xor.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_set_path.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_validate.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_valid_val.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_wildcard.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_arg_xor_dict.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_delete_arg.py
coverage run -a --source=gen_class test/unit/gen_class/timeformat_add_format.py
coverage run -a --source=gen_class test/unit/gen_class/timeformat_create_adhoc_hack.py
coverage run -a --source=gen_class test/unit/gen_class/timeformat_create_hack.py
coverage run -a --source=gen_class test/unit/gen_class/timeformat_get_hack.py
coverage run -a --source=gen_class test/unit/gen_class/timeformat_init.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_get_args.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_get_args_keys.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_get_val.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_init.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_insert_arg.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_parse_multi.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_parse_single.py
coverage run -a --source=gen_class test/unit/gen_class/argparser_update_arg.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_daemonize.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_delpid.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_init.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_restart.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_start.py
coverage run -a --source=gen_class test/unit/gen_class/daemon_stop.py
coverage run -a --source=gen_class test/unit/gen_class/daemon2_init.py
coverage run -a --source=gen_class test/unit/gen_class/daemon2_daemonize.py
coverage run -a --source=gen_class test/unit/gen_class/daemon2_del_pid.py
coverage run -a --source=gen_class test/unit/gen_class/daemon2_restart.py
coverage run -a --source=gen_class test/unit/gen_class/daemon2_start.py
coverage run -a --source=gen_class test/unit/gen_class/daemon2_stop.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_init.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_capture_pkgs.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_capture_repos.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_fetch_install_pkgs.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_fetch_repos.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_distro.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_all_repos.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_enabled_repos.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_hostname.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_install_pkgs.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_installed.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_os.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_release.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_update_pkgs.py
coverage run -a --source=gen_class test/unit/gen_class/dnf_get_updates.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_init.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_contains.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_delitem.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_get.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_getitem.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_has_key.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_keylower.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_pop.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_setdefault.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_setitem.py
coverage run -a --source=gen_class test/unit/gen_class/keycaseinsensitivedict_update.py
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
coverage run -a --source=gen_class test/unit/gen_class/mail2_init.py
coverage run -a --source=gen_class test/unit/gen_class/mail2_add_attachment.py
coverage run -a --source=gen_class test/unit/gen_class/mail2_add_text.py
coverage run -a --source=gen_class test/unit/gen_class/mail2_send_mail.py
coverage run -a --source=gen_class test/unit/gen_class/programlock_del.py
coverage run -a --source=gen_class test/unit/gen_class/programlock_init.py
coverage run -a --source=gen_class test/unit/gen_class/progressbar_calc_and_update.py
coverage run -a --source=gen_class test/unit/gen_class/progressbar_init.py
coverage run -a --source=gen_class test/unit/gen_class/progressbar_update.py
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

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
