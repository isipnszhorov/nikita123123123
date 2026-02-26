import random


def main():
    print("Welcome to the VD-games!")
    
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    needed_correct = 3
    
    while correct_answers < needed_correct:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        answer = input("Your answer: ").strip().lower()
        
        if (number % 2 == 0 and answer == "yes") or (number % 2 != 0 and answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            correct_answer = "yes" if number % 2 == 0 else "no"
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
