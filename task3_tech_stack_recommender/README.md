# Tech Stack Recommender — AI Recommendation Logic

A practical content-based recommendation system that maps a user's skills
to relevant career/job roles.

## Project Goal

The system takes at least three user skills, converts the user profile and
job-role skill profiles into TF-IDF vectors, calculates cosine similarity,
sorts the scores, and returns the Top-N most relevant career paths.

```text
User Skills
    ↓
TF-IDF Vector Mapping
    ↓
Cosine Similarity
    ↓
Sort by Similarity
    ↓
Top-3 Recommendations
```

## Example Input

```text
Python
Cloud Computing
Automation
```

## Dataset

`data/raw_skills.csv` contains job roles and their associated skill profiles.
The dataset is intentionally small and readable so the recommendation logic
can be understood and tested easily.

## How It Works

### 1. Ingestion
The program loads `raw_skills.csv`.

### 2. TF-IDF
The user's skills and every job-role skill profile are converted into a
shared numerical vector space.

### 3. Cosine Similarity
Cosine similarity compares the direction of the user vector with each
job-role vector. A higher score means stronger skill alignment.

### 4. Sorting
Job roles are sorted from the highest similarity score to the lowest.

### 5. Filtering
The system returns the Top 3 recommendations by default.

## Run on Windows

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run with the default example:

```bash
python main.py
```

Or provide your own three or more skills:

```bash
python main.py --skills Python SQL Machine Learning
```

You can also change the number of recommendations:

```bash
python main.py --skills Python Cloud Automation --top-n 5
```

## Project Structure

```text
task3_tech_stack_recommender/
├── data/
│   └── raw_skills.csv
├── outputs/
│   └── recommendations.csv
├── main.py
├── requirements.txt
└── README.md
```

## Author

**Zahid Ali**

This project demonstrates content-based recommendation, TF-IDF feature
extraction, cosine similarity, ranking, and Top-N filtering.
