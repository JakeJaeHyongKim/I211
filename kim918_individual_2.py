#Jake Kim

#word guessing game

#1. define secret word
#2. create a revealed letter list that starts empty
#3. set wrong guess count to 0
#4. ask the user for a letter
#5. is the letter in the secret word?
#6. if so: add it to the revealed letters list
#	create a blank string
#	for each letter in the secret word, if the letter in revealed letter list, add that letter to string, otherwise add an underscore to string
#7. if letter not in secret word, add one to wrong guess
#8. repeat from step 3

#reference to Deduplicator, 2016, August 7. Random word guessing game. retreived from https://stackoverflow.com/questions/19926167/random-word-guessing-game

word = "key"

word_list = list(word)

def word_guessing():
    
    blanks = '_' * len(word_list)
    blanks_list = list(blanks)
    
    print ()
    
    print ("Word: ",blanks)

    
    print("Welcome to word guessing game by Jake")

    count = 0
    
    while count < 5:

        guess = input("please guess a letter: ")
        if len(guess) == 1:
        
            if guess not in  'abcdefghijklmnopqrstuvwxyz':

                print ("Please only guess letters!")
            
            elif guess in word:
                for letter in word_list:
            
                    if guess == letter:
                        letter_index = word_list.index(guess)
                        #use index to see each word at time
                        blanks_list[letter_index] = guess
                        #I don't get why we use this...I want to ask AI or professor in lab or lecture
                        print("Your guess is correct!")
                
            else:
                count += 1
                print("Your guess is wrong!", " You attempted", count, " times")

                
        else:
            print("please only guess 1 letter at time.")

            print()
        if blanks_list == word_list:

            print("Congraturation!")
            break
        
        else:

            print("Word: ", "".join(blanks_list))
            
    print("Game Over, the secret word is: ", word)
    
#word_guessing()


#rock scissor paper game

import random
#Algoritm 1

print("Welcome to JK's rock, paper, scissors game!")
#Algoritm 2


pick = ["rock", "paper", "scissors"]
#Algoritm 4

computerPick = random.choice(pick)
#Algoritm 5


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


#reference. Jared, (February 20th, 2016). Your First Python Game: Rock, Paper, Scissors. https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
