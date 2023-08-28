pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //sh 'pip install -e ./PiCarProject/ '
                sh 'python3 *.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest *.py'
            }
        }
    }
}