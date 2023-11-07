pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                /usr/bin/python2 ./test/unit/arg_parser/_make_dir.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_add_def.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_cond_req.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_cond_req_or.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_default.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_dir_chk.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_dir_chk_crt.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_file_chk.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_noreq_xor.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_parse2.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_require.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_req_or_lst.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_req_xor.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_set_path.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_validate.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_valid_val.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_wildcard.py
                /usr/bin/python2 ./test/unit/arg_parser/arg_xor_dict.py
                /usr/bin/python2 ./test/unit/arg_parser/parse_multi.py
                /usr/bin/python2 ./test/unit/arg_parser/parse_single.py
                /usr/bin/python2 ./test/unit/arg_parser/file_create.py
                /usr/bin/python2 ./test/unit/errors/emptyrowerror.py
                /usr/bin/python2 ./test/unit/errors/error.py
                /usr/bin/python2 ./test/unit/errors/nooptionerror.py
                /usr/bin/python2 ./test/unit/errors/notmastererror.py
                /usr/bin/python2 ./test/unit/errors/notslaveerror.py
                /usr/bin/python2 ./test/unit/errors/notyetimplementederror.py
                /usr/bin/python2 ./test/unit/errors/slavenotrunningerror.py
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
                /usr/bin/python2 ./test/unit/gen_libs/get_inst.py
                /usr/bin/python2 ./test/unit/gen_libs/get_date.py
                /usr/bin/python2 ./test/unit/gen_libs/get_secs.py
                /usr/bin/python2 ./test/unit/gen_libs/get_time.py
                /usr/bin/python2 ./test/unit/gen_libs/has_whitespace.py
                /usr/bin/python2 ./test/unit/gen_libs/help_func.py
                /usr/bin/python2 ./test/unit/gen_libs/in_list.py
                /usr/bin/python2 ./test/unit/gen_libs/is_add_cmd.py
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
                /usr/bin/python2 ./test/unit/gen_class/get_inst.py
                /usr/bin/python2 ./test/unit/gen_class/setup_mail.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_add_def.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_cond_req.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_cond_req_or.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_default.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_dir_chk.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_dir_chk_crt.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_dir_crt.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_exist.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_file_chk.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_noreq_xor.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_parse2.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_require.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_req_or_lst.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_req_xor.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_set_path.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_validate.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_valid_val.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_wildcard.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_arg_xor_dict.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_delete_arg.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_get_args.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_get_args_keys.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_get_val.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_init.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_insert_arg.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_parse_multi.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_parse_single.py
                /usr/bin/python2 ./test/unit/gen_class/argparser_update_arg.py
                /usr/bin/python2 ./test/unit/gen_class/daemon_daemonize.py
                /usr/bin/python2 ./test/unit/gen_class/daemon_delpid.py
                /usr/bin/python2 ./test/unit/gen_class/daemon_init.py
                /usr/bin/python2 ./test/unit/gen_class/daemon_restart.py
                /usr/bin/python2 ./test/unit/gen_class/daemon_start.py
                /usr/bin/python2 ./test/unit/gen_class/daemon_stop.py
                /usr/bin/python2 ./test/unit/gen_class/daemon2_init.py
                /usr/bin/python2 ./test/unit/gen_class/daemon2_daemonize.py
                /usr/bin/python2 ./test/unit/gen_class/daemon2_del_pid.py
                /usr/bin/python2 ./test/unit/gen_class/daemon2_restart.py
                /usr/bin/python2 ./test/unit/gen_class/daemon2_start.py
                /usr/bin/python2 ./test/unit/gen_class/daemon2_stop.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_filter_ignore.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_filter_keyword.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_filter_regex.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_find_marker.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_get_marker.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_init.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_load_ignore.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_load_keyword.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_load_loglist.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_load_marker.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_load_regex.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_set_marker.py
                /usr/bin/python2 ./test/unit/gen_class/logfile_set_predicate.py
                /usr/bin/python2 ./test/unit/gen_class/logger_init.py
                /usr/bin/python2 ./test/unit/gen_class/logger_log_close.py
                /usr/bin/python2 ./test/unit/gen_class/logger_log_crit.py
                /usr/bin/python2 ./test/unit/gen_class/logger_log_debug.py
                /usr/bin/python2 ./test/unit/gen_class/logger_log_err.py
                /usr/bin/python2 ./test/unit/gen_class/logger_log_info.py
                /usr/bin/python2 ./test/unit/gen_class/logger_log_warn.py
                /usr/bin/python2 ./test/unit/gen_class/progressbar_init.py
                /usr/bin/python2 ./test/unit/gen_class/progressbar_update.py
                /usr/bin/python2 ./test/unit/gen_class/progressbar_calc_and_update.py
                /usr/bin/python2 ./test/unit/gen_class/singleinstanceexception.py
                /usr/bin/python2 ./test/unit/gen_class/programlock_init.py
                /usr/bin/python2 ./test/unit/gen_class/programlock_del.py
                /usr/bin/python2 ./test/unit/gen_class/system_init.py
                /usr/bin/python2 ./test/unit/gen_class/system_set_host_name.py
                /usr/bin/python2 ./test/unit/gen_class/timeformat_add_format.py
                /usr/bin/python2 ./test/unit/gen_class/timeformat_create_adhoc_hack.py
                /usr/bin/python2 ./test/unit/gen_class/timeformat_create_hack.py
                /usr/bin/python2 ./test/unit/gen_class/timeformat_get_hack.py
                /usr/bin/python2 ./test/unit/gen_class/timeformat_init.py
                /usr/bin/python2 ./test/unit/gen_class/yum_init.py
                /usr/bin/python2 ./test/unit/gen_class/yum_get_hostname.py
                /usr/bin/python2 ./test/unit/gen_class/yum_get_os.py
                /usr/bin/python2 ./test/unit/gen_class/yum_get_distro.py
                /usr/bin/python2 ./test/unit/gen_class/yum_get_release.py
                /usr/bin/python2 ./test/unit/gen_class/yum_fetch_install_pkgs.py
                /usr/bin/python2 ./test/unit/gen_class/yum_fetch_update_pkgs.py
                /usr/bin/python2 ./test/unit/gen_class/mail_init.py
                /usr/bin/python2 ./test/unit/gen_class/mail_add_2_msg.py
                /usr/bin/python2 ./test/unit/gen_class/mail_create_body.py
                /usr/bin/python2 ./test/unit/gen_class/mail_create_subject.py
                /usr/bin/python2 ./test/unit/gen_class/mail_print_email.py
                /usr/bin/python2 ./test/unit/gen_class/mail_read_stdin.py
                /usr/bin/python2 ./test/unit/gen_class/mail_send_mail.py
                /usr/bin/python2 ./test/unit/gen_class/mail_send_mailx.py
                /usr/bin/python2 ./test/unit/machine/linux.py
                /usr/bin/python2 ./test/unit/machine/amachine.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": ["test/unit/gen_libs/*.py","test/unit/gen_class/*.py"],
                                "target": "pypi-proj-local/highpoint/python-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
