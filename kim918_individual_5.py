#Jake Kim
#Group 10

#1. Answer the question: when using strftime what is the placeholder that will display the full name of the day of the week (Monday, Tuesday, etc.).
#(ex. "%d" is the placeholder that displays the day as a two digit number)
#Answer. "%A"

#2. Write an algorithm for step 3.
#First, import datetime
#put today as indicator of dates
#Need to make the date to be displayed in format of year, month, date (split the date input by "/" and change order by index
#change above to be displayed by the name of day (Friday, Saturday, etc)
#Select the items (select name of items) that were sold in weekend (Saturday, Sunday), only.
#print the items selected above

#3. Write a program that reads in the information from a file called ShopRecords.csv

import csv, datetime

data = csv.DictReader(open("ShopRecords.csv","r"))

for entry in data:
    date = datetime.date.today()
    
    date_entry = entry["Date"].split("/")
    
    day = datetime.date(int(date_entry[2]), int(date_entry[0]), int(date_entry[1]))
    
    if day.strftime("%A") == "Saturday" or day.strftime("%A") == "Sunday":
        
        print(entry["Item"])
