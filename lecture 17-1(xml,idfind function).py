import xml.etree.ElementTree as ET


def id_find(num):
    
    root = ET.parse("students.xml")
    
    students = root.iter("Student")
    
    
    for student in students:
        
        if student.find("id").text == num:
            
            name = student.find("name/first").text +" " + student.find("name/last").text
            

            return name
        
    return "NOT FOUND"

print(id_find("0019846768"))
print(id_find("0019846789"))
print(id_find("1234567890"))

print("\n")



def fee_find(name):
    
    root = ET.parse("students.xml")
    
    students = root.iter("Student")


    for student in students:
        
        if student.find("name/first").text + " " + student.find("name/last").text == name:
            
            sentence = name + " " + "owes" + " " + student.text + student.attrib +"in" +student.tag

            return sentence
        
    return "NOT FOUND"

print(fee_find("Rose Dawson"))
print(fee_find("Jack Sparrow"))
print(fee_find("No Body"))
