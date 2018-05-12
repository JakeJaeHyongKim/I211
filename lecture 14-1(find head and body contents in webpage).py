#import re, urllib, request to look up webpage and find contents
#in HTML, head is <head> and body is <body>

import re, urllib.request

def findContents(url):
    print("Searching: ", url)

    web_page = urllib.request.urlopen(url)
    contents = web_page.read().decode(errors="replace")
    web_page.close()

    
    head = re.findall('(?<=<head>).+?(?=</head>)', contents, re.DOTALL)[0]
        
    body = re.findall('?<=<body>).+?(?=</body>)',contents, re.DOTALL)[0]
    return head,body

findContents('http://cgi.soic.indiana.edu/~dpierz/test.html')

head, body = findContents(contents)
