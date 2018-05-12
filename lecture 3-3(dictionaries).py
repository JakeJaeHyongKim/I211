#dictionaries
# adding value dict[key]= value

scores = {"Dave" : 125, "Abby" : 100, "Carrie" : 275, "Ben" : 150}

print("Current Players:")
print(sorted(scores.keys()))
#backslash is \ in this

user_in = input("Please enter a player name:")

if user_in in scores.keys():
    print("The Score for ", user_in, "is", scores[user_in])
