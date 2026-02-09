pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Library System...'
                bat 'echo Compiling library modules'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Library Tests...'
                bat 'echo Test Case 1: PASS'
                bat 'echo Test Case 2: PASS'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                bat 'echo Library System Deployed Successfully'
            }
        }
    }
}
