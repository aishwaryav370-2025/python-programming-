#WAP to ask the user to enter names of their 3 favorite movies and store them in a list
movies = []
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#or 
movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))

print(movies)

#WAP to check if a list contains a palindrome of element.
list1 = [1, 2, 1]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Pallindrome")
else:
    print("Not pallidrome ")
    
#WAP to count the number of students with the "A" grade in the following tuple 
#["c","D", "A", "A","B", "B", "A"]

grade = ["c","D", "A", "A","B","B" ,"A"]
print(grade.count("A"))

#Store the above values in a list and sort them from "A" to "D"

list = ["c","D", "A", "A","B", "B", "A"]
list.sort()
print(list)


