"""
Tech Stack Recommender — Project 3

A content-based recommendation system that maps a user's skills to
job roles using TF-IDF vectors and cosine similarity.

The pipeline follows:
Input -> TF-IDF vector mapping -> Cosine Similarity -> Sorting -> Top-N output
"""

from pathlib import Path
import argparse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "raw_skills.csv"
OUTPUT_PATH = BASE_DIR / "outputs" / "recommendations.csv"


def normalize_skill_text(text: str) -> str:
    """Normalize comma-separated skills into a consistent text string."""
    return ", ".join(
        skill.strip().lower()
        for skill in str(text).split(",")
        if skill.strip()
    )


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and validate the job-role dataset."""
    df = pd.read_csv(path)

    required_columns = {"job_role", "skills"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {sorted(missing)}")

    df = df.dropna(subset=["job_role", "skills"]).copy()
    df["skills"] = df["skills"].map(normalize_skill_text)

    if df.empty:
        raise ValueError("The dataset contains no usable job roles.")

    return df


def recommend_roles(user_skills, df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """
    Convert user skills and job-role skills into TF-IDF vectors,
    calculate cosine similarity, then return the highest-scoring roles.
    """
    user_text = normalize_skill_text(", ".join(user_skills))

    # User profile is included in the same corpus so both sides share a vocabulary.
    corpus = [user_text] + df["skills"].tolist()

    vectorizer = TfidfVectorizer(
        token_pattern=r"(?u)\b[\w+#./-]+\b",
        ngram_range=(1, 2),
    )
    vectors = vectorizer.fit_transform(corpus)

    user_vector = vectors[0]
    item_vectors = vectors[1:]

    scores = cosine_similarity(user_vector, item_vectors).flatten()

    results = df[["job_role", "skills"]].copy()
    results["similarity_score"] = scores

    results = (
        results.sort_values(
            by=["similarity_score", "job_role"],
            ascending=[False, True],
        )
        .head(top_n)
        .reset_index(drop=True)
    )

    return results


def save_results(results: pd.DataFrame) -> None:
    """Save the Top-N recommendation list."""
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    results.to_csv(OUTPUT_PATH, index=False)


def display_results(user_skills, results: pd.DataFrame) -> None:
    """Print recommendations in a clean format."""
    print("\n" + "=" * 68)
    print("              💼 Tech Stack Recommender")
    print("          Content-Based Recommendation System")
    print("=" * 68)

    print("\nYour skills:")
    print("  " + ", ".join(user_skills))

    print("\nTop 3 Recommended Career Paths")
    print("-" * 68)

    for index, row in results.iterrows():
        print(
            f"{index + 1}. {row['job_role']:<24} "
            f"Similarity: {row['similarity_score']:.2%}"
        )
        print(f"   Matching skill profile: {row['skills']}")

    print("\nResults saved to:")
    print(f"  {OUTPUT_PATH}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Recommend career paths from three user skills."
    )
    parser.add_argument(
        "--skills",
        nargs="+",
        default=["Python", "Cloud Computing", "Automation"],
        help="At least three user skills, e.g. Python Cloud Automation",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=3,
        help="Number of recommendations to return (default: 3)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if len(args.skills) < 3:
        raise SystemExit("Please provide at least three skills.")

    if args.top_n < 1:
        raise SystemExit("--top-n must be at least 1.")

    df = load_dataset()

    results = recommend_roles(
        user_skills=args.skills,
        df=df,
        top_n=min(args.top_n, len(df)),
    )

    save_results(results)
    display_results(args.skills, results)

    print("\nProject completed successfully. ✅")


if __name__ == "__main__":
    main()
