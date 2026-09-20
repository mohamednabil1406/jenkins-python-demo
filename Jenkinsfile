pipeline {
    agent any

    stages {

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\devop\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\devop\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test_app.py'
            }
        }
    }
}