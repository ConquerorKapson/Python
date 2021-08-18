print("Welcome to banda/bandi dhoondho program :)")
print('''
************************************************
#             .,,,,,,,,,,.                     *
#          ,;;;;;;;;;;;;;;,                    *
#        ,;;;;;;;;;;;)));;(((,,;;;,,_          *
#       ,;;;;;;;;;;'      |))))))))))))\       *
#       ;;;;;;/ )''    - /,)))((((((((((\      *
#       ;;;;' \        ~|\  ))))))))))))))     *
#       /     /         |   ((((((((((((((     *
#     /'      \      _/~'    ')|()))))))))     *
#   /'         `\   />     o_/)))((((((((      *
#  /          /' `~~(____ /  ()))))))))))      *
# |     ---,   \        \     ((((((((((       *
#           `\   \~-_____|      ))))))))       *
#             `\  |      |_.---.  \            *
************************************************
''')
print("Aapka banda ya bandi ko daaku pakad ke le gaye hai ab kya aap unhe dhoondh payenge")
print("\nYour mission is to find your banda/bandi.\n")
gen1 = input("Are you a boy or girl? (type boy/girl): ")
if(gen1 == "boy"):
    gen="girl"
else:
    gen = "boy"
step1 = input("""Where will you go first left, right, or forward? (type the answer in lower case) : """)
if(step1 == "left"):
    step2 = input("""\nAap highway pe aa chuke hai ab aapko road cross karni hai\na)cross the road\nb)dont cross the road (Type a/b)\n:""")
    if(step2=="a"):
        print("\nRoad cross karte karte aapko koi uda gaya, Game Over!!!")
    elif(step2 == "b"):
        print(f"""\nAap road hi cross hi nahi karoge to kya khaak pohonchoge {gen}friend ke pass, Game Over!!!""")

elif(step1 == "right"):
    step2 = input("""\nAap kaali pahaadi ke peeche aa chuke hai. ab left mein ek andheri gali hai aur right mein gufa. kahaan jayenge left ya right?""")
    if(step2 == "right"):
        print("""\nGufa mein janwar the aur vo aapko khaa chuke hai, Game Over!!!""")
    elif(step2 == "left"):
        step3 = input("""\nAap andheri gali main hai aur aapko ek gun mili hai ab aap kya karenge \na)use uthayenge aur aage chalenge.\nb)aise hi aage badh jayenge(Type a/b)\n:""")
        if(step3 == "a"):
            step4 = input(f"""\naapko daaku mil gaya\na)Shoot kardo\nb)usse kaho ki piase lele lekin mere {gen}friend ko chhod de.(Type a/b)\n:""")
            if(step4 == "a"):
                print(f"""\nuhh ohhh daaku to mar gaya lekin aapke pass to {gen}friend hai hi nahi ab jaaye aur araamse kone mein ro le :), game completed itni hi thi khelne ke liye dhanyawaad""")
            elif(step4 == 'b'):
                print("""\nusne aapse paise bhi leliye aur aapko goli maardi, Game Over !!!""")
        elif(step3 == 'b'):
            print("Tum Gun nahi leke jaoge lekin Daaku ke pass to hogi na Lallu, protection kaise hogi -_- Game Over!!!")

else:
    if(gen1 == "boy"):
        print("""\nAapka pehla kadam aapko khaayi ke andar le gaya yahaan aap mar gaye wahaan aapki maashuka, Game Over!!!""")
    else:
        print("""\nAapka pehla kadam aapko khaayi ke andar le gaya yahaan aap mar gaye wahaan aapka khasam, Game Over!!!""")

