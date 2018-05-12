#Jake Kim
#Group 10
#Individual HW 4

#1. where can you find the Standard Documentation for Python?
#On Idle, there is a tab of "Help". Python doc is in that tab. Also, I can simply press F1 button for it.

##2. Write an algorithm for step 3.
#import os
##needs to have input to ask user's input for directory
#from home directory
#change path to new one that user had input
#look for files (contents) in the directory
#find a file that contains name of draft
#rename it to final, instead of draft

##3. Write a program that asks the user for a path to a directory, then updates the names of all the files in the directory that contain the word draft to instead say final
##     EX: "term paper (draft).txt" would be renamed "term paper (final).txt"
        
##BONUS (5pts): for any .txt file that your program changes the name of, have your program add a line of text that states "Edited on "
    #           followed by the current date to the end of the text in the file that it is editing.


import os, datetime

date = datetime.date.today()

user_in = input("Please enter a directory: ")

home = os.getcwd()

new_home = os.path.join(home, user_in)

os.chdir(new_home)

contents = os.listdir(new_home)

for file in contents:
    
    if "draft" in file:
        new_contents = os.rename(file, file.replace("draft", "final"))
        print(file.replace("draft", "final"))
        print("Edited on: ", date)
