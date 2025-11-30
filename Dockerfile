# 1. Base Image: Start with a lightweight Linux + Python 3.9
FROM python:3.9-slim

# 2. Setup Work Directory: Create a folder inside the container
WORKDIR /app

# 3. Copy Requirements: Move the file from laptop to container
COPY requirements.txt .

# 4. Install Dependencies: Run pip inside the container
# --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Code: Move the src folder
COPY src/ src/
COPY tests/ tests/ 

# 6. Default Command: What happens when we run the container?
# For now, let's make it run the training script
CMD ["python", "-c", "from src.train import train_model; print(train_model())"]
