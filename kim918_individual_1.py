#Rock Paper Scissors game
#User- "enter" rock, or paper, or scissors
#computer- "choose" rock, or paper, or scissors (random)

# I used following website for reference. Jared, (February 20th, 2016). Your First Python Game: Rock, Paper, Scissors. https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

#Algorithms:
#1. Import radint from import module
#2. Show welcome message to user
#3."Get input from user by asking (do you want rock? or paper? or scissors?)
#4. Create a list of options with rock, paper, and scissors for computer to be able to pick randomly in each game
#5. Allow computer to only pick from lists by inserting range from 0 to 2 in list
#6. Make the game begins when user input value
#7. Repeats until player don't input, the input from player is True
#8. When user wins (ex. user= rock, computer= scissors), show "Win!". When user and computer tie (ex. rock and rock), show "Ties!". When User loses (ex. user= paper, computer= scissors), show "lose!"
#9. If the input from user is spelled wrong or not valid input, print "not valid"

from random import randint
#Algoritm 1

print("Welcome to JK's rock, paper, scissors game!")
#Algoritm 2


pick = ["rock", "paper", "scissors"]
#Algoritm 4

computerPick = pick[randint(0,2)]
#Algoritm 5

user = False
#Make user don't input yet, game doesn't begin. Algoritm 7. Set user value before begins.

while user == False:
#set user True when user inputs. Algorithm 7, Algoritm 8. Keep repeats the game until user doesn't put any input

    
    user = input("Do you want rock? or paper? or scissors?")
    #get user input, so game starts. Algorithm 3

    if user == computerPick:
        print ("Ties!")
    #easier to code when there is one common thing can be set in beginning. If user and computer picks same thing, it is tie. #Algorithm 8
    elif user == "rock":
        if computerPick == "scissors":
            print("win!")
        else:
            print("lose")
    elif user == "scissors":
        if computerPick == "paper":
            print("win!")
        else:
            print("lose")
    elif user == "paper":
        if computerPick == "rock":
            print("win!")
        else:
            print("lose")
    else:
        print("Invalid, try again")
        #Algoritm 9


    user = False
    computerPick= pick[randint(0,2)]
    #so game continues after games, resets the value

#3
#"A program" that takes a string as input
#Takes a string as input.
#reverse the order of all characters in the string.
#pring reversed version of string to user.
    
#reference: Bergantino, P. (May 31, 2009). Reverse a string in Python. https://stackoverflow.com/questions/931092/reverse-a-string-in-python

user = str(input("Type string:"))

reverseUser = user[::-1]
    #[::-1] makes string to be reversed. begin:end:step in string

print(reverseUser)






#4.
#takes 2 lists (input)
#figure out if there is anything in common between 2 lists
#if there is any member in lists is common, True. Otherwise, False.

#reference: jivoi.(September 30, 2016). junk/python_simple_ex/ex10.py. https://github.com/jivoi/junk/blob/master/python_simple_ex/ex10.py

def common(list1, list2):
    #need to compare items in 2 lists
    
    for item1 in list1:
        #for items in list 1
        for item2 in list2:
            #for items in list 2
            if item1 == item2:
                #if those two have same element
                return True
                #print True
                break
                #Then, break the loop
            
    return False
    #otherwise, print False
print(common([1, 2, 3], [1, 4, 5]))

print(common([1, 2, 3, 5], [4, 0, 6]))
