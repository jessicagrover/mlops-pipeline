# Use Python 3.8 image
FROM python:3.8-slim

# Set working directory inside container
WORKDIR /app

# Copy the model and FastAPI app
COPY model.pkl /app
COPY main.py /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
