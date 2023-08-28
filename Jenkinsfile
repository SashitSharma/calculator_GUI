pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //sh 'pip install -e ./PiCarProject/ '
                sh 'python3 Unittests/*.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest Unittests/*.py'
            }
        }
    }
}