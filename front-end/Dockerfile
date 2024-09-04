# Frontend Dockerfile

# Use node as the base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json /app/package.json
RUN npm install

# Copy the rest of the application files
COPY . /app

# Start the application
CMD ["npm", "start"]

