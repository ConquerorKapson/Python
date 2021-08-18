import random
import my_logos

def game():
    print(my_logos.logo_four)
    difficulty = input("Enter the difficulty level, type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        num = 10
    elif difficulty == 'hard':
        num = 5
    else:
        while difficulty != 'easy' or difficulty !='hard':
            print("Wrong choice, enter again.")
            difficulty = input("Enter the difficulty level, type 'easy' or 'hard': ").lower()
    print(f"You got {num} chances")

    answer = random.randint(1,100)

    print("I have choosen a number from 1 to 100, you have to guess what it is")
    print("")

    while num != 0:
        guess = int(input("Enter your guess: "))
        if guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print("Wohoo 🥳 you guessed it")
            break
        num-=1
        print(f"{num} chances left")
        print(" ")
        if num == 0:
            print("uh ohh, your number of guesses finished  🙃 ")
            print(f"The correct number was {answer}")


game()
play_again = input("Do you want to guess again?(y/n): ")
while play_again=='y':
    game()