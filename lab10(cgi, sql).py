#! /usr/bin/env python3

print('Content-type: text/html\n')

#1. Establish connection with MySQL database
#2. Show tables command in database
#3. save that result
#4. use for loop to gather those result and show

import MySQLdb

"""<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Robot</title>
</head>
<h1>Robot Table</h1>

<body>
	<table border = 1 width='30%'>
	<tr>
	<td>RobotID</td>
	<td>Name</td>
	<td>Weapon</td>
	<td>Active</td>
	<td>Durability</td>
	</tr>
	{content}
	</table>

</body>
</html>"""

string = "i211s18_kim918" 		
password = "my+sql=i211s18_kim918" 	

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


try:				#Always surround .execute with a try!
        SQL = "SELECT * FROM Robot;"
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception as e:	#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:			#This runs if there was no error
        result = ""
        for row in results:
            result+="<tr>"
            for i in row:
                result += "<td>"+str(i)+"</td>"
            result+="</tr>"
        print(html.format(content=result))

