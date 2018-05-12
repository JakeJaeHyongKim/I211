#word list comprehension
#if word contains less than 4 letters, append as upper case
#if not, leave it as it is

words= ["apple", "ball", "candle", "dog", "egg", "frog"]
word = [i.upper() if len(i) < 4 else i for i in words]
#not proper: word = [word.upper() if len(words) < 4 else word for word in words]
#learn how to take only word less than 4 letters

print(word)
