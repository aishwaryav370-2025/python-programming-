#type conversion in python
a = int("2")
b = 4.67
sum = a + b
print(sum)
print(type(a))

a = 2.15
a = str(a)
print(type(a))

#Input in python 
name =input("Enter your name : ")
print('welcome ', name)

val = input("Enter some value: ")
print(type(val), val )

#type casting 
int("5")
val = float(input("Enter some value: "))
print(type(val), val)

name = input("Enter name : ")
age =input("Enter age : ")
marks = input("Enter marks : ")

print("welcome ", name )
print("Your age is : ", age)
print("Your marks are : ", marks)