# tests/test_score_calculator.py
import pytest
from score_calculator import calculate_average_score

def test_calculate_average_score_valid():
    feedback_list = [
        {"student_name": "Alice", "rating": 4},
        {"student_name": "Bob", "rating": 5},
        {"student_name": "Charlie", "rating": 2}
    ]
    assert calculate_average_score(feedback_list) == 3.6666666666666665

def test_calculate_average_score_empty():
    assert calculate_average_score([]) == 0

def test_calculate_average_score_invalid_data():
    feedback_list = [
        {"student_name": "Alice", "rating": 4},
        {"student_name": "Bob", "rating": "invalid"}
    ]
    assert calculate_average_score(feedback_list) == 4
