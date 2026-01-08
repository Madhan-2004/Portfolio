pipeline {
    agent any

    environment {
        PYTHON = '"C:\\Users\\arunr\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\IDLE (Python 3.10 64-bit).lnk"'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/Madhan-2004/Portfolio'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '"%PYTHON%" -m pip install --upgrade pip'
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Start Flask Application') {
            steps {
                echo 'Starting Flask application...'
                bat 'start /B "%PYTHON%" app\\app.py'
                bat 'timeout /T 8'
            }
        }

        stage('Run Selenium Automation Tests') {
            steps {
                echo 'Running Selenium test cases...'
                bat '"%PYTHON%" -m pytest tests'
            }
        }

        stage('Deploy') {
            steps {
                echo 'All tests passed. Deployment approved.'
            }
        }
    }

    post {
        success {
            echo 'PIPELINE SUCCESS: All stages executed successfully. Application is stable.'
        }

        failure {
            echo 'PIPELINE FAILURE: Tests failed or error occurred. Deployment blocked.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
