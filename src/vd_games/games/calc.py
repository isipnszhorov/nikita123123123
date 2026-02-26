"""Calculator game."""

import random

DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():
    """Generate question and answer for calculator game."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:  # operation == '*'
        correct_answer = num1 * num2
    
    question = f"{num1} {operation} {num2}"
    return question, str(correct_answer)
