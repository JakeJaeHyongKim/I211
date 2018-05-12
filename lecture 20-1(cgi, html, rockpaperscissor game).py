#! /usr/bin/env python3
print('Content-type: text/html\n')

#1. import modules including cgi, random, and cgitb
#2. copy and paste html format for python
#3. insert dropdown list for user's choice
#4. computer chose its choice randomly
#5. if user chose rock and computer chose scissors, print "You Win"
#6. create more if boolean condition

import cgi, random, cgitb

computer = random.choice("rock","paper","scissors")

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title></head>
    <body>
        <p>You chose
        {user}</p><form method="post" action="speech.cgi">
<p>Choice:
<select name="choice">
	<option>rock</option>
	<option>paper</option>
	<option>scissors</option>
</select>
</p>
<button type="submit">Submit</button>
</form> 

        <p>computer chose {comp}</p>
	<p>{message}</p>
    </body>
</html>"""


form = cgi.FieldStorage()
guess = form.getfirst('guess', 'even')

if (computer == "rock" and guess == "") or \
   (computer == "scissors"  and  == "") or \
   (computer == "paper" and =="")

    message ="You won!"
    
elif:
    (computer==

else:
    message ="You Lose!"

print(html.format(user = guess, comp = num, message = message))
