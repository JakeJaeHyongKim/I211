import xml.etree.ElementTree as ET

root = ET.parse(source="students.xml")


fee = root.iter("fees")
total = 0
print("The total amount of student fees is: ")

for elem in fee:
    total += int(elem.text)

print("$",total)
    
