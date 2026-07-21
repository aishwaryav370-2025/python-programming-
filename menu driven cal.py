a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

ch = int(input("Enter choice: "))

if ch == 1:
    print(a + b)
elif ch == 2:
    print(a - b)
elif ch == 3:
    print(a * b)
elif ch == 4:
    print(a / b)
else:
    print("Invalid Choice")