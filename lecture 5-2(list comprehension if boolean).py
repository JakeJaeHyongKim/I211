#create list with [divide number by number that is inputed. if div_number is divisible with 7, return to list. if not, don't save]
#get input for lower bound
#input for upper bound
#input for dividing number
#return number that is divisible by dividing number and print list of it

lower_bound = eval(input("please enter a lower bound (int): "))

upper_bound = eval(input("please enter an upper bount(int): "))
 
div_num = eval(input("please enter a number to divide by (int): "))

div_numList = [num for num in range(lower_bound, upper_bound+1) if num % div_num == 0]


print(div_numList)
