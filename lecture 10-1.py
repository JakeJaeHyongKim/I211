#import urllib.request to enable url programming
#create a function called getContent
#set an URL as variable
#print output as a file with same name, "filename".html (basename)
#if there is no basename, print index.html

import urllib.request, os

def getContent():

    webpage = urllib.request.urlopen("http://www.sice.indiana.edu/")

    contents = webpage.read().decode(errors = "replace")

    webpage.close()
    base_web = os.path.basename("http://www.sice.indiana.edu/")
    if not base_web:
        base_web = "index.html"
        
    file = open(base_web, "w", encoding = "utf-8")
    file.write(contents)
    file.close()
    
getContent()

