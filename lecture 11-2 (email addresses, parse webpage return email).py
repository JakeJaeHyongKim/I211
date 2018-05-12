#open the webpage
#get contents from webpage
#print matched items (email)
import re, urllib.request

def getEmail():

    user_in = input("Search what page?")

    web_open = urllib.request.urlopen(user_in)
    contents = web_open.read().decode(errors = "replace")

    web_open.close()
    print("The email addresses in ", web_open, " are", re.findall('[\w]*[.]*[-]*[a-z]+[@][a-z]+[\w]',contents))

getEmail()
