#first, import OS
#looks through all objects in directory
#find total size of all files in bytes in that directory

#use for loop to get all the file names in directory
#for file, append to calculation
#for folder,return to path

#use os.path.getsize(file_name) with the file names that I got by for loop

import os



def file_size(dir):

    size = 0
    #home
    for file in os.listdir(dir):
        if os.path.isfile(item):
    
        size += os.path.getsize(file)
    elif os.path.isdir(item):
        total += size(os.path.join(os.getcwd(), item))
    
    return file_size(folder)

user_in = input("please enter a directory")
file_size(user_in)
