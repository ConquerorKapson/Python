rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
# from replit import clear
rsp =[rock, paper, scissors];
print("Welcome to rock, paper and scissors game :)))")
you = 0
computer = 0
times = int(input("Number of points of match? "))

while(you < times and computer < times):
    comp = random.randint(0,2)
    human = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))
    if(human>2 or human<0):
        continue;
    print("Machine's choice\n")
    print(rsp[comp])

    print("Your choice\n")
    print(rsp[human])

    if(human == comp):
        print(f"TIE You: {you} and Machine: {computer}")
    elif(human == 0):
        if(comp == 1):
            computer+=1
            print(f"Machine got a point")
            print(f"You: {you} and Machine:{computer}")
        elif(comp == 2):
            you +=1
            print("You got a point")
            print(f"You: {you} and Machine:{computer}")

    elif(human == 1):
        if(comp == 2):
            computer+=1
            print(f"Machine got a point")
            print(f"You: {you} and Machine:{computer}")
        elif(comp == 0):
            you +=1
            print("You got a point")
            print(f"You: {you} and Machine:{computer}")

    elif(human == 2):
        if(comp == 0):
            computer+=1
            print(f"Machine got a point")
            print(f"You: {you} and Machine:{computer}")
        elif(comp == 1):
            you +=1
            print("You got a point")
            print(f"You: {you} and Machine:{computer}")


if(you > computer):
    print("HURRAY YOU WON!!!")
else:
    print("HURRAY I WON!!!")