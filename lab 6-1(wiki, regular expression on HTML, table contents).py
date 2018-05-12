
import re, urllib.request

def findMovie(url):
    print("Searching: ", url)  

    web_open = urllib.request.urlopen(url)

    contents = web_open.read().decode(errors = "replace")


    web_open.close()
    
    table = re.findall('(?<=of 2016</caption>).+?(?=</table>)',contents,re.DOTALL)[0]

    link = re.findall('(?<=<i><a href=")/wiki.+?(?=")',table, re.DOTALL)

    #don't close body
    empty = []
    
    for i in link:
        if ".org" not in i:
            empty.append(i)
    print(empty)

    
    user_in=input("Please select your favorite movie: ")
    
    newWeb = ("https://en.wikipedia.org/wiki/"+user_in)
    
    web_open = urllib.request.urlopen(newWeb)

    contents = web_open.read().decode(errors = "replace")
    web_open.close()

    
    plot = re.findall('(?<=id="Plot").+?(?="Cast")',user_in, re.DOTALL)

    print(plot)
    
findMovie('https://en.wikipedia.org/wiki/2016_in_film')
