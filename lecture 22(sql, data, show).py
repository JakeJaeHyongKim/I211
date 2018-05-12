#! /usr/bin/env python3

print('Content-type: text/html\n')

#1. Establish connection with MySQL database
#2. Show tables in database

import MySQLdb

string = "i211s18_kim918" 		#change username to yours!!!
password = "my+sql=i211s18_kim918" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


try:				#Always surround .execute with a try!
        SQL = "SHOW TABLES;"
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception as e:	#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:				#This runs if there was no error
        result = ""
        for row in results:
                result += row+'<br>'
        print("The current tables in the Database are:\n", result)
