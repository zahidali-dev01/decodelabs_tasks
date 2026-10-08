# Iris Classifier — Supervised Learning Project

A small, practical machine-learning project that classifies Iris flowers into
three species using supervised learning.

## Project Goal

The project follows a complete classification workflow:

```text
Iris Dataset
     ↓
Understand Data
     ↓
80/20 Train-Test Split
     ↓
StandardScaler
     ↓
K-Nearest Neighbors (KNN)
     ↓
Predictions
     ↓
Accuracy + Precision + Recall + F1
     ↓
Confusion Matrix
```

## Dataset

The project uses the built-in **Iris dataset** available through
`scikit-learn`.

- 150 samples
- 4 numerical features
- 3 classes:
  - setosa
  - versicolor
  - virginica

The four measurements are sepal length, sepal width, petal length, and petal width.

## Model

**Algorithm:** K-Nearest Neighbors (KNN)

The model uses `k = 5` neighbors. Feature scaling is applied with
`StandardScaler` before training because KNN is distance-based.

## Evaluation

The project reports:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

It also saves:

```text
outputs/
├── confusion_matrix.png
└── classification_report.txt
```

## Installation

Python 3.9+ is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the project directory:

```bash
python main.py
```

## Example Prediction

The program also demonstrates a prediction for:

```text
[5.1, 3.5, 1.4, 0.2]
```

which is expected to belong to the `setosa` class.

## Project Structure

```text
task2_iris_classifier/
├── main.py
├── requirements.txt
├── README.md
└── outputs/
    ├── confusion_matrix.png
    └── classification_report.txt
```

## Author

**Zahid Ali**

This is my implementation of a supervised-learning classification project,
focused on dataset handling, model training, evaluation, and prediction.
