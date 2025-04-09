# tests/test_search_feedback.py
import pytest
from search_feedback import search_feedback_by_student_name

def test_search_feedback_by_student_name_valid():
    feedback_list = [
        {"student_name": "Alice", "feedback_text": "Good", "rating": 4},
        {"student_name": "Bob", "feedback_text": "Excellent", "rating": 5},
        {"student_name": "Alice", "feedback_text": "Needs improvement", "rating": 2}
    ]
    results = search_feedback_by_student_name(feedback_list, "Alice")
    assert len(results) == 2
    assert results[0]["student_name"] == "Alice"

def test_search_feedback_by_student_name_not_found():
    feedback_list = [
        {"student_name": "Alice", "feedback_text": "Good", "rating": 4},
        {"student_name": "Bob", "feedback_text": "Excellent", "rating": 5}
    ]
    results = search_feedback_by_student_name(feedback_list, "Charlie")
    assert len(results) == 0

def test_search_feedback_by_student_name_type_error():
    with pytest.raises(TypeError):
        search_feedback_by_student_name("invalid", "Alice")
    with pytest.raises(TypeError):
        search_feedback_by_student_name([], 123)
