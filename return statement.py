def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i 
        #print("The average is:",sum / len(numbers))
    return sum / len(numbers)

c = average(5, 6, 7)
print(c)

        
        
    