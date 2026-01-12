import random

won_by_user = 0
won_by_computer = 0
times_played = 0


def execute():
    print('-' * 20)
    print("Welcome to Number Guessing Game, \nYour mission is guess number with 3 tries, in range 10")
    while True:
        print('-' * 20)
        print("Choose: \n[1] Play\n[2] Session Stats\n[Any] Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            play()
        elif choice == '2':
            stats()
        else:
            quit()


def play():
    global won_by_computer, won_by_user, times_played
    tries = 3
    times_played += 1
    computer_choice = random.randint(0, 10)
    while tries > 0:
        print('-' * 20)
        user_choice = int(input("Enter your number: "))
        if user_choice > computer_choice:
            print('-' * 20)
            print("Your guess is too high")
            tries -= 1
        elif user_choice < computer_choice:
            print('-' * 20)
            print("Your guess is too low")
            tries -= 1
        else:
            print('-' * 20)
            print("You guess is correct")
            won_by_user += 1
            return True
    won_by_computer += 1
    return False


def stats():
    global won_by_user, won_by_computer, times_played
    print('-' * 20)
    print("Won by user: ", won_by_user)
    print("Won by computer: ", won_by_computer)
    print("Times played: ", times_played)


execute()