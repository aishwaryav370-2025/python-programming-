#indexing
str = "Aishwarya"
chr = str[4]
print(chr)
chr = str[-1]
print(chr)

#slicing 
#Accessing parts of a strings 
#str[starting_index : ending_index  ] #ending index is not included 

str = "My self Aishwarya and I am learning python programming"
sub_str = str[0:7]
print(sub_str)

str1 = "My self Aishwarya and I am learning python programming"
print(str1[ : 10]) #starting index is not mentioned so it will start from 0
print(str1[10 : ]) #ending index is not mentioned so it will go till the end of the string
print(str1[ : ]) #starting and ending index is not mentioned so it will print the whole string
print(str1[: : 3]) #starting and ending index is not mentioned and step size is 3 so it will print every 3rd character of the string
print(str1[7:len(str1)])

#Negative indexing and slicing
str2 = "My self Aishwarya and I am learning python programming"
print(str2[-6:-3]) #starting index is -3 and ending index is -6 so it will print the characters from -3 to -6
print(str2[-5:-3])
print(str2[-14: ])
print(str2[ : -14])