# 🚀 MLOps CI/CD Lab: End-to-End Pipeline

This repository demonstrates a production-grade **MLOps (Machine Learning Operations)** pipeline implemented using **GitHub Actions**, **Docker**, and **FastAPI**.

It moves beyond simple model training scripts to a structured, automated ecosystem that ensures code quality, reproducibility, and automated deployment.

## 🏗️ Architecture

The system is designed with a **Separation of Concerns** principle:

1.  **CI (Continuous Integration):** Triggered on every code push. verifying the code logic via Unit Tests.
2.  **CD (Continuous Delivery):** Packages the model and API into a Docker container and pushes it to Docker Hub.
3.  **CT (Continuous Training):** A decoupled workflow triggered manually (or via schedule) to retrain the model on heavy compute, completely separate from the deployment logic.

---

## 📂 Project Structure

```text
mlops-cicd-lab/
├── .github/workflows/
│   ├── ci-pipeline.yml    # CI/CD: Tests code & Builds Docker image (if tests pass)
│   └── retrain.yml        # CT: Retrains model & Updates artifact (Manual Trigger)
├── docs/                  # Project documentation and tutorials
├── src/
│   ├── app.py             # FastAPI serving application
│   ├── train.py           # Model training logic (produces model.joblib)
│   └── preprocessing.py   # Data cleaning logic
├── tests/                 # Pytest unit tests
├── Dockerfile             # Recipe for the production image
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
---

## ⚙️ Workflows Explained

### 1. The Gatekeeper (CI Pipeline)
*   **Trigger:** `git push` to `main`.
*   **Action:** Installs dependencies and runs `pytest`.
*   **Goal:** Ensures no broken code (syntax errors, logic bugs) ever reaches the deployment stage.

### 2. The Delivery Truck (CD Pipeline)
*   **Trigger:** Successful completion of the CI Tests.
*   **Action:**
    1.  Logs into Docker Hub using GitHub Secrets.
    2.  Builds a Docker image containing the code and the model.
    3.  Pushes the image to Docker Hub with the `latest` tag.

### 3. The Factory (CT Pipeline)
*   **Trigger:** Manual "Workflow Dispatch" (UI Button).
*   **Action:**
    1.  Runs `src/train.py` to generate a new `model.joblib`.
    2.  Uploads the model as a GitHub Artifact.
    3.  Triggers the build process to package this **new** model into the Docker image.
*   **Why?** This decouples heavy training (which might need GPUs) from the lightweight CI checks.

---
## 🚀 How to Run Locally

### Prerequisites
*   Python 3.9+
*   Docker

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run Tests
```bash
pytest
```

### 3. Build & Run Docker Container
```bash
# Build the image
docker build -t mlops-api:v1 .

# Run the container (Mapping port 8000)
docker run -p 8000:8000 mlops-api:v1
```

### 4. Test the API
Once the container is running, open your browser to the Swagger UI:
> `http://localhost:8000/docs`

Or use curl:
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

---
## 🛠️ Technologies Used

*   **GitHub Actions:** For orchestration.
*   **Docker:** For containerization and environment consistency.
*   **FastAPI:** For high-performance model serving.
*   **Scikit-Learn:** For the ML model (Random Forest).
*   **Pytest:** For automated testing.
*   **Docker Hub:** As the Container Registry.

---
### 📖 Documentation

A full step-by-step notebook explaining the creation of this pipeline can be found in `docs/project_documentation.ipynb`.
