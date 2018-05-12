#import urllib.request module
#create an empty string to put number in
#browse url, read, and save contents as variable
#use while loop to keep put number, until it gets 4 digit code
#if statement to select what we needed
#
#use <form method="get" action="secret_vault.cgi">
#url += add on the values of each variable

import urllib.request

page = ""

num4 = 0
num3 = 0
num2 = 0
num1 = 0

while True:
   
    url= "http://cgi.soic.indiana.edu/~bdemares/secret_vault.cgi?"
    url += "groupname=Group+10&num1="+str(num1)+"&num2="+str(num2)+"&num3="+str(num3)+"&num4="+str(num4)
    print(num1, num2, num3, num4)
    
    

    web_page = urllib.request.urlopen(url)
    lines = web_page.read().decode(errors="replace")
    web_page.close()
    if "Wrong" not in lines:
        break
    #could also use range to automately put numbers in
    if num4 != 9:
        num4 +=1
    else:
        num4 = 0
        if num3 != 9:
            num3 +=1
        else:
            num3 = 0
            if num2 != 9:
                num2 +=1
            else:
                num2 = 0
                if num1 != 9:
                    num1 +=1
                else:
                    num1 = 0

print(lines)




