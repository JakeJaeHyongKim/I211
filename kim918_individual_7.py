#Jake Kim
#Group 10

#problem 1

#first, import xml etree module for element tree
#create function

#set root of tree as library.xml file
#set where to start from in file (book section)
#write for loop to go over every book in section
#if bookid for fuction equals to the attribute of book, put information to variable
#return variable
#return not found if nothing equavelent
#It only shows "NOT FOUND", so I tried in "print" way instead

import xml.etree.ElementTree as ET
#1

def display_book(id):

#2
    root = ET.parse(source="library.xml")
    #3
    books = root.iter("book")
    #4
    for book in books:
    #5
        if book.attrib == {'id' : id}:
        #6
            title = book.find("title")
            author = book.find("author")
            price = book.find("price")
            print("Title: ",title.text,"\n", "Author: ", author.text, "\n", "Price: ", price.text)
            print("-"*30)
##          info = book.find("title").text + "; " + book.find("author").text + "; " + book.find("price").text
            #7
##          return info
            #8
##        return "NOT FOUND"

        #9

    #problem 2
    
    #use findall to make a list of everything that is found in section (because it should be multiple of results I want)
    #set variables for all of the information that I need
    #create for loop to go thorugh the section to find the "computer" book released in "December"
    #set range of lenth of everything in list that is formed with books that qualifies my criteria
    #if statement, if the book is published on December (use index, because it is a list)
    #print the results
    
    published = root.findall("book/publish_date")
    author = root.findall("book/author")
    title = root.findall("book/title")
    price = root.findall("book/price")
    #1,2
    
    for i in range(len(published)):
        #3,4
        
        if published[i].text.split("-")[1] == "12":
            #5,6
            print("Author: ", author[i].text)
            print("Title: ", title[i].text)
            print("Price: ", price[i].text)
            #7
            
    print("-"*30)

    #problem 3
    #find every genre of the book, need to use findall since it could be multiple of it
    #use for loop to go through every genre in section
    #just print result (text inside <>" "<>), since I only need results of one

    genres =root.findall("book/genre")
    
    #1
    for genre in genres:
        #2
        print(genre.text)
        #3

    
display_book("bk107")





