pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Compile the .cpp file using a shell script
                    sh 'g++ -o your_executable PES1UG21CS583.cpp'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Print output of the .cpp file using a shell script
                    sh './your_executable'
                }
            }
        }
        stage('Deploy') {
            steps {
                // Add deployment steps here if necessary
                echo 'Deployment steps go here'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
