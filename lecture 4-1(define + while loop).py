#password should be at least 8 characters long
#keep looping until they provide at least 8 character long password

#1. define password character
#2. create loop with input ("enter a password")- while loop, so it keeps looping)
#3. when user provides right password, stops the loop
#4. print the inputted password with "your password is"

def valid_pass():
#algorithm 1    
    while True:
        
        user = input("Please enter a valid password:")
        #algorithm 2

        if len(user) < 8:
             print("The password should be at least 8 characters long")
             #algorithm 2

        else:
            return user
        #use return, when I want to save the result from fuction
        #algorithm 3
        
            break
            
my_pass = valid_pass()
#save the definition and input

print("Your password is", my_pass)
#algorithm 4
