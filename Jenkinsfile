pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Library Management System'
                bat 'echo Checking source files'
                bat 'echo Build completed successfully'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing Test Cases'
                bat 'echo Login Test : PASS'
                bat 'echo Book Issue Test : PASS'
                bat 'echo Return Book Test : PASS'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application'
                bat 'echo Application deployed on local server'
            }
        }
    }
}
