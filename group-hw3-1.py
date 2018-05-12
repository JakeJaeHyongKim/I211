import sqlite3

db_con = sqlite3.connect("my_db.txt")
cursor = db_con.cursor()

def createPersonTable(cursor):
    SQL = """CREATE TABLE Person
        (PersonID varchar (10) UNIQUE,
        FirstName varchar (25) NOT NULL,
        LastName varchar (25) NOT NULL,
        Birth date NOT NULL,
        Age int DEFAULT 18);"""
    cursor.execute(SQL)
    
def insertPerson(cursor, id_num, fname, lname, bdate, age=18):
    SQL = "INSERT INTO Person (PersonID, FirstName, LastName, Birth, Age)"
    SQL += "VALUES ('" + str(id_num) + "', '" + fname + "', '" + lname + "', '"
    SQL += bdate + "', " + str(age) + ");"
    cursor.execute(SQL)
    
    
#createPersonTable(cursor)
#insertPerson(cursor, 1, 'Jack', 'Sparrow', '1745-04-01', 46)

def createOtherTable(cursor):
    SQL = """CREATE TABLE Other
        (OtherID varchar (10) UNIQUE,
        AnimalName varchar (25) NOT NULL,
        CarBrand varchar (25) NOT NULL,
        SportsTeam varchar (25) NOT NULL,
        RandomInfo varchar(50) NOT NULL);"""
    cursor.execute(SQL)

createPersonTable(cursor)
createOtherTable(cursor) 
db_con.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
results = cursor.fetchall()
print("The current tables in the Database are: ")
result=""
for row in results:
    result+=row[0]+"\t"
print(result)
