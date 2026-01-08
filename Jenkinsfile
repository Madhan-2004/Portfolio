pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
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
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Start Flask Application') {
            steps {
                echo 'Starting Flask application...'
                sh 'nohup python app/app.py &'
                sh 'sleep 8'
            }
        }

        stage('Run Selenium Automation Tests') {
            steps {
                echo 'Running Selenium test cases...'
                sh 'pytest tests/'
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
