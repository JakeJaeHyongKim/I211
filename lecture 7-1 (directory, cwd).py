#import OS from system
#get input from user for what directory (cwd) is user looking for
#keep ask agiain until it's a valid directory name
#directory in directory.zip

import os

home = os.getcwd()
dir_home = os.listdir(home)

dir_list = []

for file in dir_home:
    
    if os.path.isdir(file):
        
        dir_list.append(file)


print(dir_list)

while True:

    user_in = input("please enter directory: ")

    if user_in in dir_list:

        break

    else:

        print("Invalid directory, please enter again: ")

