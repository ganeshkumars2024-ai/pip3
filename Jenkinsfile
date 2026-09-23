pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_EXTRA_CHECK', defaultValue: true, description: 'Run the extra check stage')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ganeshkumars2024-ai/pip3.git'
            }
        }
        stage('Build') {
            steps {
                bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m py_compile app.py'
                echo 'Build successful: app.py compiled with no syntax errors'
            }
        }
        stage('Extra Check') {
            when {
                expression { params.RUN_EXTRA_CHECK == true }
            }
            steps {
                echo 'Running extra check: verifying greet() output format...'
                bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -c "from app import greet; print(greet(\'Student\'))"'
            }
        }
    }
}