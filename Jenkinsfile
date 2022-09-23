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
                ./test/unit/cmds_gen/unit_test_run.sh
                ./test/unit/errors/unit_test_run.sh
                ./test/unit/gen_libs/unit_test_run.sh
                ./test/unit/gen_class/unit_test_run.sh
                ./test/unit/machine/unit_test_run.sh
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
