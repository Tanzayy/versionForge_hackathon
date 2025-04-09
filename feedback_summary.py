# feedback_summary.py
from collections import Counter

def summarize_feedback(feedback_list):
    """Summarizes feedback, showing top scores and grade-wise counts."""
    if not isinstance(feedback_list, list):
        raise TypeError("Input must be a list.")

    ratings = [feedback["rating"] for feedback in feedback_list if isinstance(feedback, dict) and "rating" in feedback and isinstance(feedback["rating"], int)]
    if not ratings:
        return {"top_scores": [], "grade_counts": {}}

    top_scores = Counter(ratings).most_common(3)  # Get top 3 scores
    grade_counts = Counter(ratings)

    return {"top_scores": top_scores, "grade_counts": dict(grade_counts)}

if __name__ == "__main__":
    feedback_data = [
        {"student_name": "Alice", "rating": 4},
        {"student_name": "Bob", "rating": 5},
        {"student_name": "Charlie", "rating": 2},
        {"student_name": "David", "rating": 5},
        {"student_name": "Eve", "rating": 4},
        {"student_name": "Frank", "rating": 5}
    ]
    summary = summarize_feedback(feedback_data)
    print(summary)
