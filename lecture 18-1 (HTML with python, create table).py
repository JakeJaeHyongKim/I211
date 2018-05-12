
#1. Input initial data
#2. Create html template
#3. create table in body
#4. for loop to look over the data and take the data into table, enter column first then row
import re, urllib.request

data = [["Item", "Cost", "Type"], ["Coke", "$2", "Drink"],
        ["Water", "$0", "Drink"], ["Fries", "$4", "Appetizer"],
        ["Onion Rings", "$3", "Appetizer"], ["Steak", "$12", "Entree"],
        ["Chicken", "$8", "Entree"], ["Caesar Salad", "$7", "Entree"]]

out = open("template2.html", "w")

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>table</title>
</head>
<body>
	{content}
</body>
</html>"""
table="<table border=1>"
for row in data:
    table+="<tr>"
    
    for column in row:
        table+="<td>"+column+"</td>"
        
    table+="</tr>"
    
table+="</table>"


out.write(html.format(content=table))
out.close()

print("Finished writing.")

#back to list

lst = []
web_open = urllib.request.urlopen("file:///C:/Users/ttgy9/Box%20Sync/2018%20SPRING%20(kim918@indiana.edu)/INFO-I211/template2.html")

content = web_open.read().decode(errors = "replace")

web_open.close()

row_data = re.findall('(?<=<tr>).+?(?=</tr>)', content, re.DOTALL)

for item in row_data:
    column_data = re.findall('(?<=<td>).+?(?=</td>)', item, re.DOTALL)
    lst.append(column_data)

print(lst)
