#01. print number from 1 to 100 
i = 1
while i <=100:
    print(i)
    i +=1 
    
#02. print numbers from 100 to 1 
i = 100 
while i >= 1:
    print(i)
    i -= 1
    
#03. Print the multiplication table of number n
n = int(input("Enter the number: "))
i = 1 
while i<=10:
    print(n*i)
    i += 1
    
#04.print the elemet of the following list using a loop 
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(nums):
    print(nums[i])
    i += 1
    
#05.Search for a number x in this tuple using loop:(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36 
i = 1 
while i < len(nums):
    if(nums[i] == x):
        print("FOUND AT INDEX", i)
    i += 1 





