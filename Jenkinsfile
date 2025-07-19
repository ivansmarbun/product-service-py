pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t product-service-py:${env.BUILD_NUMBER} ."
                    sh "docker tag product-service-py:${env.BUILD_NUMBER} product-service-py:latest"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh "docker run --rm product-service-py:${env.BUILD_NUMBER} python -m unittest discover"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker stop product-service-container || true"
                    sh "docker rm product-service-container || true"

                    sh "docker run -d -p 5002:5002 --name product-service-container product-service-py:${env.BUILD_NUMBER}"

                    echo "Product Service deployed on port 5002"
                    echo "Access it at http://<Your-Jenkins-Host-IP>:5002 (or localhost if Jenkins is local)"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "Pipeline for Product Service completed successfully!"
        }
        failure {
            echo "Pipeline for Product Service failed. Check console output for errors."
        }
    }
}
