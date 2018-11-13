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
                cd /var/jenkins/workspace/Highpoint/python-lib
                pip2 install mock --user
                ./test/unit/gen_libs/chk_crt_dir.py
                ./test/unit/gen_libs/chk_crt_file.py
                ./test/unit/gen_libs/clear_file.py
                ./test/unit/gen_libs/cp_file.py
                ./test/unit/gen_libs/data_multi_out.py
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
                ./test/unit/gen_libs/touch.py
                ./test/unit/gen_libs/write_file.py
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/gen_libs/code_coverage.sh'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner"
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
