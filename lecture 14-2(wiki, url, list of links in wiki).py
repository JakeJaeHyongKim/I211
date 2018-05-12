
import re, urllib.request

def findLink(url):
    print("Searching: ", url)  

    web_open = urllib.request.urlopen(url)

    contents = web_open.read().decode(errors = "replace")


    web_open.close()

    body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)[0]
    #don't close body
    link = re.findall('(?<=href=")/wiki.+?(?=")',body, re.DOTALL)
    return link

links = findLink('https://en.wikipedia.org/wiki/2016_in_film')

for i in links:
    if ".org" not in i:
        print(i)
