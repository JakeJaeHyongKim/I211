#User inputs number or stop
#If user inputs number- print
#If user inputs stop- stop
#sum up all the numbers when user inputs stop, then print out

sum_num = 0
#set num list 0


while True:

    user_in = input("Please enter a number or stop:")

    if user_in == "stop":
        
        break
    

    else:
        sum_num += int(user_in)

print(sum_num)
