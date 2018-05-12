#first import re
#read a text file
#find all that has email, phone numbers, and proper names
#copy contents and file
#replace it with word "redacted" at the end

import re

file = open("message.txt", "r")

fileContents = file.read()

file.close()

redacted = re.sub('[\w.-]+[@][\w.]+|[(][\d]{3}[)] [\d]{3}-[\d]{4}|[A-Z][a-z]*[ ][A-Z][a-z]*',"redacted", fileContents)

new_file = open("messageRedacted.txt","w")

newContents = new_file.write(redacted)

new_file.close()

