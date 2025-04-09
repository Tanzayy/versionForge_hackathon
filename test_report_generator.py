# tests/test_report_generator.py
import pytest
import os
from report_generator import export_feedback_to_txt

def test_export_feedback_to_txt_valid():
    feedback_list = [
        {"student_name": "Alice", "feedback_text": "Great lecture!", "rating": 5},
        {"student_name": "Bob", "feedback_text": "Could be better.", "rating": 3}
    ]
    assert export_feedback_to_txt(feedback_list, "test_report.txt")
    assert os.path.exists("test_report.txt")
    os.remove("test_report.txt")

def test_export_feedback_to_txt_empty():
    assert export_feedback_to_txt([], "test_report.txt")
    assert os.path.exists("test_report.txt")
    os.remove("test_report.txt")

def test_export_feedback_to_txt_invalid_data():
    feedback_list = [
        {"student_name": "Alice", "feedback_text": "Great lecture!", "rating": 5},
        "invalid_data"
    ]
    assert export_feedback_to_txt(feedback_list, "test_report.txt")
    assert os.path.exists("test_report.txt")
    os.remove("test_report.txt")

def test_export_feedback_to_txt_type_error():
    with pytest.raises(TypeError):
        export_feedback_to_txt("invalid", "test_report.txt")
