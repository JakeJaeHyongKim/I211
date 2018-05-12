#! /usr/bin/env python3

import cgitb

cgitb.enable()

print("Content=type:text/html\n")

file1= open("top100moviesAFI.txt","r")
AFI=file1.readlines()
file1.close()

file2= open("top100moviesRT.txt","r")
RT=file2.readlines()
file2.close()

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Top movie comparison</title>
</head>
<body>
	<table border = 1>
	<tr>
	<td>Movie</td>
	<td>AFI Rank</td>
	<td>RT Rank</td>
	</tr>
	{content}
	</table>
	
</body>
</html>"""


table=""

for movie in sorted(set(AFI)|set(RT)):
    if movie in AFI:
        AFI_rank = AFI.index(movie)
    else:
        AFI_rank = "--"
    if movie in RT:
        RT_rank = RT.index(movie)
    else:
        RT_rank = "--"
    
    table+="<tr>"
    
    table+="<td>"+movie+"</td>"+"<td>"+str(AFI_rank)+"</td>"+"<td>"+str(RT_rank)+"</td>"
        
    table+="</tr>"
    

print(html.format(content=table))
