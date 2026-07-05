#String Functions 

str = "I am a student of python programming"
print(str.endswith("er"))#returns True if the string ends with the specified value, otherwise False
print(str.startswith("I")) #returns True if the string starts with the specified value, otherwise False
print(str.capitalize()) #returns a copy of the string with its first character capitalized and the rest lowercased
print(str.upper()) #returns a copy of the string with all the cased characters converted to uppercase
print(str.lower()) #returns a copy of the string with all the cased characters converted to
print(str.replace("python", "java")) #returns a copy of the string with all occurrences of a substring replaced with another substring
print(str.find("student")) #returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1
print(str.count("a")) #returns the number of occurrences of a substring in the string
