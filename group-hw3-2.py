import sqlite3

db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()

def createFacultyTable(cursor):
    SQL = """CREATE TABLE IF NOT EXISTS Faculty
        (FacultyID int (11) NOT NULL,
        Name varchar (25) NOT NULL,
        Title varchar (100) NOT NULL,
        Email varchar (30),
        Areas varchar (200)
        );"""
    cursor.execute(SQL)

def insertFaculty(cursor, FacultyID, Name, Title, Email, Areas):
    

    SQL = "INSERT INTO Faculty (FacultyID, Name, Title, Email, Areas) VALUES ('"
    SQL += str(FacultyID)+"', '"+str(Name) + "', '" + str(Title) + "', '" +str(Email)+ "', '" + str(Areas) + "');"

    cursor.execute(SQL)
    db_con.commit()

createFacultyTable(cursor)


insertFaculty(cursor, 1, 'Will Smith', 'English teacher', 'willsmith@gmail.com', 'English')
insertFaculty(cursor, 2, 'Mr. Bob', 'Chemistry teacher', 'Bob@yahoo.com', 'Chemistry, Biology')
insertFaculty(cursor, 3, 'Mrs. Williams', 'Geography teacher', 'williams@yahoo.com', 'Geography, History')
insertFaculty(cursor, 4, 'Ms. Robins', 'Calculus Professor', 'mrobins@gmail.com', 'Mathematics')
insertFaculty(cursor, 5, 'Beau Buck', 'History Teacher', 'bb@gmail.com', 'History')
                            

def displayData(cursor):
    cursor.execute("SELECT * FROM Faculty")
    results = cursor.fetchall()
    result=""
    for row in results:
        for i in row:
            result += str(i)+"\t"
    print(result)

displayData(cursor)
