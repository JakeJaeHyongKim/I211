#Jake Kim
#Group 10
#Lab Practical 1

#create a text file that contains 25 possible passwords
#read a file and make it to list of passwords by list comprehension
#format the output by creating a function called show_list
#Put limitation to select the passwords that qualifies for clues
#Find the password that has same letter twice in a row

pass_list = [line.strip() for line in open("passwords.txt", "r")]
#algoritm 1 & 2

format_output = "{} {} {} {} {}"
def show_list():
    print("The Current possibble passwords are:\n","-"*15)

#algoritm 3
    for i in pass_list[25]:
                   
        print(format_output.format(pass_list[index]))


print("\nclue 1: password is at least 6 characters long\n")
print("The Current possibble passwords are:\n","-"*15)         
clue1 = [format_output.format(word[0]) for word in pass_list if len(word) >= 6]
print(clue1)

print("\nClue 2: password contains at least 1 letter\n")
print("The Current possibble passwords are:\n","-"*15)
clue2 = [format_output.format(word) for word in clue1 if len([let for let in word if let.isalpha()]) >= 1]
print(clue2)

print("\nClue 3: password doesn't start with a vowel, but second character is a vowel\n\n")
print("The Current possibble passwords are:\n","-"*15)
clue3 = [format_output.format(word) for word in clue2 if tuple(word[0]) != "aeiou" and tuple(word[1]) == "aeiou"]
print(clue3)

print("\nClue 4: password has twice more not-vowel letters than vowels\n")
print("The Current possibble passwords are:\n","-"*15)
clue4 = [format_output.format(word) for word in clue3 if len([let for let in word if let in "qwrtyupsdfghjklzxcvbnm"]) > 2*len([let for let in word if let in "aeiou"])]
print(clue4)

print("\nClue 5 (Bonus): password has same letter twice in a row (password, princess)\n")
print("Password Found!\n","-"*15)
clue5 = [format_output.format(word) for word in clue4 if let[i] == let[i]]
print(clue5)
        
show_list()
