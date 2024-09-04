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

# Copy the requirements file and install dependencies in the virtual environment
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runner - Copy the virtual environment and the application code
FROM python:3.9-slim as runner

# Create a working directory
WORKDIR /app/

# Copy the virtual environment from the compiler stage
COPY --from=compiler /opt/venv /opt/venv

# Activate the virtual environment by updating PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code
COPY . /app/

# Run the Flask application
CMD ["python", "app.py"]