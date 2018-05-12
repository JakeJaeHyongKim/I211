#1. create list with number
#2. move bigger number to right
#3. if the number2 is smaller than number1, number1 moves to right 
#4. repeat step 3 until the list is sorted with smallest number in the left, and the greatest to right(all cases are true).
#5. 

intList=[6,3,2,5,7,1,1,2]

while True:
#to
    swap=False
    
    for i in range(len(intList)-1):
        if intList[i] > intList[i+1]:
            intList[i],intList[i+1]=intList[i+1],intList[i]
            print(intList)
            #To see entire process

            swap=True
            #Run infinitely until everything is sorted correctly.
    if swap==False:
        # one = is setting something, == is boolean value (either True or False)
        break
    
print(intList)
