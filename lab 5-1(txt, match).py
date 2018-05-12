import re

file = open("quote.txt", "r")

fileContents = file.read()

print("Matches: ", re.findall('[A-Z][\w]+', fileContents))
#[a-z] = [\w]
print("Matches: ", re.findall('[a-z]+ing', fileContents))

print("Matches: ", re.findall('[a-z]*a{2}*[a-z]', fileContents))

print("Matches: ", re.findall(',[^?!.,]*,', fileContents))
#^ is everything but not these
print("matchings: ", len(re.findall('[vV][a-z]+', fileContents)))
