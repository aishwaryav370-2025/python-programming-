#Dictionaries are used to store data values in key value pairs
info = {
    "Key" : "Value",
    "name" :"Aishwarya",
    "learning" : "coding",
    "age" : 19,
    "marks" :99.99,
    "subject" : ["kannada", "English", "Hindi"],
    "topics" : ("dict", "set"),
    45.67 : 98.78
}

info["name"] = "Pratiksha"
print(info["Key"])
print(info["name"])
print(info["age"])

#Nested Dictionaries
student = {
    "name" : "Aishwarya V",
    "subjects": {
        "phy" : 97,
        "chem" : 88,
        "math" : 99
    }
}

print(student)
print(student["subjects"])


#Dictionary method
print(student.keys())
print(list(student.keys()))
print(len(student))
print(student.values())
print(list(student.values()))
print(student.items())
print(student.get("name"))
student.update({"city" : "blr"})
new_dict = {"age" : 19, "Reg no" : "25BTCE198"}
student.update(new_dict)

print(student)