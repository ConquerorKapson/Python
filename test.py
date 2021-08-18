import blackjackart
# from replit import clear
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
your_cards = []
dealer_cards = []

def distribute():
    for i in range(2):
        your_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    print(f"Your cards are: {your_cards},Score:{sum(your_cards)}")
    print(f"Dealer's first card is: [{dealer_cards[0]}]")

def distribute_dealer():
    while sum(dealer_cards)<17:
        dealer_cards.append(random.choice(cards))

def is_equal():
    return sum(your_cards)==sum(dealer_cards)

def sum_handler(ls):
    for i in range(len(ls)):
        if ls[i]==11 and sum(ls)>21:
            ls[i]=1
    return sum(ls)<21

def dealer_turn():
    while sum(dealer_cards)<17:
        dealer_cards.append(random.choice(cards))
        if sum(dealer_cards)>21:
            if sum_handler(dealer_cards):
                continue
            else:
                return

def result():
    print(f"Your cards are: {your_cards},Score:{sum(your_cards)}")
    print(f"Dealer's cards are: {dealer_cards},Score:{sum(dealer_cards)}")
    print("")

def start():
    distribute()
    if sum(your_cards)==21:
        distribute_dealer()
        if sum(dealer_cards)== sum(your_cards):
            print(f"Dealer's cards are: {dealer_cards},Score:{sum(dealer_cards)}")
            print("IT'S A DRAW ! 🙃")
            return
    elif sum(your_cards)<21:
        choice = input("Do you want a hit?(y/n): ").lower()
        while choice == 'y':
            your_cards.append(random.choice(cards))
            if sum(your_cards)==21:
                break
            elif sum(your_cards)<21:
                print(f"Your cards are: {your_cards}; Score:{sum(your_cards)}")
            elif sum(your_cards)>21:
                if sum_handler(your_cards):
                    print(f"Your cards are: {your_cards}; Score:{sum(your_cards)}")
                    pass
                else:
                    print(f"Your cards are: {your_cards}; Score:{sum(your_cards)}")
                    print("YOU LOSE ☹️  ")
                    return
            choice = input("Do you want a hit?(y/n): ").lower()
    dealer_turn()
    dealer_sum = sum(dealer_cards)
    if is_equal():
        result()
        print("IT'S A DRAW ! 🙃 ")
        return
    elif dealer_sum>21:
        result()
        print("HURRAY YOU WON  🥳  AB TO PARTY HOGI !!!")
        return
    elif dealer_sum < 21:
        if dealer_sum > sum(your_cards):
            result()
            print("DEALER WON  🥺 ")
            return
        else:
            result()
            print("HURRAY YOU WON  🥳  AB TO PARTY HOGI!!!")
            return
    elif dealer_sum == 21:
        result()
        print("DEALER WON  🥺 ")
        return


print(blackjackart.logo)
shuru_kare = input("Do you want to start the blackjack game?(y/n): ").lower()
if shuru_kare=='y':
    start()
play_again = input("\nDo you want to play again?(y/n): ").lower()
while play_again == 'y':
    # clear()
    print(blackjackart.logo)
    your_cards = []
    dealer_cards = []
    start()
    play_again = input("\nDo you want to play again?(y/n): ").lower()

