
import pandas as pd
import joblib

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_predict

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("data/tickets.csv")

X = df["ticket"]
y = df["category"]

# Load the pipeline definition from train_model.py
# Recreate the same pipeline for cross-validation.

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2)
    )),
    ("classifier", LogisticRegression(max_iter=1000))
])

# ==========================================
# 2. STRATIFIED 4-FOLD CROSS VALIDATION
# ==========================================

cv = StratifiedKFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

# ==========================================
# 3. DISPLAY RESULTS
# ==========================================

print("\nCLASSIFICATION EVALUATION")
print("==========================")

for i, score in enumerate(scores, start=1):
    print(f"Fold {i} Accuracy: {score * 100:.2f}%")

average_accuracy = scores.mean() * 100

print("\nAverage Accuracy:",
      round(average_accuracy, 2), "%")

print("Standard Deviation:",
      round(scores.std() * 100, 2), "%")

# ==========================================
# 4. CLASSIFICATION REPORT
# ==========================================

predictions = cross_val_predict(
    model,
    X,
    y,
    cv=cv
)

print("\nClassification Report:")
print(classification_report(
    y,
    predictions,
    zero_division=0
))

# ==========================================
# 5. CONFUSION MATRIX
# ==========================================

print("\nConfusion Matrix:")
print(confusion_matrix(y, predictions))

# ==========================================
# 6. COMPARE WITH TARGET
# ==========================================

print("\nTARGET EVALUATION")

if average_accuracy >= 90:
    print("Classification target achieved!")
else:
    print("Classification target not achieved yet.")

print("Target: 90%")
print("Actual:", round(average_accuracy, 2), "%")
