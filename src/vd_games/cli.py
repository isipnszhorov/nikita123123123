import prompt

def welcome_user():
    print("VD-games")
    print("Welcome to the VD-games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
