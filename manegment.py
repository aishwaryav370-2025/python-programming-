name = input("Enter student name: ")
roll = input("Enter roll number: ")
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))
total = m1 + m2 + m3
average = total / 3
print("\nStudent Details")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total)
print("Average:", average)
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: F")
print("Program Completed")