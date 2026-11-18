
import pandas as pd

from classifier import predict_severity
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================================
# 1. LOAD TEST DATA
# ==========================================

df = pd.read_csv("data/severity_test.csv")

actual = df["actual_severity"]

# ==========================================
# 2. PREDICT SEVERITY
# ==========================================

predicted = df["ticket"].apply(predict_severity)

# ==========================================
# 3. DISPLAY PREDICTIONS
# ==========================================

print("\nSEVERITY EVALUATION")
print("===================")

for i, row in df.iterrows():

    print("\nTicket:", row["ticket"])
    print("Actual:", actual[i])
    print("Predicted:", predicted[i])

    if actual[i] == predicted[i]:
        print("Result: Correct")
    else:
        print("Result: Incorrect")

# ==========================================
# 4. CALCULATE ACCURACY
# ==========================================

accuracy = accuracy_score(actual, predicted)

print("\nSeverity Accuracy:",
      round(accuracy * 100, 2), "%")

# ==========================================
# 5. CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(classification_report(
    actual,
    predicted,
    labels=["Low", "Medium", "High", "Critical"],
    zero_division=0
))

# ==========================================
# 6. CONFUSION MATRIX
# ==========================================

print("\nConfusion Matrix:")

print(confusion_matrix(
    actual,
    predicted,
    labels=["Low", "Medium", "High", "Critical"]
))

# ==========================================
# 7. TARGET COMPARISON
# ==========================================

print("\nTARGET EVALUATION")

if accuracy >= 0.85:
    print("Severity target achieved!")
else:
    print("Severity target not achieved yet.")

print("Target: 85%")
print("Actual:", round(accuracy * 100, 2), "%")
