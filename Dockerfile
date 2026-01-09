# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Start Uvicorn ASGI server
CMD ["uvicorn", "skillbridge.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
