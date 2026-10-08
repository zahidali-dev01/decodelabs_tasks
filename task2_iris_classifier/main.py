"""
Iris Classifier — Supervised Learning Project

A small end-to-end classification project using the Iris dataset,
StandardScaler, and K-Nearest Neighbors (KNN).

Pipeline:
1. Load the Iris dataset
2. Inspect the data
3. Split into training/testing sets (80/20)
4. Scale features
5. Train a KNN classifier
6. Evaluate with accuracy, confusion matrix, precision, recall, and F1
7. Predict new flower measurements
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


OUTPUT_DIR = Path("outputs")
RANDOM_STATE = 42
TEST_SIZE = 0.20
K_NEIGHBORS = 5


def load_data():
    """Load the built-in Iris dataset into a DataFrame."""
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name="target")
    target_names = iris.target_names
    return X, y, target_names


def build_model(X_train, y_train):
    """Scale training data and fit the KNN classifier."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = KNeighborsClassifier(n_neighbors=K_NEIGHBORS)
    model.fit(X_train_scaled, y_train)

    return scaler, model


def evaluate_model(scaler, model, X_test, y_test, target_names):
    """Evaluate the trained model and save a confusion matrix."""
    X_test_scaled = scaler.transform(X_test)
    predictions = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted", zero_division=0)
    recall = recall_score(y_test, predictions, average="weighted", zero_division=0)
    f1 = f1_score(y_test, predictions, average="weighted", zero_division=0)
    matrix = confusion_matrix(y_test, predictions)

    OUTPUT_DIR.mkdir(exist_ok=True)

    report = classification_report(
        y_test,
        predictions,
        target_names=target_names,
        zero_division=0,
    )
    (OUTPUT_DIR / "classification_report.txt").write_text(report, encoding="utf-8")

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=target_names,
    )
    display.plot()
    plt.title("Iris Classifier — Confusion Matrix")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=150)
    plt.close()

    return accuracy, precision, recall, f1, matrix


def predict_example(scaler, model, target_names):
    """Predict the class of one example flower."""
    sample = pd.DataFrame(
        [[5.1, 3.5, 1.4, 0.2]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ],
    )
    scaled_sample = scaler.transform(sample)
    prediction = model.predict(scaled_sample)[0]
    probabilities = model.predict_proba(scaled_sample)[0]

    print("\nExample Prediction")
    print("-" * 40)
    print("Measurements:", sample.iloc[0].tolist())
    print("Predicted class:", target_names[prediction])
    print("Class probabilities:")
    for name, probability in zip(target_names, probabilities):
        print(f"  {name:<10}: {probability:.2%}")


def main():
    print("=" * 58)
    print("             🌸 Iris Classifier")
    print("        Supervised Learning with KNN")
    print("=" * 58)

    X, y, target_names = load_data()

    print("\nDataset")
    print("-" * 40)
    print(f"Samples:  {len(X)}")
    print(f"Features: {X.shape[1]}")
    print(f"Classes:  {', '.join(target_names)}")
    print("\nFirst 5 rows:")
    print(X.head().to_string(index=False))

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
        shuffle=True,
    )

    print("\nTrain/Test Split")
    print("-" * 40)
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples:  {len(X_test)}")
    print("Split ratio: 80/20")

    scaler, model = build_model(X_train, y_train)

    accuracy, precision, recall, f1, matrix = evaluate_model(
        scaler, model, X_test, y_test, target_names
    )

    print("\nModel Evaluation")
    print("-" * 40)
    print(f"Algorithm: K-Nearest Neighbors (K={K_NEIGHBORS})")
    print(f"Accuracy:  {accuracy:.4f} ({accuracy:.2%})")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    print("\nConfusion Matrix")
    print(matrix)

    predict_example(scaler, model, target_names)

    print("\nSaved outputs:")
    print(f"  {OUTPUT_DIR / 'confusion_matrix.png'}")
    print(f"  {OUTPUT_DIR / 'classification_report.txt'}")
    print("\nProject completed successfully. ✅")


if __name__ == "__main__":
    main()
