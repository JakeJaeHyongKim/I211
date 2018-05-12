#1. Choose Topic of adventure
#2. ask question about where to go
#3. If statement to process different action for answer
#4. repeat finished one path of logic

print("Choose Your Own Adventure")

def playGame():
    user_in = input("Where would you like to visit? 1 = Cancun, 2 = London \n")
    
    if user_in == "1":
        print("You chose Cancun! Enjoy being warm!")
        user_in1 = input("What would you like to do in Cancun? 1 = Enjoy sun on the beach, 2 = Drink lots of Tequila\n")

        if user_in1 == "1":
            print("Nice! Go to get some tan")
        elif user_in1 == "2":
            print("Oops! Be careful with that during your trip!")
        else:
            print("Your answer was invalid, please answer again")
    
    elif user_in == "2":
        print("You chose London! Enjoy the city life!")
        user_in2 = input("What would you like to do in London? 1 = Eat good foods, 2 = walk around streets\n")

        if user_in2 == "1":
            print("Yay! There are lots of good foods in London!")
        elif user_in2 == "2":
            print("Yay! The streetview in London is so pretty!")
        else:
            print("Your answer was invalid, please answer again")

    else:
        print("Your answer was invalid, please answer again")

#Repeat with while loop
while True:
    playGame()
    user_in3 = input("Do you want to play another game? 1 = Yes, 2 = No\n")

    if user_in3 == "2":
        break
