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

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
