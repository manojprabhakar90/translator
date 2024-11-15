# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure Poetry is in the PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy the Poetry configuration and lock files first for better caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the project files into the container
COPY . /app

# Expose the port for your application (if needed, for example 8000)
EXPOSE 8000

# Default command (adjust based on your actual app)
CMD ["poetry", "run", "python", "translate/translation.py"]
