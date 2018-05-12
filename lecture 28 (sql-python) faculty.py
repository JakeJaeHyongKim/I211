#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi

def results_table(records):
    html = """
    <!doctype html>
    <html>
    <head><meta charset="utf-8">
    <title>Faculty Add</title></head>
        <body>
            <h1>New Faculty Member Added!</h1>
            <table border='1' width='100%'>
            <tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th></tr>
            {content}
            </table>
            <p><a href="FacultyAdd.html">Go Back</a></p>

        </body>
    </html>"""

    table = ""
    for row in records:
            table += "<tr>"
            for item in row:
                table += "<td  align='center'><a href='FacultyDelete.cgi?fid=" + str(row[0]) + "'>Delete</a></td></tr>"
            table += "</tr>"
    print(html.format(content = table))
form = cgi.FieldStorage()

fid = form.getfirst("fid", "")
name = form.getfirst("name", "")
title = form.getfirst("title", "")
email = form.getfirst("email", "")
areas = form.getfirst("areas", "")
    
#establish DB connection
string = "i211s18_username" 	#change this to yours
password = "my+sql=i211s18_username"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


try:				#Always surround .execute with a try!
        SQL = "INSERT INTO Faculty (Name, Title, Email, Areas)"
        SQL += "VALUES('" + name + "','" + title + "','" + email + "','"
        SQL += areas + "');"
        cursor.execute(SQL)
        db_con.commit()            

        SQL = "SELECT * FROM Faculty; "
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception as e:		#Here we handle the error
        print '<p>Something went wrong with the SQL!</p>'
        print SQL
        print "\nError:", e
else:				#This runs if there was no error
        results_table(results)
