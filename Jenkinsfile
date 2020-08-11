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
                ./test/unit/arg_parser/_make_dir.py
                ./test/unit/arg_parser/arg_add_def.py
                ./test/unit/arg_parser/arg_cond_req.py
                ./test/unit/arg_parser/arg_cond_req_or.py
                ./test/unit/arg_parser/arg_default.py
                ./test/unit/arg_parser/arg_dir_chk_crt.py
                ./test/unit/arg_parser/arg_file_chk.py
                ./test/unit/arg_parser/arg_noreq_xor.py
                ./test/unit/arg_parser/arg_parse2.py
                ./test/unit/arg_parser/arg_require.py
                ./test/unit/arg_parser/arg_req_or_lst.py
                ./test/unit/arg_parser/arg_req_xor.py
                ./test/unit/arg_parser/arg_set_path.py
                ./test/unit/arg_parser/arg_validate.py
                ./test/unit/arg_parser/arg_valid_val.py
                ./test/unit/arg_parser/arg_wildcard.py
                ./test/unit/arg_parser/arg_xor_dict.py
                ./test/unit/arg_parser/parse_multi.py
                ./test/unit/arg_parser/parse_single.py
                ./test/unit/arg_parser/file_create.py
                ./test/unit/cmds_gen/add_cmd.py
                ./test/unit/cmds_gen/create_cfg_array.py
                ./test/unit/cmds_gen/disconnect.py
                ./test/unit/cmds_gen/get_inst.py
                ./test/unit/cmds_gen/is_add_cmd.py
                ./test/unit/cmds_gen/run_prog.py
                ./test/unit/errors/emptyrowerror.py
                ./test/unit/errors/error.py
                ./test/unit/errors/nooptionerror.py
                ./test/unit/errors/notmastererror.py
                ./test/unit/errors/notslaveerror.py
                ./test/unit/errors/notyetimplementederror.py
                ./test/unit/errors/slavenotrunningerror.py
                ./test/unit/gen_libs/and_is_true.py
                ./test/unit/gen_libs/bytes_2_readable.py
                ./test/unit/gen_libs/chk_crt_dir.py
                ./test/unit/gen_libs/chk_crt_file.py
                ./test/unit/gen_libs/chk_int.py
                ./test/unit/gen_libs/clear_file.py
                ./test/unit/gen_libs/compress.py
                ./test/unit/gen_libs/cp_dir.py
                ./test/unit/gen_libs/cp_file2.py
                ./test/unit/gen_libs/cp_file.py
                ./test/unit/gen_libs/crt_file_time.py
                ./test/unit/gen_libs/date_range.py
                ./test/unit/gen_libs/del_not_and_list.py
                ./test/unit/gen_libs/del_not_in_list.py
                ./test/unit/gen_libs/dict_2_list.py
                ./test/unit/gen_libs/dict_2_std.py
                ./test/unit/gen_libs/dir_file_match.py
                ./test/unit/gen_libs/disk_usage.py
                ./test/unit/gen_libs/display_data.py
                ./test/unit/gen_libs/file_2_list.py
                ./test/unit/gen_libs/file_cleanup.py
                ./test/unit/gen_libs/file_search_cnt.py
                ./test/unit/gen_libs/file_search.py
                ./test/unit/gen_libs/filename_search.py
                ./test/unit/gen_libs/float_div.py
                ./test/unit/gen_libs/get_base_dir.py
                ./test/unit/gen_libs/get_data.py
                ./test/unit/gen_libs/get_date.py
                ./test/unit/gen_libs/get_inst.py
                ./test/unit/gen_libs/get_secs.py
                ./test/unit/gen_libs/get_time.py
                ./test/unit/gen_libs/help_func.py
                ./test/unit/gen_libs/in_list.py
                ./test/unit/gen_libs/is_empty_file.py
                ./test/unit/gen_libs/is_missing_lists.py
                ./test/unit/gen_libs/is_true.py
                ./test/unit/gen_libs/key_cleaner.py
                ./test/unit/gen_libs/list_2_dict.py
                ./test/unit/gen_libs/list_2_str.py
                ./test/unit/gen_libs/list_dirs.py
                ./test/unit/gen_libs/list_files.py
                ./test/unit/gen_libs/list_filter_files.py
                ./test/unit/gen_libs/load_module.py
                ./test/unit/gen_libs/make_md5_hash.py
                ./test/unit/gen_libs/make_zip.py
                ./test/unit/gen_libs/merge_data_types.py
                ./test/unit/gen_libs/merge_two_dicts.py
                ./test/unit/gen_libs/milli_2_readadble.py
                ./test/unit/gen_libs/month_days.py
                ./test/unit/gen_libs/month_delta.py
                ./test/unit/gen_libs/mv_file.py
                ./test/unit/gen_libs/mv_file2.py
                ./test/unit/gen_libs/normalize.py
                ./test/unit/gen_libs/not_in_list.py
                ./test/unit/gen_libs/no_std_out.py
                ./test/unit/gen_libs/openfile.py
                ./test/unit/gen_libs/pct_int.py
                ./test/unit/gen_libs/print_data.py
                ./test/unit/gen_libs/print_dict.py
                ./test/unit/gen_libs/prt_dict.py
                ./test/unit/gen_libs/prt_lvl.py
                ./test/unit/gen_libs/prt_msg.py
                ./test/unit/gen_libs/rename_file.py
                ./test/unit/gen_libs/rm_dup_list.py
                ./test/unit/gen_libs/rm_file.py
                ./test/unit/gen_libs/rm_newline_list.py
                ./test/unit/gen_libs/root_run.py
                ./test/unit/gen_libs/rotate_files.py
                ./test/unit/gen_libs/str_2_list.py
                ./test/unit/gen_libs/str_2_type.py
                ./test/unit/gen_libs/touch.py
                ./test/unit/gen_libs/validate_date.py
                ./test/unit/gen_libs/validate_int.py
                ./test/unit/gen_libs/write_file.py
                ./test/unit/gen_libs/write_file2.py
                ./test/unit/gen_libs/write_to_log.py
                ./test/unit/gen_class/get_inst.py
                ./test/unit/gen_class/setup_mail.py
                ./test/unit/gen_class/Daemon_delpid.py
                ./test/unit/gen_class/Daemon_init.py
                ./test/unit/gen_class/Daemon_restart.py
                ./test/unit/gen_class/Daemon_start.py
                ./test/unit/gen_class/LogFile_filter_ignore.py
                ./test/unit/gen_class/LogFile_filter_keyword.py
                ./test/unit/gen_class/LogFile_filter_regex.py
                ./test/unit/gen_class/LogFile_find_marker.py
                ./test/unit/gen_class/LogFile_get_marker.py
                ./test/unit/gen_class/LogFile_init.py
                ./test/unit/gen_class/LogFile_load_ignore.py
                ./test/unit/gen_class/LogFile_load_keyword.py
                ./test/unit/gen_class/LogFile_load_loglist.py
                ./test/unit/gen_class/LogFile_load_marker.py
                ./test/unit/gen_class/LogFile_load_regex.py
                ./test/unit/gen_class/LogFile_set_marker.py
                ./test/unit/gen_class/LogFile_set_predicate.py
                ./test/unit/gen_class/Logger_init.py
                ./test/unit/gen_class/Logger_log_close.py
                ./test/unit/gen_class/Logger_log_crit.py
                ./test/unit/gen_class/Logger_log_debug.py
                ./test/unit/gen_class/Logger_log_err.py
                ./test/unit/gen_class/Logger_log_info.py
                ./test/unit/gen_class/Logger_log_warn.py
                ./test/unit/gen_class/ProgramLock_init.py
                ./test/unit/gen_class/ProgramLock_del.py
                ./test/unit/gen_class/ProgressBar_init.py
                ./test/unit/gen_class/SingleInstanceException.py
                ./test/unit/gen_class/System_init.py
                ./test/unit/gen_class/System_set_host_name.py
                ./test/unit/gen_class/Yum_init.py
                ./test/unit/gen_class/Yum_get_hostname.py
                ./test/unit/gen_class/Yum_get_release.py
                ./test/unit/gen_class/Yum_get_os.py
                ./test/unit/gen_class/Yum_get_distro.py
                ./test/unit/gen_class/Yum_fetch_install_pkgs.py
                ./test/unit/gen_class/Yum_fetch_update_pkgs.py
                ./test/unit/gen_class/ProgressBar_update.py
                ./test/unit/gen_class/ProgressBar_calc_and_update.py
                ./test/unit/gen_class/Mail_init.py
                ./test/unit/gen_class/Mail_add_2_msg.py
                ./test/unit/gen_class/Mail_create_body.py
                ./test/unit/gen_class/Mail_create_subject.py
                ./test/unit/gen_class/Mail_print_email.py
                ./test/unit/gen_class/Mail_read_stdin.py
                ./test/unit/gen_class/Mail_send_mail.py
                ./test/unit/machine/linux.py
                ./test/unit/machine/amachine.py
                ./test/unit/machine/solaris.py
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
}
