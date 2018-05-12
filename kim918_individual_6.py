##Answer the question: what is the Python regular expression pattern that would match a hex color code. (for example, the pattern that would match an email address is '[\w.-]+@[\w.-]')
#### '#[\w{6}]'
##
##Write an algorithm for step 3. As part of your algorithm, be sure to describe the pattern you're using to find the win/loss result for each game.

#### First, import  re, urllib.request to use regular expression and search in url
## 2. open the webpage
## 3. read that webpage, set a variable to save those contents.
## 4. create empty list, 0 number counter
## 5. close the webpage
## 6. use regular expression, re.findall, to find the contents of number of games, score in that contents
## 7. add +1 to win or lose
## 8. for those items that I found, make list of those and print the list


##Write a program that looks at the source of http://cgi.soic.indiana.edu/~dpierz/mbball.html (a copy of the IU men's basketball team record page). Use regular expressions to find all the games IU has played in this year and calculate the total number of wins and losses (including exhibition games)
##     The output should look like the following:
##
##Wins: 18
##Losses: 12

import re, urllib.request

web_open = urllib.request.urlopen('http://cgi.soic.indiana.edu/~dpierz/mbball.html')

contents = web_open.read().decode(errors = "replace")

web_open.close()

result = []
win = 0
lose = 0

games = re.findall("(?<=div class='schedule_game_results'><div>).*?(?=</div>)", contents)

for i in games:
    if "W" in i:
        win += 1
    elif "L" in i:
        lose += 1
print("Wins: ", win)

print("Loses: ", lose)

points = 0

for game in games:
    if game:
        first_score = game[2:4]
        second_score = game[5:7]
        points += abs(int(first_score) - int(second_score))

print("Total Difference: ", points)
    
##Bonus [10 pts]. Extend your code from part 3 to also calculate the total difference in points scored in all the games (a game that finished 68-71 would have a difference of 3 points, 85-52 a difference of 33 points etc)
##
##Total Difference: 431
