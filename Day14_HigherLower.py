import random
# from replit import clear
import z_higher_lower
import game_data

def select_question():
    num = random.randint(0, len(game_data.data)-1)
    return {
        "number": num,
        "name":game_data.data[num]['name'],
        "follower": game_data.data[num]['follower_count'],
        "description": game_data.data[num]['description'],
        "country":game_data.data[num]['country'],
    }

def display(x):
    print(f"{x['name']}, a {x['description']} from {x['country']}.")

def is_correct(A,B,x):
    if A['follower'] > B['follower'] and x == "A":
        return True
    elif A['follower'] < B['follower'] and x == "B":
        return True
    else:
        return False

def game(flag,score):
    while flag == True:
        print(z_higher_lower.logo)
        A = select_question()
        B = select_question()
        while A['number'] == B['number']:
            B = select_question()

        print("")
        print("A: ", end = "")
        display(A)
        print(z_higher_lower.vs)
        print("B: ", end = "")
        display(B)
        print("")
        print(f"Your present score is:{score}")
        choice = input("\nWho has more followers? type A or B: ").upper()
        while choice !="A" and choice !="B":
            print("You entered a wrong choice enter again !!!")
            choice = input("\nWho has more followers? type A or B: ").upper()

        if is_correct(A,B,choice):
            score+=1
        else:
            print("")
            print("Uh ohh you went wrong :( ")
            print(f"Your total score was: {score}")
            flag = False
            break
        # clear()


game(True,0)
val = input("\nDo you want to play again?(y/n): ").lower()
while val == 'y':
    # clear()
    game(True,0)
    val = input("\nDo you want to play again?(y/n): ").lower()

print("Bye Bye")