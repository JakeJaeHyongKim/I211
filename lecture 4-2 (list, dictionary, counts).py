#create a list with numbers
#create dictionary
#dictionary will store each number and times of appearance
#print number and counts of numbers

numList =[1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    
def numCounts(lst):

    numDict = {}
    
    for num in lst:
        if num in numDict:
            numDict[num] += 1
        else:
            numDict[num] = 1
    return numDict

title = "{0}\t{1}"

titles = ["Number", "Count"]

#main section
print(title.format("Number", "Count"))

lst = numCounts(numList)

for item in lst.items():

    
    print(title.format(item[0],item[1]))
