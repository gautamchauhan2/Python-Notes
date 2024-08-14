#Dictionary

info={
    "name" : "Gautam",
    "subjects":["python","C","Java"],
    "topics":("dict","set"),
    "age":35,
    "is_adult":True,
    "marks":94.4
    }
#print(info)    

#Nested dictionaries

student={
    "name":"Gautam",
    "Score":{
        "phy":97,
        "math":98,
        "chem":95
    }
}
#nested dictionaries

#stu=student["Score"]["math"]
#print(stu)

#dictionary methods
#print(student.keys())
#print(student.values())
#print(student.items())
print(student.get("name"))