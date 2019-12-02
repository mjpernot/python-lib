#!/bin/bash
# Unit test code coverage for gen_class module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=gen_class test/unit/gen_class/setup_mail.py
coverage run -a --source=gen_class test/unit/gen_class/Daemon_delpid.py
coverage run -a --source=gen_class test/unit/gen_class/Daemon_init.py
coverage run -a --source=gen_class test/unit/gen_class/Daemon_restart.py
coverage run -a --source=gen_class test/unit/gen_class/Daemon_start.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_filter_ignore.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_filter_keyword.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_filter_regex.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_find_marker.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_get_marker.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_init.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_load_ignore.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_load_keyword.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_load_loglist.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_load_marker.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_load_regex.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_set_marker.py
coverage run -a --source=gen_class test/unit/gen_class/LogFile_set_predicate.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_init.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_log_close.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_log_crit.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_log_debug.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_log_err.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_log_info.py
coverage run -a --source=gen_class test/unit/gen_class/Logger_log_warn.py
coverage run -a --source=gen_class test/unit/gen_class/ProgramLock_del.py
coverage run -a --source=gen_class test/unit/gen_class/ProgramLock_init.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_calc_and_update.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_init.py
coverage run -a --source=gen_class test/unit/gen_class/ProgressBar_update.py
coverage run -a --source=gen_class test/unit/gen_class/SingleInstanceException.py
coverage run -a --source=gen_class test/unit/gen_class/System_init.py
coverage run -a --source=gen_class test/unit/gen_class/System_set_host_name.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_distro.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_hostname.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_os.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_get_release.py
coverage run -a --source=gen_class test/unit/gen_class/Yum_init.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_init.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_add_2_msg.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_create_body.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_create_subject.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_print_email.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_read_stdin.py
coverage run -a --source=gen_class test/unit/gen_class/Mail_send_mail.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
