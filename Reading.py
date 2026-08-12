f = open("demo.txt", "r")

data = f.read(5)
print(data)

f.close()

#If u want to read the file line by line, use readline() menthod.

f = open("demo.txt", "r")
line1 = f.readline()
print(line1)

f.close()

#if first only everthing is read then the next readline() will retrun empty space 

f =open("demo.txt", "r+")
f.write("ABC")
print(f.read())
f.close()


#append mode is used to add data at the end 

f = open("demo.txt", "a+")
f.write("XYZ")
print(f.read())
f.close()
