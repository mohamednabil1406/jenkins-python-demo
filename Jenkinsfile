pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['DEV', 'TEST', 'PROD'],
            description: 'Select the deployment environment'
        )

        booleanParam(
            name: 'RUN_TESTS',
            defaultValue: true,
            description: 'Run automated tests'
        )
    }

    environment {
        APP_NAME = 'python-ci-demo'
        PYTHON = 'C:\\Users\\devop\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {

        stage('Build') {
            steps {
                echo "Application: ${APP_NAME}"
                echo "Selected Environment: ${params.ENVIRONMENT}"
                echo "Build Number: ${env.BUILD_NUMBER}"

                bat '"%PYTHON%" app.py'
            }
        }

        stage('Test') {
            when {
                expression {
                    params.RUN_TESTS
                }
            }

            steps {
                echo "Running tests..."

                bat '"%PYTHON%" test_app.py'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }

        failure {
            echo "❌ Pipeline failed!"
        }
    }
}