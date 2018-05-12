import re, urllib.request, random, webbrowser

def findLink(url):
    
    url = 'https://en.wikipedia.org/wiki/2016_in_film'
    
    print("Searching: ", url)

    web_open = urllib.request.urlopen(url)

    contents = web_open.read().decode(errors = "replace")


    web_open.close()

    body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)[0]
    #don't close body
    links = re.findall('(?<=href=")/wiki.+?(?=")',body, re.DOTALL)
    wiki_link = [link for link in links if ".org" not in link]
    
    return wiki_link

url_list = findLink('https://en.wikipedia.org/wiki/2016_in_film')

for url in url_list:
    print("\t", url)

user_in = input("Please select a link: ")

jumps = eval(input("How many jumps would you like to have? "))

for jump in range(jumps):
    
    randomList = findLink(user_in)
    print("Jumping from:", user_in)
    tries = random.choice(randomList)
    user_in = "https://en.wikipedia.org"+str(tries)
    print("To", user_in)
    webbrowser.open_new_tab(user_in)
