pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Madhan-2004/Portfolio.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Start Flask App') {
            steps {
                sh 'nohup python app/app.py &'
                sh 'sleep 8'
            }
        }

        stage('Run Automation Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy (Only if Tests Pass)') {
            when {
                success()
            }
            steps {
                echo 'All tests passed. Deployment approved.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. App is stable.'
        }

        failure {
            echo 'Pipeline failed. Tests did not pass. Deployment blocked.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
