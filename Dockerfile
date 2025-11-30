FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY tests/ tests/

# 1. Build-Time Training: Train the model so it is baked into the image
# (In advanced MLOps, we download from S3/MLflow, but this is best for starting)
RUN python src/train.py

# 2. Expose the port (Documentation only)
EXPOSE 8000

# 3. Run the API Server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
