# tests/test_count_feedback.py
import pytest
from count_feedback import count_total_feedback

def test_count_total_feedback_valid():
    feedback_list = [
        {"student_name": "Alice", "feedback_text": "Good", "rating": 4},
        {"student_name": "Bob", "feedback_text": "Excellent", "rating": 5},
        {"student_name": "Charlie", "feedback_text": "Needs improvement", "rating": 2}
    ]
    assert count_total_feedback(feedback_list) == 3

def test_count_total_feedback_empty():
    assert count_total_feedback([]) == 0

def test_count_total_feedback_type_error():
    with pytest.raises(TypeError):
        count_total_feedback("invalid")
