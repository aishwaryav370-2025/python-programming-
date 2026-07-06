###WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value

marks = {}

x = int(input("enter phy:  "))
marks.update({"phy": x})

x = int(input("enter math: "))
marks.update({"math" : x})

x = int(input("enter chem: "))
marks.update({"chem": x})

print(marks)

#figure out a way to store 9 and 9.0 as separate values in the set (u can take helpof built in data types )
values = {9, '9.0'}
print(values)

#or 

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)