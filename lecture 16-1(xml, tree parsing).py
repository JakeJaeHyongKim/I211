import xml.etree.ElementTree as ET

root = ET.parse("students.xml")

elements = root.iter()

for elem in elements:
    print("Tag Name: ", elem.tag)
    print("Tag Text: ", elem.text)
    print("Children: ", list(elem))

    print("-"*20)
