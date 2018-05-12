#set letter and number matching
#create dictionary 1=i, 3=e, 4=a, 5=s, 7=t
#ask user for phrase that wants to be translated in program
#if user inputs a number that is not in the dictionary, print out a letter itself or print out a number that was inputted

matching = {"1" : "i", "3" : "e", "4" : "a", "5" : "s", "7" : "t"}

user_in = input("please enter the phrase to translate: ")

output = [matching[let] if let in matching.keys() else let for let in user_in]

print("The Output is: ", "".join(output))
