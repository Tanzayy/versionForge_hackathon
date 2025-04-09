# count_feedback.py
def count_total_feedback(feedback_list):
    """Counts the total number of feedback entries."""
    if not isinstance(feedback_list, list):
        raise TypeError("Input must be a list.")
    return len(feedback_list)

if __name__ == "__main__":
    feedback_data = [
        {"student_name": "Alice", "feedback_text": "Good", "rating": 4},
        {"student_name": "Bob", "feedback_text": "Excellent", "rating": 5},
        {"student_name": "Charlie", "feedback_text": "Needs improvement", "rating": 2}
    ]
    count = count_total_feedback(feedback_data)
    print(f"Total feedback entries: {count}")
