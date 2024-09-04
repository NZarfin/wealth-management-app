# Stage 1: Compiler - Build the virtual environment and install dependencies
FROM python:3.9-slim as compiler

# Create a working directory
WORKDIR /app/

# Set environment variable to ensure output is not buffered
ENV PYTHONUNBUFFERED=1

# Create virtual environment in /opt/venv
RUN python -m venv /opt/venv

# Activate the virtual environment by updating PATH
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies in the virtual environment
# Ensure you copy the requirements.txt into the image.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Stage 2: Runner - Copy the virtual environment and the application code
FROM python:3.9-slim as runner

# Create a working directory
WORKDIR /app/

# Copy the virtual environment from the compiler stage
COPY --from=compiler /opt/venv /opt/venv

# Activate the virtual environment by updating PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code
# It's good to ensure only necessary files are copied. 
# Consider using a .dockerignore file to exclude files not needed in the image.
COPY . /app/

# Expose the port the app runs on
EXPOSE 8001

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8001", "-w", "4"]
