import re

original = "test loon etta planet aaw meek ziim try"

print("Original: ", original)
print("Match: ", re.findall('[\w]*[aeiou]{2}[\w*]', original))
