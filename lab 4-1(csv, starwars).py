#import csv first
#create a function listCharacters()
#open the csv by DictReader to make it as dictionary to pull out information
#print out character name, acter/actress name and birthdate with padding


#create function getBios()
#print out a bio of that character as person
#format the output and padding

#provide youngest and oldest person from the above as formatted


import csv, datetime

def listCharacters():
    data = csv.DictReader(open("star-wars.csv","r"))
    char_list = []
    print("-"*60)
    print("MAIN CHARACTERS")
    print("STAR WARS: THE FORCE AWAKENS")
    print("-"*60)
    
    for entry in data:
        char_list.append(((entry["name"],entry["character"],entry["birthday"])))

    for cast in sorted(char_list):

        name, character, birthday = cast

        cast_space = 40 - len(name)
        char_space = 40 - len(character)
        print(name, cast_space*" ", character, char_space*" ", birthday)

listCharacters()


def getBios():
    data = csv.DictReader(open("star-wars.csv","r"))
    print("-"*60)
    print("BIOS")
    print("-"*60)
    
    friday = []

    
    oldest = 0
    youngest = 1000
    name_oldest = " "
    name_youngest = " "
    for entry in data:
        date = datetime.date.today()

        actual_birthday = entry["birthday"].split("/")

        birthday = datetime.date(int(actual_birthday[2]), int(actual_birthday[0]), int(actual_birthday[1]))
        
        age = date - birthday
        age_int = int(age.days/365)
                 

        if age_int > oldest:
            oldest = age_int
            name_oldest = entry["name"]
        if age_int < youngest:
            youngest  = age_int
            name_youngest = entry["name"]
        if birthday.strftime("%A")== "Friday":
            friday.append(entry["name"])
    print("The oldest cast member is ", name_oldest, " who is ", oldest, " years old.")
    print("The youngest cast member is ", name_youngest, " who is ", youngest, " years old.")
            

    print("Cast members born on a Friday:\n")
    for i in friday:
        print(i)
            
    data = csv.DictReader(open("star-wars.csv","r"))
    
    for entry in data:
        
        date = datetime.date.today()

        actual_birthday = entry["birthday"].split("/")

        birthday = datetime.date(int(actual_birthday[2]), int(actual_birthday[0]), int(actual_birthday[1]))
        
        age = date - birthday
        age_int = int(age.days/365)
        
        print(entry["character"], " is played by ", entry["name"], " who was born on ", birthday.strftime("%A"), birthday.strftime("%B"), actual_birthday[1], actual_birthday[2], ".")
        
        print(entry["name"], " is ", age_int, " years old.")

getBios()

