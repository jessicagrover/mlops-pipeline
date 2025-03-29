import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load a dataset
data = load_iris()
X, y = data.data, data.target

# Train a model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the trained model to a file
joblib.dump(model, 'model.joblib')
