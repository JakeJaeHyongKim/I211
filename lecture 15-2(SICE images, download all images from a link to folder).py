#create folder
#1. go to see url page
#assign variable to link
#download "image" files from the link to the folder that I created
#Leave their original names

import urllib.request, os, re

def image_list(page):
    
    web_open = urllib.request.urlopen(url)

    contents = web_open.read().decode(errors = "replace")

    web_open.close()
    
    images = re.findall('(?src=").+?(?=")',url, re.DOTALL)
    image_links = [link for link in images if "http" in link]

    return image_links

pictures = image_list(
