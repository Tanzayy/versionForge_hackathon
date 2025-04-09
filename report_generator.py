# report_generator.py
def export_feedback_to_txt(feedback_list, filename="feedback_report.txt"):
    """Exports feedback data to a .txt file."""
    if not isinstance(feedback_list, list):
        raise TypeError("Input must be a list.")

    try:
        with open(filename, "w") as f:
            for feedback in feedback_list:
                if isinstance(feedback, dict):
                    f.write(f"Student: {feedback.get('student_name', 'Unknown')}\n")
                    f.write(f"Feedback: {feedback.get('feedback_text', 'No feedback')}\n")
                    f.write(f"Rating: {feedback.get('rating', 'N/A')}\n")
                    f.write("-" * 20 + "\n")
        return True
    except Exception as e:
        print(f"Error exporting feedback: {e}")
        return False

if __name__ == "__main__":
    feedback_data = [
        {"student_name": "Alice", "feedback_text": "Great lecture!", "rating": 5},
        {"student_name": "Bob", "feedback_text": "Could be better.", "rating": 3}
    ]
    if export_feedback_to_txt(feedback_data):
        print("Feedback exported successfully.")
    else:
        print("Feedback export failed.")
