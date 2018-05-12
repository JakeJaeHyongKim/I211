
## List Comprehensions

result = [ output/transformation  for-loop/iteration  if (boolean)/condition/(optional) ]

# EXAMPLE NO.1 - output and iteration only
squares = []
for x in range(10):
	squares.append(x**2)

squares = [x**2 for x in range(10)]

# Step 1
result_list = []
# Step 2
result_list = [for x in range(10)]
# Step 3
result_list = [x**2 for x in range(10)]
# Ta-da!


# EXAMPLE NO.1 - YOU TRY
doubles = []
for x in range(10):
	doubles.append(x + x)  # or x * 2

# >>>
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# write the list comprehension



# EXAMPLE NO.2 - output, iteration and optional condition
numbers = []
for x in range(100):
	if x % 3 == 0:
		numbers.append(x)

# (resulting list) = [ transformation iteration filter(optional) ]
numbers = [x for x in range(100) if x % 3 == 0]


# EXAMPLE NO.2 - YOU TRY
numbers = []
for x in range(100):
	if x % 10 == 0:
		numbers.append(x)

# >>>
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# write the list comprehension



# EXAMPLE NO.3
# same result, using for loop
letters = ["a","b","c","d","e","f","g"]
for i in range(len(letters)):
	letters[i] = letters[i].upper()

# same result, using list comprehension
letters = [char.upper() for char in letters]

# FYI: what is actually happening in this list comprehension
# not an item replacement, but appending to a new list
letters = ["a","b","c","d","e","f","g"]
result = []
for i in range(len(letters)):
	result[i] = letters[i].upper()
letters = result

# EXAMPLE NO.3 - YOU TRY




# EXAMPLE NO.4
letters = ["a","b","c","d","e","f","g"]
for i in range(len(letters)):
	if letters[i] in "aeiou":
		letters[i] = letters[i].upper()

# EXAMPLE NO.4 - using if/else - another way to say the same thing
letters = ["a","b","c","d","e","f","g"]
result = []
for i in range(len(letters)):
	if letters[i] in "aeiou":
		result.append(letters[i].upper())
	else:
		result.append(letters[i])
letters = result

# EXAMPLE NO.4 - using list comprehension
letters = [letters[i].upper() if letters[i] in "aeiou" else letters[i] for i in range(len(letters))]

# >>>
# ['A', 'b', 'c', 'd', 'E', 'f', 'g']

# EXAMPLE NO.4 - YOU TRY
words = ["apple","ball","candle","dog","egg","frog"]
for i in range(len(words)):
	if len(words[i]) < 4:
		words[i] = words[i].upper()

# >>>
# ['apple', 'ball', 'candle', 'DOG', 'EGG', 'frog']
# >>>
# ['DOG', 'EGG']

# write the list comprehension twice.. once to mimic the first output
# ... and once to mimic what your for loop above did, the second output
words = [word.upper() for word in words if len(word) < 4]


## Dictionary Comprehensions
## See slides for a dictionary / counting example

# a_list = [11, 12, 13, 14, 15, 16]
# b_list = ["a", "b", "c", "d", "e", "f"]
# a_dict = {a_list[i]:b_list[i] for i in range(len(a_list))}
# print a_dict

# >>>
# {11: 'a', 12: 'b', 13: 'c', 14: 'd', 15: 'e', 16: 'f'}
