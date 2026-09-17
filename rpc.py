import time
import random

answers = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}


def show_menu():
    print("")
    print("\x1b[31mROCK\x1b[0m \x1b[32mPAPER\x1b[0m \x1b[35mSCISSORS\x1b[0m \x1b[1mGAME\x1b[0m")
    print("")
    print("\x1b[7mV 1.0 by leifde\x1b[27m")
    print("")
    print("")
    time.sleep(0.5)


def get_player_choice():
    print("")
    print("Choose your Option:")
    print("")
    time.sleep(0.5)

    print("1. \x1b[31mRock\x1b[0m")
    time.sleep(0.5)

    print("2. \x1b[32mPaper\x1b[0m")
    time.sleep(0.5)

    print("3. \x1b[35mScissors\x1b[0m")
    print("")
    print("")

    while True:
        try:
            personal_answer = int(input("Your Option: "))
            print("")

            if personal_answer in answers:
                return personal_answer
            else:
                print("Choose one of the options!")
                print("")

        except ValueError:
            print("")
            print("Please enter a number!")
            print("")


def get_computer_choice():
    computer_answer = random.choice(list(answers.keys()))
    return computer_answer


def determine_winner(personal_answer, computer_answer):
    print("")
    print("Your Choice:", answers[personal_answer])
    print("")
    print("Computer's Choice:", answers[computer_answer])
    print("")

    if computer_answer == personal_answer:
        print("")
        print("\x1b[33mIt's a tie!\x1b[0m")
        print("")

    elif (
        (personal_answer == 1 and computer_answer == 3)
        or (personal_answer == 2 and computer_answer == 1)
        or (personal_answer == 3 and computer_answer == 2)
    ):
        print("")
        print("\x1b[32mYou win!\x1b[0m")
        print("")

    else:
        print("")
        print("\x1b[31mYou lose!\x1b[0m")
        print("")


def game():
    personal_answer = get_player_choice()
    computer_answer = get_computer_choice()

    determine_winner(personal_answer, computer_answer)


if __name__ == "__main__":
    show_menu()

    while True:
        game()

        choice = input("Play again? (y/n): ").strip().lower()

        if choice != "y":
            print("")
            print("Game closed.")
            break

        print("")
        print("------------------------------")
        print("")