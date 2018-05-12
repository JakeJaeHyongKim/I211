#! /usr/bin/env python3

print('Content-type: text/html\n')

#1. Establish connection with MySQL database
#2. Show tables command in database
#3. save that result
#4. use for loop to gather those result and show

import MySQLdb

string = "i211s18_kim918" 		#change username to yours!!!
password = "my+sql=i211s18_kim918" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


try:				#Always surround .execute with a try!
        SQL = "SELECT * FROM Faculty;"
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception as e:	#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:				#This runs if there was no error
        result = ""
        table = "<html>\n<head><title>Faculty Table</title></head>\n<body><table border='1' width='30%'>\n"
        header = "<tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th></tr>"
        htmlend = "</tr>\n</table>\n</body></html>"
        for row in results:
            for i in row:
                result += "<td>"+str(i)+"</td>"
            
        print(table,"<tr>", header,result, htmlend)
