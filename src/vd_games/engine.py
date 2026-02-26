"""Game engine for VD games."""

import prompt


def run_game(game_module):
    """
    Run a game using the game engine
    Args:
        game_module: Module with get_question_and_answer() function
                    and DESCRIPTION constant
    """
    print("Welcome to the VD Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.DESCRIPTION)

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        question, correct_answer = game_module.get_question_and_answer()
        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ").strip().lower()

        if user_answer == str(correct_answer).lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
