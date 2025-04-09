# feedback_entry.py

def collect_feedback():
    feedback_list = []
    while True:
        name = input("Enter student name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        try:
            score = float(input("Enter feedback score (0-10): "))
            if 0 <= score <= 10:
                feedback_list.append({'name': name, 'score': score})
            else:
                print("Score must be between 0 and 10.")
        except ValueError:
            print("Invalid score. Please enter a number.")
    return feedback_list
