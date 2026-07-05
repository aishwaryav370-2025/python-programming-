#WAP to check if a number entered by the uses is odd or even 
num = int(input("Enter number: "))

if(num %2 == 0):
    print("Even")
else:
    print("odd")
    
#WAP to find the greatest of 3 numbers entered by the user
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third number is largest", c)
    
#WAP to check if a number is multiple of 7 or not 
x = int(input("enter number: "))
if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
     
    
