#Write your code below this line 👇
def prime_checker(number):
    val = 0
    if number==1 or number ==0 or number == -1:
        print(f"{number} is neither prime nor composite")
    elif number ==2:
        print(f"{number} is  a prime number")
    else:
        num = 1
        while num <= number:
            if(number%num == 0):
                val+=1
            num+=1
        if(val == 2):
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")


#Write your code above this line 👆

#Do NOT change any of the code below👇


choice = "y"
while choice == "y":
    try:
        n = int(input("Check this number: "))
        prime_checker(number=n)
    except ValueError:
        print("Wrong input Try again")
        continue
    choice = input("Do you want to enter more (y/n)? ")



