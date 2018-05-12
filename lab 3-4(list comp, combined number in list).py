#lab practical example
#appeal only what I need as output, #1= sort it

nums = ["123", "321", "435", "2468"]

num_order = [num for num in nums if [digit for digit in num] == \
             sorted([digit for digit in num])]

print(num_order)


lst1 = [1,2,3]
lst2 = sorted([1,2,3])

#2= only odd numbers as output

nums = ["123", "321", "435", "2468"]

num_odd = [num for num in nums if [digit for digit in num if int(digit) % 2 == 1] == \
             sorted([ digit for digit in num if int(digit) % 2 == 1 ])]

print(num_odd)
