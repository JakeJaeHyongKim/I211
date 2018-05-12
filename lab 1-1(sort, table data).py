#1. I setup inputStatements (titles)
#2. Save inputStatements into sublist
#3. looping to reask input statements (5 times)
#4. For each loop, repeats step 2
#5. When sublist is created, put it into main list


info=[]

for i in range(2):
    
    user=[]
    #sublist

    age = input("how old are you?")
   
    user.append(int(age))
     #sets the input as integer
    name = input("what is your name?")
    user.append(name)
    
    homeTown = input("where are you from?")
    user.append(homeTown)
    
    info.append(user)

info.sort()
#save sorted information

title="{}\t{}\t{}"
#It's going to be 3 input in title. \ separates things, t makes tab between.
titles = ["NAME","AGE","HOMETOWN"]

print(title.format(titles[1],titles[0],titles[2]))
#print titles as formatted
      
print("_"*40)
    #print dashes
      
for i in info:
    print(title.format(i[1],i[0],i[2]))
    #print in order
    
