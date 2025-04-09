# tests/test_feedback_summary.py
import pytest
from feedback_summary import summarize_feedback

def test_summarize_feedback_valid():
    feedback_list = [
        {"student_name": "Alice", "rating": 4},
        {"student_name": "Bob", "rating": 5},
        {"student_name": "Charlie", "rating": 2},
        {"student_name": "David", "rating": 5},
        {"student_name": "Eve", "rating": 4},
        {"student_name": "Frank", "rating": 5}
    ]
    summary = summarize_feedback(feedback_list)
    assert summary["top_scores"] == [(5, 3), (4, 2), (2, 1)]
    assert summary["grade_counts"] == {4: 2, 5: 3, 2: 1}

def test_summarize_feedback_empty():
    assert summarize_feedback([]) == {"top_scores": [], "grade_counts": {}}

def test_summarize_feedback_invalid_data():
    feedback_list = [
        {"student_name": "Alice", "rating": 4},
        {"student_name": "Bob", "rating": "invalid"}
    ]
    assert summarize_feedback(feedback_list) == {"top_scores": [(4, 1)], "grade_counts": {4: 1}}

def test_summarize_feedback_type_error():
    with pytest.raises(TypeError):
        summarize_feedback("invalid")
