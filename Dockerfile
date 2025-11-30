FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
# COPY tests/ tests/  <-- In prod, we usually don't copy tests, but okay for lab.

# ❌ REMOVED: RUN python src/train.py
# The model.joblib must be provided from the outside now!

EXPOSE 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
