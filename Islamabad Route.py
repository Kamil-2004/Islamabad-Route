logo = """

o-O-o     o               o           o     o--o            o      
  |       |               |           |     |   |           |      
  |   o-o |  oo o-O-o  oo O-o   oo  o-O     O-Oo  o-o o  o -o- o-o 
  |    \  | | | | | | | | |  | | | |  |     |  \  | | |  |  |  |-' 
o-O-o o-o o o-o-o o o o-o-o-o  o-o- o-o     o   o o-o o--o  o  o-o 

"""
print(logo)


import random

print("Welcome to Islamabad")

r1 = input("Where you want to go: Left (Giga Mall) or Right (Amazon Mall): ").lower()

if r1 == "left":  # if user wants to go to Giga Mall
    r2 = input("If you want to do shopping go to 2nd floor, "
               "if you are hungry then go to the food court which is on the 3rd floor: ")

    if r2 == "2":
        print("Enjoy your shopping")
    elif r2 == "3":
        print("Enjoy your food")
    else:
        print("Please enter the correct floor")

elif r1 == "right":  # if user wants to go to Amazon Mall
    r3 = input("If you want to go to the Mosque then go to the ground floor, "
               "if you want to play then go to the play area: ").lower()

    if r3 == "ground floor" or r3 == "mosque":
        print("Spend time with Allah")
    elif r3 == "play area":
        r4 = input("1. Outdoor\n2. Indoor: ")

        if r4 == "1":
            print("Play outdoor")
        elif r4 == "2":
            print("Play indoor")
        else:
            print("Please enter the correct option")
    else:
        print("Go home")

else:
    print("You entered a wrong route")

