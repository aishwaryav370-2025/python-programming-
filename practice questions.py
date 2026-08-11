#Write a recursion function to calculatethe sum of first n natural numbers 

def sum_natural(n):
    if n == 0:
        return 0 
    print(n)
    return sum_natural(n-1) + n 

print(sum_natural(5))

#Write a recursive function to print all elements in a list
#Hint: use list & index as parameters 

def print_list(list, index):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)
    
fruits = ["apple", "banana", "cherry", "date"]
print_list(fruits, 0)

