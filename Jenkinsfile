pipeline {
    agent any  
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
        stage('Stop/Remove existing MySQL Service') {
            steps {
                // Stop and remove any existing MySQL container
                sh '''
                docker stop mysql-db || true
                docker rm mysql-db || true
                '''
                // Wait for MySQL to be ready
                sh '''
                sleep 15
                '''
            }
        }
        stage('Run MySQL') {
            steps {
                // Start MySQL container using credentials from .env
                sh '''
                docker run -d --name mysql-db --network=${DOCKER_NETWORK} \
                    -e MYSQL_ROOT_PASSWORD=${DB_ROOT_PASSWORD} \
                    -e MYSQL_DATABASE=${DB_NAME} \
                    -e MYSQL_USER=${DB_USER} \
                    -e MYSQL_PASSWORD=${DB_PASSWORD} \
                    -p 3306:3306 mysql:latest
                '''
            }
        }

        stage('Build Flask App Image From Docker') {
            steps {
                // Build the Flask application Docker image
                sh 'docker build -t flask-app -f back-end/app/Dockerfile .'
            }
        }

        stage('Run Flask App') {
            steps {
                // Start Flask app container, connecting it to the MySQL container
                sh '''
                docker run -d --name flask-app --network=${DOCKER_NETWORK} \
                    -e DB_HOST=${DB_HOST} \
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
                echo "Pushed to production branch"
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
                echo "succesfully Cleaned up ${DOCKER_NETWORK}"
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

