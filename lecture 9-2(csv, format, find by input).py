#import csv first

#ask for input
#open csv, and read it by dictreader
#format the title and entry
#save dict above as variable (data)
#use dictreader to make it as dictionary, and find companies that have the inputted state in state entry
#use for loop, print a sorted list above in alphabetical order

import csv

data = csv.DictReader(open("companies.csv","r"))

data_format = "{}\t\t{}"

companies = []

user_in = input("Search for companies in what state? ")

print("-"*60)

for entry in data:

    if  entry["state"] == user_in:
            companies.append((entry["company_name"],entry["web"]))
            #to append 2 items, double (( ))

for company in sorted(companies):

    name, web = company

    name_space = 40 - len(name)

    print(name, name_space*" ", web)
