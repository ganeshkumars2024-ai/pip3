pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ganeshkumars2024-ai/pip3.git'
            }
        }
        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" app.py'
                    }
                }
                stage('Backend Check') {
                    steps {
                        bat '"C:\\Users\\HP\\AppData\\Local\\Python\\bin\\python.exe" app.py'
                    }
                }
            }
        }
        stage('Summary') {
            steps {
                echo 'Both frontend and backend checks are complete.'
            }
        }
    }
}