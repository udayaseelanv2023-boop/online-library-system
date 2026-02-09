pipeline {
    agent any

    environment {
        APP_NAME = "Student Grade App"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building ${APP_NAME}"
                bat 'python student_app.py'
            }
        }

        stage('Test') {
            steps {
                echo "Running Unit Tests"
                bat 'python test_student_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application (simulated)"
                bat 'echo Application deployed successfully'
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed! Check logs."
        }
    }
}
