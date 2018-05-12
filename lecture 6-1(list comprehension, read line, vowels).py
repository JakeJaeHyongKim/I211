#get input for file name
#read file, read line

#print the words in file that contains 2 or more vowels

file_name = input("please enter a file name: ")

file_contents = [line.strip() for line in open(file_name, "r")]
#apply .function to transformation, that changes the format of output

print("All lines in the file: ", file_contents)

words = [line for word in file_contents for line in word.split(" ") if len([let for let in line if let in "aeiou"]) >= 2]
#put different variable after for

print("The words in the file that contain 2 or more vowels: ", words)
