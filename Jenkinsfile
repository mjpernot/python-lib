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
                pip2 install mock --user
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
                ./test/unit/gen_libs/and_is_true.py
                ./test/unit/gen_libs/bytes_2_readable.py
                ./test/unit/gen_libs/chk_crt_dir.py
                ./test/unit/gen_libs/chk_crt_file.py
                ./test/unit/gen_libs/chk_int.py
                ./test/unit/gen_libs/clear_file.py
                ./test/unit/gen_libs/cp_file.py
                ./test/unit/gen_libs/data_multi_out.py
                ./test/unit/gen_libs/del_not_in_list.py
                ./test/unit/gen_libs/display_data.py
                ./test/unit/gen_libs/file_2_list.py
                ./test/unit/gen_libs/file_search_cnt.py
                ./test/unit/gen_libs/file_search.py
                ./test/unit/gen_libs/get_base_dir.py
                ./test/unit/gen_libs/get_data.py
                ./test/unit/gen_libs/is_empty_file.py
                ./test/unit/gen_libs/list_dirs.py
                ./test/unit/gen_libs/merge_data_types.py
                ./test/unit/gen_libs/merge_two_dicts.py
                ./test/unit/gen_libs/month_delta.py
                ./test/unit/gen_libs/no_std_out.py
                ./test/unit/gen_libs/rotate_files.py
                ./test/unit/gen_libs/str_2_type.py
                ./test/unit/gen_libs/touch.py
                ./test/unit/gen_libs/validate_date.py
                ./test/unit/gen_libs/validate_int.py
                ./test/unit/gen_libs/write_file.py
                ./test/unit/gen_libs/write_file2.py
                ./test/unit/gen_libs/write_to_log.py
                ./test/unit/gen_class/ProgramLock_init.py
                ./test/unit/gen_class/ProgramLock_del.py
                ./test/unit/gen_class/ProgressBar_init.py
                ./test/unit/gen_class/SingleInstanceException.py
                ./test/unit/gen_class/Yum_init.py
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
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": ["test/unit/gen_libs/*.py","test/unit/gen_class/*.py"],
                                "target": "generic-local/highpoint/python-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
