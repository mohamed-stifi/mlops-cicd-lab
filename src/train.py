# src/train.py (Updated)
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model(n_estimators: int = 100):
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    # --- NEW: Save the model ---
    joblib.dump(model, "model.joblib")
    print(f"Model saved to model.joblib with accuracy: {accuracy}")
    
    return model, accuracy

if __name__ == "__main__":
    train_model()
