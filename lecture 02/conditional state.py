#conditional statements 

age = 18 
if(age >= 18):
    print("You are eligible to vote")
    if(age<18):
        print("You are not eligible to vote ")
        
light = "Red"
if(light == "green"):
    print("You can go")
elif(light == "Yellow"):
    print("You can wait")
else:
    print("You can stop")
    
num= 5 

if(num > 2):
    print("Number is greater than 2") #indentation is a proper spacing in python
if(num < 10):
    print("Number is less than 10")
    
#grade students based on marks 

marks = int(input("Enter student marks: "))

if(marks >= 90):
     grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>= 70 and marks<80):
    grade = "C"
else:
    grade = "D"
    print("grade of the student ->", grade)
    
    