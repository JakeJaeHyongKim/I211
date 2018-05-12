#! /usr/bin/env python3

print("Content=type:text/html\n")


out = open("cgi_tables.cgi", "w")

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Tables in CGI</title>
</head>
<body>
	{content}
</body>
</html>"""

table="<table border=1>"

for row in range(1,11):
    table+="<tr>"
    
    for column in range(1,11):
        table+="<td>"+"row"+str(row)+"colum"+str(column)+"</td>"
        
    table+="</tr>"
    
table+="</table>"


out.write(html.format(content=table))
out.close()

print(table, "\nFinished writing.")

