#Create 3 lists for even, odd, and non-whole numbers
#Takes number input (10 times)
#sorts numbers into list

evenNum = []

oddNum = []

nonNum = []

for i in range(10):
    #10 times
    
    user_in = eval(input("please enter a number:"))
    # eval is better function to see if the input is integer

    if user_in % 2 == 0 and user_in > 0:
        #/ is just divide, % is divide w/o left over (no remainder)
        # ! is "not"

        evenNum.append(user_in)

    elif user_in % 2 == 1 and user_in >= 0:
        
        oddNum.append(user_in)

    else:

        nonNum.append(user_in)

print("The results are:")

print(evenNum)

print(oddNum)

print(nonNum)
