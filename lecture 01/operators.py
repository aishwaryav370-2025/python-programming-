#An operators is a symbol that performs a certain operation between operands.
#Arithmetic operators 
a = 5
b = 6 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b) #remainder is called modulus operator

#relational operators 
a = 50 
b = 20 
print(a == b) #equal to
print(a != b) #not equal to
print(a > b) #greater than
print(a < b) #less than
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to

#Assignment operators
num = 10 
num += 10 
num -= 5
num *= 2
num /= 5
num **= 2
num %= 3
print("num :" , num )

#Logical operators
#not, and, or
a = 50
b = 30 
print(not True)
print(not False)
print(not (a < b)) 

#And operator
val1 = True
val2 = True
print("and operator : ", val1 and val2)

#Or operator 
val1 = True
val2 = True
print("or operator : ", val1 or val2)

print("or operator : ", (a == b ) or (a < b))