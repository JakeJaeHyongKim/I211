#import re, urllib.request to parse webpage


import re, urllib.request

def parseWeb(url):
    print("Searching: ", url)
    

    web_open = urllib.request.urlopen(url)

    contents = web_open.read().decode(errors = "replace")


    web_open.close()
    
    websites = re.findall('(?<=href=")http.+?(?=")', contents)
    
    for website in websites:
        print(website)

parseWeb('http://www.sice.indiana.edu/about/contact/index.html')
