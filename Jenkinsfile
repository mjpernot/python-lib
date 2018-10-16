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
                sh './test/unit/gen_libs/chk_crt_dir.py'
                sh './test/unit/gen_libs/chk_crt_file.py'
                sh './test/unit/gen_libs/clear_file.py'
                sh './test/unit/gen_libs/cp_file.py'
                sh './test/unit/gen_libs/display_data.py'
                sh './test/unit/gen_libs/file_2_list.py'
                sh './test/unit/gen_libs/file_search_cnt.py'
                sh './test/unit/gen_libs/file_search.py'
                sh './test/unit/gen_libs/get_base_dir.py'
                sh './test/unit/gen_libs/get_data.py'
                sh './test/unit/gen_libs/is_empty_file.py'
                sh './test/unit/gen_libs/list_dirs.py'
                sh './test/unit/gen_libs/merge_data_types.py'
                sh './test/unit/gen_libs/merge_two_dicts.py'
                sh './test/unit/gen_libs/month_delta.py'
                sh './test/unit/gen_libs/no_std_out.py'
                sh './test/unit/gen_libs/touch.py'
                sh './test/unit/gen_libs/write_file.py'
            }
        }
        stage('SonarQube analysis') {
            steps {
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
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "python-lib/*.py",
                                "target": "python-lib"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
