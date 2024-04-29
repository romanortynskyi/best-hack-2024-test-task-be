FROM python:3.12.3-slim-bookworm

# Create a working directory for your app
WORKDIR /app

# Copy Poetry configuration files (pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock ./

# Install Poetry itself (optional, if not already installed in the image)
RUN pip install poetry

# Disable virtualenv creation (Poetry manages dependencies)
# RUN poetry config virtualenvs.create false

# Install dependencies (excluding development ones)
RUN poetry install --only main

# Copy your app code
COPY . .

# Expose port (adjust if your app listens on a different port)
EXPOSE 5000

ENV SQLALCHEMY_DATABASE_URI=arn:aws:secretsmanager:us-east-1:891377136147:secret:best-hack-2024-test-task-be/sqlalchemy-database-uri-mdOYL2

RUN cd test_task_be && poetry run alembic upgrade head

# Set the command to run your app (replace "app:app" with your entry point)
CMD ["poetry", "run", "python", "test_task_be/app.py"]
