for maven:
pipeline {
    agent any
    
    tools {
        maven '3.6.3'
    }
    
    stages {
      stage('Test') {
            steps {
                script {
                    // Compile your code here
                    sh 'mvn test' // Adjust the command based on your build tool
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Compile your code here
                    sh 'mvn clean compile' // Adjust the command based on your build tool
                }
            }
        }
    }
    
    post {
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed. Check for compilation errors.'
        }
    }
}

