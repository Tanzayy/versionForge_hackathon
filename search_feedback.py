# search_feedback.py
def search_feedback_by_student_name(feedback_list, student_name):
    """Searches feedback by student name."""
    if not isinstance(feedback_list, list):
        raise TypeError("Input feedback_list must be a list.")
    if not isinstance(student_name, str):
        raise TypeError("Input student_name must be a string.")

    results = [feedback for feedback in feedback_list if isinstance(feedback, dict) and feedback.get("student_name") == student_name]
    return results

if __name__ == "__main__":
    feedback_data = [
        {"student_name": "Alice", "feedback_text": "Good", "rating": 4},
        {"student_name": "Bob", "feedback_text": "Excellent", "rating": 5},
        {"student_name": "Alice", "feedback_text": "Needs improvement", "rating": 2}
    ]
    search_results = search_feedback_by_student_name(feedback_data, "Alice")
    print(search_results)
