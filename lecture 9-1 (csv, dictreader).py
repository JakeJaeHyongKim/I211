#import csv first
#open csv, and read it
#save above as variable (data)
#use dictreader to make it as dictionary, and find companies that have IN in state entry
#use for loop, print a sorted list above in alphabetical order

import csv

data = csv.DictReader(open("companies.csv","r"))

companies = []

for entry in data:

    if  entry["state"] == "IN":
        companies.append(entry["company_name"])

print(sorted(companies))
