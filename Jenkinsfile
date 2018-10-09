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
                sh './test/unit/gen_libs/file_2_list.py'
            }
        }
    }
}
