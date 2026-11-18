
from classifier import calculate_priority

test_cases = [
    ("Critical", "High", "P1"),
    ("Critical", "Low", "P1"),
    ("High", "High", "P1"),
    ("High", "Low", "P2"),
    ("Medium", "Low", "P3"),
    ("Low", "Low", "P4")
]

correct = 0

print("\nPRIORITY EVALUATION")
print("===================")

for severity, impact, expected in test_cases:

    predicted = calculate_priority(severity, impact)

    result = "PASS" if predicted == expected else "FAIL"

    if predicted == expected:
        correct += 1

    print(
        f"Severity: {severity}, "
        f"Impact: {impact}, "
        f"Expected: {expected}, "
        f"Predicted: {predicted}, "
        f"{result}"
    )

accuracy = correct / len(test_cases) * 100

print("\nPriority Rule Accuracy:", accuracy, "%")
