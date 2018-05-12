#Create empty list to put number that is squared in
#append the number that is squared into empty list
#for loop to square numbers, put range 0, number+1 because last one is not in list
#print new list that contains number that is squared
#return that result to save in function

#list comprehension way


def square(number):
    squList = [i * i for i in range(0,number+1)]
    return squList


print(square(10))


