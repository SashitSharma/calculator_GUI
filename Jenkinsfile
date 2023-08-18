pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build Code'
            }
        }

        stage('Test') {
            steps {
                echo 'Test Code'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy code'
            }
        }
    }
    post
    {
        always
        {
            emailext body: 'Summary', subject: 'Pipeline Status', to: 'SashitSHarma@gmail.com'
        }
    }
}
