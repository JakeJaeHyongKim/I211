#Jake Kim
#Group 10

#first import modules (re, urllib.request, webbrowser)
#webbrowser is needed for bonus
#open the webpage that is given in the assignment sheet
#read contents in the webpage, set a variable to recall it later
#close the webpage
#print the beginning phrase, searching ....
#use re.findall to find every title of the news in the contents variable (that was set previously)
#need to use for loop to eliminate unrelevant (not needed) contents
#print outcome of for loop

#ask for user input to search that input word in titles
#find the titles that have that word from user
#print outcomes of it

#for bonus, I need to use a re.findall to find the url of those titles that are found in previous one.
#set variable for that urls to be able to use later
#use webbrowser.open_new_tab module to open those url in browser

import re, urllib.request, webbrowser

web_page = urllib.request.urlopen('http://cgi.soic.indiana.edu/~dpierz/news.html')

contents = web_page.read().decode(errors="replace")

web_page.close()

print("Searching: http://cgi.soic.indiana.edu/~dpierz/news.html\n")

title = re.findall('(?<=<span itemprop="headline">).+?(?=</span>)',contents,re.DOTALL)

for i in title:
    if ".edu" not in title:
        print("\t",i,"\n")
        
web_page = urllib.request.urlopen('http://cgi.soic.indiana.edu/~dpierz/news.html')


contents = web_page.read().decode(errors="replace")

web_page.close()

user_in = input("Please enter a word to search for: ")


title = re.findall('(?<=<span itemprop="headline">).+?(?=</span>)',contents,re.DOTALL)

user_title = re.findall('(?<=)user_in.+?(?=")',title,re.DOTALL)

url = re.findall('(?<=<h1><a itemprop="url" href=").+?(?=">)',contents,re.DOTALL)
#find url of those webpages that has user_in in title. It has to be brought from original contents, because it is out of range of title.

for word in user_in:
    if word == user_title:
        print(word)
#I tried to get those News titles that contains the user_in, but it is not running properly.


webbrowser.open_new_tab(url)
