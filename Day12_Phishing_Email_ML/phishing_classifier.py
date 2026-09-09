import pandas as pd
import json

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# DAY 12 - PHISHING EMAIL DETECTION WITH ML
# ============================================================

print("=" * 60)
print("DAY 12 - PHISHING EMAIL DETECTION WITH ML")
print("=" * 60)


# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

dataset_path = "Day12_Phishing_Email_ML/phishing_dataset.csv"

try:
    df = pd.read_csv(dataset_path)
    print("\nDataset loaded successfully.")

except FileNotFoundError:
    print("\nERROR: phishing_dataset.csv not found.")
    exit()


# Check required columns
if "email" not in df.columns or "label" not in df.columns:
    print("\nERROR: Dataset must contain 'email' and 'label' columns.")
    exit()


print(f"Total samples: {len(df)}")


# ------------------------------------------------------------
# 2. DATASET INFORMATION
# ------------------------------------------------------------

phishing_count = int((df["label"] == 1).sum())
legitimate_count = int((df["label"] == 0).sum())

print("\nDataset Information")
print("-" * 40)
print(f"Total samples : {len(df)}")
print(f"Phishing      : {phishing_count}")
print(f"Legitimate    : {legitimate_count}")


# ------------------------------------------------------------
# 3. PREPARE DATA
# ------------------------------------------------------------

X = df["email"].astype(str)
y = df["label"].astype(int)


# ------------------------------------------------------------
# 4. TRAIN / TEST SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print(f"\nTraining samples : {len(X_train)}")
print(f"Testing samples  : {len(X_test)}")


# ------------------------------------------------------------
# 5. CREATE NAIVE BAYES MODEL
# ------------------------------------------------------------

print("\nTraining Naive Bayes model...")

model = Pipeline([
    ("vectorizer", CountVectorizer(
        lowercase=True,
        stop_words="english"
    )),
    ("classifier", MultinomialNB())
])


# ------------------------------------------------------------
# 6. TRAIN MODEL
# ------------------------------------------------------------

model.fit(X_train, y_train)

print("Model training completed successfully.")


# ------------------------------------------------------------
# 7. MAKE PREDICTIONS
# ------------------------------------------------------------

y_pred = model.predict(X_test)


# ------------------------------------------------------------
# 8. CALCULATE ACCURACY
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"\nAccuracy: {accuracy * 100:.2f}%")


# ------------------------------------------------------------
# 9. CONFUSION MATRIX
# ------------------------------------------------------------

cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("\nConfusion Matrix")
print("-" * 40)
print("                 Predicted")
print("                 Legit  Phishing")
print(
    f"Actual Legit     {cm[0][0]:5d}   {cm[0][1]:5d}"
)
print(
    f"Actual Phishing  {cm[1][0]:5d}   {cm[1][1]:5d}"
)


# ------------------------------------------------------------
# 10. CLASSIFICATION REPORT
# ------------------------------------------------------------

report = classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Legitimate", "Phishing"],
    output_dict=True
)

print("\nClassification Report")
print("-" * 40)

print(
    classification_report(
        y_test,
        y_pred,
        labels=[0, 1],
        target_names=["Legitimate", "Phishing"]
    )
)


# ------------------------------------------------------------
# 11. SAMPLE EMAIL PREDICTIONS
# ------------------------------------------------------------

sample_emails = [
    "Please verify your account using the official security portal.",
    "The team meeting is scheduled for tomorrow at 10 AM.",
    "Your account requires immediate security verification.",
    "Please review the meeting notes attached to this message."
]

sample_predictions = model.predict(sample_emails)

print("\nSample Predictions")
print("-" * 40)

sample_results = []

for email, prediction in zip(sample_emails, sample_predictions):

    if prediction == 1:
        label = "PHISHING"
    else:
        label = "LEGITIMATE"

    print(f"\n{label}:")
    print(email)

    sample_results.append({
        "email": email,
        "prediction": label
    })


# ------------------------------------------------------------
# 12. SAVE MODEL REPORT
# ------------------------------------------------------------

model_report = {
    "project": "Day 12 - Phishing Email Detection with ML",
    "algorithm": "Multinomial Naive Bayes",
    "dataset": {
        "total_samples": len(df),
        "phishing": phishing_count,
        "legitimate": legitimate_count
    },
    "training_samples": len(X_train),
    "testing_samples": len(X_test),
    "accuracy": round(float(accuracy), 4),
    "accuracy_percentage": round(float(accuracy * 100), 2),
    "confusion_matrix": cm.tolist(),
    "classification_report": report,
    "sample_predictions": sample_results
}

report_path = "Day12_Phishing_Email_ML/model_report.json"

with open(report_path, "w", encoding="utf-8") as file:
    json.dump(model_report, file, indent=4)


# ------------------------------------------------------------
# 13. COMPLETION MESSAGE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("REPORT SAVED")
print("=" * 60)

print(f"\nReport file: {report_path}")

print("\nDay 12 completed successfully!")