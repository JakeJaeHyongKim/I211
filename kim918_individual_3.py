#Jake Kim
#Group 10

##Develop an algorithm to solve all remaining steps in this problem.
##Use a list comprehension to load the data from a file named “teams.txt”. There’s a sample filePreview the documentView in a new window on Canvas with the data shown above.
##Print out the information read in from the file formatted as shown in the example.
##Use a list comprehension to create a list of the names of teams with less than 5 letters in their name.
##Use a list comprehension to create a list of the names of the three teams with the highest wins.

#load a text file, read line by line the file
#strip the line
#split the line
#print the words and # in line as formatted

#select and list teams that have less than 5 letters
#select and list teams that have the highest wins, in this case, more than 7 wins (if I can, select top 3)


fileContents = [line.strip().split(" ") for line in open("teams.txt", "r")]

for i in fileContents:
    print("The",i[0]," have won", i[1], " games")

short_name = [word[0] for word in fileContents if len(word[0]) < 5]
#select and print words that have less than 5 letters (len), use index to only select from first item in line which is name
#print those names in string

print("Teams with names shorter than 5 letters: ", short_name)

team_flip = sorted([[int(word[1]),word[0]] for word in fileContents], reverse = True)
#reverse = True makes the outcome to be descending order

#we can use 2 different list comprehensive to make it easier

win_team = [team_flip[i][1] for i in range(3)]

#double indexing
print("The three teams with the highest wins are: ", win_team)

