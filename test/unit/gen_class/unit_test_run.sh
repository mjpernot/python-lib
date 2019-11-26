#!/bin/bash
# Unit testing program for the gen_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: gen_class module"  
test/unit/gen_class/setup_mail.py
test/unit/gen_class/Daemon_init.py
test/unit/gen_class/LogFile_filter_ignore.py
test/unit/gen_class/LogFile_filter_keyword.py
test/unit/gen_class/LogFile_filter_regex.py
test/unit/gen_class/LogFile_find_marker.py
test/unit/gen_class/LogFile_get_marker.py
test/unit/gen_class/LogFile_init.py
test/unit/gen_class/LogFile_load_ignore.py
test/unit/gen_class/LogFile_load_keyword.py
test/unit/gen_class/LogFile_load_loglist.py
test/unit/gen_class/LogFile_load_marker.py
test/unit/gen_class/LogFile_load_regex.py
test/unit/gen_class/LogFile_set_predicate.py
test/unit/gen_class/Logger_init.py
test/unit/gen_class/Logger_log_close.py
test/unit/gen_class/Logger_log_crit.py
test/unit/gen_class/Logger_log_debug.py
test/unit/gen_class/Logger_log_err.py
test/unit/gen_class/Logger_log_info.py
test/unit/gen_class/Logger_log_warn.py
test/unit/gen_class/ProgressBar_init.py
test/unit/gen_class/ProgressBar_update.py
test/unit/gen_class/ProgressBar_calc_and_update.py
test/unit/gen_class/SingleInstanceException.py
test/unit/gen_class/ProgramLock_init.py
test/unit/gen_class/ProgramLock_del.py
test/unit/gen_class/System_init.py
test/unit/gen_class/System_set_host_name.py
test/unit/gen_class/Yum_init.py
test/unit/gen_class/Yum_get_hostname.py
test/unit/gen_class/Yum_get_os.py
test/unit/gen_class/Yum_get_distro.py
test/unit/gen_class/Yum_get_release.py
test/unit/gen_class/Yum_fetch_install_pkgs.py
test/unit/gen_class/Yum_fetch_update_pkgs.py
test/unit/gen_class/Mail_init.py
test/unit/gen_class/Mail_add_2_msg.py
test/unit/gen_class/Mail_create_body.py
test/unit/gen_class/Mail_create_subject.py
test/unit/gen_class/Mail_print_email.py
test/unit/gen_class/Mail_read_stdin.py
test/unit/gen_class/Mail_send_mail.py

