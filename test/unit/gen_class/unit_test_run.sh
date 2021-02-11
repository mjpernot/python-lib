#!/bin/bash
# Unit testing program for the gen_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: gen_class module"  
test/unit/gen_class/get_inst.py
test/unit/gen_class/setup_mail.py
test/unit/gen_class/daemon_delpid.py
test/unit/gen_class/daemon_init.py
test/unit/gen_class/daemon_restart.py
test/unit/gen_class/daemon_start.py
test/unit/gen_class/logfile_filter_ignore.py
test/unit/gen_class/logfile_filter_keyword.py
test/unit/gen_class/logfile_filter_regex.py
test/unit/gen_class/logfile_find_marker.py
test/unit/gen_class/logfile_get_marker.py
test/unit/gen_class/logfile_init.py
test/unit/gen_class/logfile_load_ignore.py
test/unit/gen_class/logfile_load_keyword.py
test/unit/gen_class/logfile_load_loglist.py
test/unit/gen_class/logfile_load_marker.py
test/unit/gen_class/logfile_load_regex.py
test/unit/gen_class/logfile_set_marker.py
test/unit/gen_class/logfile_set_predicate.py
test/unit/gen_class/logger_init.py
test/unit/gen_class/logger_log_close.py
test/unit/gen_class/logger_log_crit.py
test/unit/gen_class/logger_log_debug.py
test/unit/gen_class/logger_log_err.py
test/unit/gen_class/logger_log_info.py
test/unit/gen_class/logger_log_warn.py
test/unit/gen_class/progressbar_init.py
test/unit/gen_class/progressbar_update.py
test/unit/gen_class/progressbar_calc_and_update.py
test/unit/gen_class/singleinstanceexception.py
test/unit/gen_class/programlock_init.py
test/unit/gen_class/programlock_del.py
test/unit/gen_class/system_init.py
test/unit/gen_class/system_set_host_name.py
test/unit/gen_class/yum_init.py
test/unit/gen_class/yum_get_hostname.py
test/unit/gen_class/yum_get_os.py
test/unit/gen_class/yum_get_distro.py
test/unit/gen_class/yum_get_release.py
test/unit/gen_class/yum_fetch_install_pkgs.py
test/unit/gen_class/yum_fetch_update_pkgs.py
test/unit/gen_class/mail_init.py
test/unit/gen_class/mail_add_2_msg.py
test/unit/gen_class/mail_create_body.py
test/unit/gen_class/mail_create_subject.py
test/unit/gen_class/mail_print_email.py
test/unit/gen_class/mail_read_stdin.py
test/unit/gen_class/mail_send_mail.py
test/unit/gen_class/mail_send_mailx.py

