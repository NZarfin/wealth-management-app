pipeline {
    agent any

    environment {
        DOCKER_NETWORK = 'backend-network'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from version control
                checkout scm
            }
        }

        stage('Load Env File') {
            steps {
                script {
                    def envProps = readFile '.env'
                    envProps.split('\n').each {
                        def keyValue = it.split('=')
                        if (keyValue.length == 2) {
                            env."${keyValue[0]}" = keyValue[1].trim()
                        }
                    }
                }
            }
        }

        stage('Setup Docker Network') {
            steps {
                // Create a Docker network for MySQL and Flask to communicate
                sh 'docker network create ${DOCKER_NETWORK} || true'
            }
        }

        stage('Run MySQL') {
            steps {
                // Start MySQL container using credentials from .env
                sh '''
                docker run -d --name mysql-db --network=${DOCKER_NETWORK} \
                    -e MYSQL_ROOT_PASSWORD=rootpassword \
                    -e MYSQL_DATABASE=${DB_NAME} \
                    -e MYSQL_USER=${DB_USER} \
                    -e MYSQL_PASSWORD=${DB_PASSWORD} \
                    -p 3306:3306 mysql:latest
                '''
            }
        }

        stage('Build Flask App') {
            steps {
                // Build the Flask application Docker image
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Flask App') {
            steps {
                // Start Flask app container, connecting it to the MySQL container
                sh '''
                docker run -d --name flask-app --network=${DOCKER_NETWORK} \
                    -e DB_HOST=mysql-db \
                    -e DB_NAME=${DB_NAME} \
                    -e DB_USER=${DB_USER} \
                    -e DB_PASSWORD=${DB_PASSWORD} \
                    -e SECRET_KEY=${SECRET_KEY} \
                    -p 8081:8081 flask-app
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests in Flask container
                sh '''
                docker exec flask-app pytest --disable-warnings
                '''
            }
        }

        stage('Push to Production Branch') {
            when {
                // Only run this stage if all previous stages pass
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                // Push to a new production branch if the tests pass
                sh '''
                git checkout -b production || git checkout production
                git add .
                git commit -m "Promote to production branch after successful tests"
                git push origin production
                '''
            }
        }

        stage('Clean up') {
            steps {
                // Stop and remove containers
                sh '''
                docker stop mysql-db flask-app || true
                docker rm mysql-db flask-app || true
                docker network rm ${DOCKER_NETWORK} || true
                '''
            }
        }
    }

    post {
        always {
            // Always perform clean-up steps
            sh 'docker system prune -f'
        }
    }
}
