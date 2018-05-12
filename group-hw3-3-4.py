import sqlite3

db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()



userin1 = input("Who would you like to update?")

userin2 = input("Please enter new title. ")

userin3 = input("Please enter new email. ")

userin4 = input("Please enter new areas. ")

def update(cursor):
    SQL = "UPDATE Faculty SET Title = '" + str(userin2)
    SQL += "', Email = '" + str(userin3)
    SQL += "', Areas = '" + str(userin4)
    SQL += "' WHERE Name = '" + str(userin1)+ "';"
    cursor.execute(SQL)
    
update(cursor)
    


db_con.commit()

def displayData(cursor):
    cursor.execute("SELECT * FROM Faculty")
    results = cursor.fetchall()
    result=""
    for row in results:
        for i in row:
            result += str(i)+"\t"
    print(result)

displayData(cursor)

