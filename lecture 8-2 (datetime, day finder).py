import datetime, time, random
#import 3 things

#click the stopwatch
start = time.clock()
#begin stopwatch as program begins
while True:
    year = random.randrange(1900, 2001)
    month = random.randrange(1, 13)
    day = random.randrange(1,32)
#random range has to be 1 more than what we need
    try:
        print(datetime.date(year, month, day).strftime("%d %b %Y is a %A on the %d day of %B"))
    #try code to keep run things as recursive
        if year % 7 == 0 and month == 2 and datetime.date(year, month, day).strftime("%A") == "Thursday":
            print("Found one!!!")
            break
    except:
        print("Tried an impossible date:", month, "/", day, "/", year)

#click stopwatch again
end = time.clock()

print("\nTotal time:", end - start, "seconds.")
