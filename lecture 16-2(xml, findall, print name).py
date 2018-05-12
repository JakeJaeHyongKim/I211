import xml.etree.ElementTree as ET

root = ET.parse(source="students.xml")


name = root.findall("Student/name")
print("The students are: ")

for elem in name:
    print(elem.find("first").text, elem.find("last").text)
