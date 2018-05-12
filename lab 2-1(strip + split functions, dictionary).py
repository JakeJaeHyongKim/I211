#1. clear nestiness in data by using for loop for strip and split (have to be str)
#2. New list
data=['50 apples\n','25 pears\n','10 oranges\n']

groceries = []

for item in data:
    #need for loop for .strip and . split function (these r string functions, not list. Need to take out each items in list)
    num, fruit = item.strip().split(" ")
    groceries.append([num, fruit])
    
groceries[2][0]

print(groceries)


#2. create dictionary


groceriesDict = {}

for item in data:
    num, fruit = item.strip().split(" ")
    groceriesDict[fruit] = num
    #key is fruit, need to get value which is num
    
print(groceriesDict["apples"])
#when I put fruit name, print number
