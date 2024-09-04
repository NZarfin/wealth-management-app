# Use an appropriate base image
FROM mysql:latest AS mysql

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root \
    MYSQL_DATABASE=mascots_db \
    MYSQL_USER=nadavsecureDB \
    MYSQL_PASSWORD=nadavsecureDBprivate 

# Expose MySQL port
EXPOSE 3306

# Use a separate stage to build the application image
FROM python:3.9-slim AS app

# Set environment variables for the application
ENV APP=target-app \
    SCOPE=user99

# Copy application files and install dependencies
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Copy the Dockerfile (assuming it's for building the app image)
COPY Dockerfile /app/Dockerfile

# Build the Docker image for the application
RUN docker build -t ${SCOPE}/${APP}:latest -f Dockerfile .

# Create a script to start the MySQL service and initialize the database
RUN echo '#!/bin/sh \n\
docker stop mysql-db || true \n\
docker rm mysql-db || true \n\
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=${DB_NAME} -e MYSQL_USER=${DB_USER} -e MYSQL_PASSWORD=${DB_PASSWORD} -d mysql:latest \n\
sleep 15 \n\
docker exec -i mysql-db mysql -unadavsecureDB -pnadavsecureDBprivate mascots_db <<EOF \n\
CREATE TABLE IF NOT EXISTS mascots ( \n\
    id INT AUTO_INCREMENT PRIMARY KEY, \n\
    guid VARCHAR(36) NOT NULL, \n\
    mascot VARCHAR(100) NOT NULL, \n\
    school VARCHAR(100) NOT NULL, \n\
    nickname VARCHAR(100) NOT NULL, \n\
    location VARCHAR(100) NOT NULL, \n\
    latlong VARCHAR(100) NOT NULL \n\
); \n\
INSERT INTO mascots (guid, mascot, school, nickname, location, latlong) VALUES \n\
('05024756-765e-41a9-89d7-1407436d9a58', 'Cy', 'Iowa State University', 'Cyclones', 'Ames, IA, USA', '42.026111,-93.648333'); \n\
EOF' > /app/start_services.sh

# Make the script executable
RUN chmod +x /app/start_services.sh

# Run the application container with MySQL
ENTRYPOINT ["/app/start_services.sh"]
CMD ["docker run --rm --name ${APP} --link mysql-db:mysql -p 8081:8081 -d ${SCOPE}/${APP}:latest"]
