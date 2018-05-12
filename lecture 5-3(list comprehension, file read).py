#get input for file name
#read file, read words

#print the words in file that contains 2 or more vowels

file_name = input("please enter a file name: ")

file_contents = [word.strip() for word in open(file_name, "r")]
#apply .function to transformation, that changes the format of output

print(file_contents)

words = [word for word in file_contents if len([let for let in word if let in "aeiou"]) >= 2 ]

print(words)
